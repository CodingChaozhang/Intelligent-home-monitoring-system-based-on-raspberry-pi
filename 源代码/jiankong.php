<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>家庭实时监控系统</title>
<!-- Bootstrap -->
    <link href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
<!-- jQuery (Bootstrap 的所有 JavaScript 插件都依赖 jQuery，所以必须放在前边) -->
    <script src="https://cdn.bootcss.com/jquery/1.12.4/jquery.min.js"></script>
    <!-- 加载 Bootstrap 的所有 JavaScript 插件。你也可以根据需要只加载单个插件。 -->
    <script src="https://cdn.bootcss.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>

<body>

<center>
<table class="table table-striped">
<h1>家庭实时监控系统</h1>
<br>
<h3 align="left" class="bg-primary">温湿度信息</h3>
<tr><th>时间(yyyy-mm-dd)</th><th>温度(°C)</th><th>湿度(%RH)</th></tr>
<?php
$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "jiankong";

// 创建连接
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("连接失败: " . $conn->connect_error);
}

$sql = "select * from dht2 order by id desc limit 3";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // 输出数据
    while($row = $result->fetch_assoc()) {
        echo"<tr><td>".$row["time"]."</td><td>".$row["temperature"]."</td><td>".$row["humidity"]."</td><tr>";
    }
} else {
    echo "0 结果";
}
$conn->close();
?>
</table>

<table class="table table-striped">
<h3 align="left" class="bg-primary">安防情况</h3>
<tr><th>序号</th><th>时间</th><th>描述</th></tr>
<?php
$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "jiankong";

// 创建连接
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("连接失败: " . $conn->connect_error);
}

$sql = "select * from buzzer order by id desc limit 3";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // 输出数据
    while($row = $result->fetch_assoc()) {
        echo"<tr><td>".$row["id"]."</td><td>".$row["time"]."</td><td>".$row["descr"]."</td><tr>";
    }
} else {
    echo "0 结果";
}
$conn->close();
?>
</table>
</center>
<h3 align="left" class="bg-primary">实时监控情况</h3>
<div>
    <img style="-webkit-user-select: none;cursor: zoom-in;"  src="http://192.168.43.121:8082/?action=stream" width="400" height="300"/>
</div>



</body>
</html>
