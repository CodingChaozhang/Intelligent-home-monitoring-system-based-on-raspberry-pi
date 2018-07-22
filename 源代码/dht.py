#coding: utf8
import Adafruit_DHT
import MySQLdb  
import datetime
#引入gpio的模块
import RPi.GPIO as GPIO
import time
# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor=Adafruit_DHT.DHT11
  
# Set GPIO sensor is connected to
gpio=4
dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
#设置GPIO模式
GPIO.setmode(GPIO.BOARD)
 
#设置in1到in4接口
IN1 = 13
IN2 = 15
IN3 = 16
IN4 = 18
 
#初始化接口
def init():
    GPIO.setup(IN1,GPIO.OUT)
    GPIO.setup(IN2,GPIO.OUT)
    GPIO.setup(IN3,GPIO.OUT)
    GPIO.setup(IN4,GPIO.OUT)
 #后退
def cabk(sleep_time):
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.HIGH)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.HIGH)
    time.sleep(sleep_time)
    GPIO.cleanup()
# Use read_retry method. This will retry up to 15 times to
# get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
  
# Reading the DHT11 is very sensitive to timings and occasionally
# the Pi might fail to get a valid reading. So check if readings are valid.
if humidity is not None and temperature is not None:
  print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
  print "temperature:",temperature
  print "humidity:",humidity  
  conn=MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='jiankong',
  )
  sql="insert into dht2(time,temperature,humidity) values('%s','%d','%d')"%(dt,temperature,humidity)
  cur=conn.cursor()
  cur.execute(sql)
  cur.close()
  conn.commit()
  conn.close()
  if temperature > 20:
    init()
    cabk(10)
else:
  print('Failed to get reading. Try again!')

