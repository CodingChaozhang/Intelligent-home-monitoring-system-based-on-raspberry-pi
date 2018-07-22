# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import MySQLdb
import time
import picamera
from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
import os
#需要填写你的 Access Key 和 Secret Key
access_key = 'h6oX5R-dcDNGBfq1fK9H9QdkQyX2lf1yDvULVieI' #这里的密钥填上刚才我让你记住的密钥对
secret_key = 'FDlqMD7-ZGbheGJlfXRHLiHqsl7XaNqXuf-7xmoM' #这里的密钥填上刚才我让你记住的密钥对
#构建鉴权对象
q = Auth(access_key, secret_key)
#要上传的空间
bucket_name = 'jiankong'
#上传到七牛后保存的文件名
key = '%s_%s_%s_%s_%s_%s.jpg'%(time.localtime()[0],time.localtime()[1],time.localtime()[2],time.localtime()[3],time.localtime()[4],time.localtime()[5])
#生成上传 Token，可以指定过期时间等
token = q.upload_token(bucket_name, key, 3600)
#
camera=picamera.PiCamera()
def uploadfile():
        camera.capture("current_photo.jpg")
	#要上传文件的本地路径
	localfile = 'current_photo.jpg'
	ret, info = put_file(token, key, localfile)
	filename = 'current_photo.jpg'
	if os.path.exists(filename):
		os.remove(filename)
def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.IN)
    GPIO.setup(11,GPIO.OUT)
    pass
def beep():
        for i in range(1,6):
            GPIO.output(11, GPIO.LOW) 
            time.sleep(0.5)
            GPIO.output(11, GPIO.HIGH)
            time.sleep(0.5)
            print "the Buzzer will make sound"
 
def detct():
    for i in range(1, 31):
        if GPIO.input(12) == True:
            print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+ "  Someone is closing!"
            conn=MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='root',
            db='jiankong',
            )
            sql="insert into buzzer(time,descr) values('%s','%s')"%(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),'someone is closing')
            cur=conn.cursor()
            cur.execute(sql)
            cur.close()
            conn.commit()
            conn.close()
            beep()
            uploadfile()
        else:
            GPIO.output(11, GPIO.HIGH)
            print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+"  Noanybody!"
        time.sleep(10)
time.sleep(2)
init()
detct()


