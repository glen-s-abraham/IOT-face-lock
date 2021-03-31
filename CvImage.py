import cv2
import base64
import datetime
from tkinter import *
from PIL import Image,ImageTk
from FaceRecognition import recognize
import os
from Lock import Lock
import time

device = cv2.VideoCapture(0) 
lock=Lock(18)
root=Tk()
root.geometry("500x350")
lmain=Label(root)
lmain.pack()

lstatus=Label(root)
lstatus.pack(side="top")

def show_frame():
	_, frame = device.read()
	frame=cv2.flip(frame,1)
	cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
	cv2image=cv2.resize(cv2image,(300,250))
	img = Image.fromarray(frame)
	imgtk = ImageTk.PhotoImage(image=img)
	lmain.imgtk = imgtk
	lmain.configure(image=imgtk)
	lmain.after(10, show_frame)

def capture_image():
	"""captures the frame from webcam"""
	lstatus['text']="Capturing and checking database"
	try:
		ret, frame = device.read()
		fname=save(frame)
		send(fname)
		
	except:
		print("error occured")



def save(img):
	"""save image to disk and uploads"""
	special_char=(" ",":",".")
	filename=str(datetime.datetime.now())
	for char in special_char:
		filename=filename.replace(char,"")

	filename="captures/"+filename+".jpg"
	

	try:
		cv2.imwrite(filename,img)
		return filename
		
		
	except:
		print("Exception saving ")	

def send(filename):
        print(filename)
        files=os.listdir("entities/")
        for file in files:
            to_cmp="entities/"+file
            print(to_cmp)
            if recognize(to_cmp,filename):
                print("unlocked")
                lock.unsetLock()
                time.sleep(5)
                lock.setLock()
                break


show_frame()
btn=Button(root,text="Unlock",command=capture_image)
btn.pack(side="bottom",fill="both",expand="yes",padx=10,pady=10)
root.mainloop()  
device.release()  
    
    
    
    
    
    

 