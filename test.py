import json
import mysql.connector
import cv2
import numpy as np
from pyzbar.pyzbar import decode 

img = cv2.imread('/Users/chaitanya/Desktop/ResearchPaper-2/saurollno.png')
for barcode in decode(img):
	#print(barcode.data)
	myData = barcode.data.decode('utf-8')
	print(myData)

#check_retrieval = "SELECT * from Students where Roll_Number = " + myData #resolved
#safe_update_retrieval = "SET SQL_SAFE_UPDATES = 0;"
update_retrieval = "SET SQL_SAFE_UPDATES = 0; UPDATE Students SET Attendance = 'Present' WHERE Roll_Number = " + myData

mydb = mysql.connector.connect(host="localhost", user="root", passwd="SMCs3789", database="AMS")

mycursor = mydb.cursor()
mycursor.execute(update_retrieval, multi = True)
mydb.commit()
result = mycursor.fetchall()

if len(result)>0:
	print(result)
else:
	print("The ID number cannot be found in Student Records") 


