
import tkinter as tk
from tkinter import Message ,Text
import cv2,os
import shutil
import csv
import numpy as np
#from PIL import Image, ImageTk
import PIL.Image
import PIL.ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font





from tkinter import *
import os
 
# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("400x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=15, height=2, bg="blue", command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("400x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=15, height=2, command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            #login_sucess()
            face_rec()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 




def face_rec():
    global window
    window = tk.Tk()
    window.title("Face_Recogniser")

    dialog_title = 'QUIT'
    dialog_text = 'Are you sure?'
    window.configure(background='black')

    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)


    message = tk.Label(window, text="Face-Recognition-Based-tracking-system" ,bg="LightSteelBlue4"  ,fg="white"  ,width=40  ,height=3,font=('times', 30, 'italic bold')) 

    message.place(x=200, y=20)

    lbl = tk.Label(window, text="Enter ID",width=20  ,height=2  ,fg="slate blue"  ,bg="sky blue" ,font=('times', 15, ' bold ') ) 
    lbl.place(x=300, y=200)

    txt = tk.Entry(window,width=23  ,bg="sky blue" ,fg="slate blue",font=('times', 15, ' bold '))
    txt.place(x=600, y=205,height=45)

    lbl2 = tk.Label(window, text="Enter Name",width=20  ,fg="slate blue"  ,bg="sky blue"    ,height=2 ,font=('times', 15, ' bold ')) 
    lbl2.place(x=300, y=300)

    txt2 = tk.Entry(window,width=20  ,bg="sky blue"  ,fg="slate blue",font=('times', 15, ' bold ')  )
    txt2.place(x=600, y=305,height=45)

    lbl3 = tk.Label(window, text="Notification : ",width=20  ,fg="slate blue"  ,bg="sky blue"  ,height=2 ,font=('times', 15, ' bold underline ')) 
    lbl3.place(x=300, y=400)

    message = tk.Label(window, text="" ,bg="sky blue"  ,fg="slate blue"  ,width=30  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
    message.place(x=600, y=400)

    
    def clear():
        txt.delete(0, 'end')    
        res = ""
        message.configure(text= res)

    def clear2():
        txt2.delete(0, 'end')    
        res = ""
        message.configure(text= res)    
        
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass
    
        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass
    
        return False
    
    def TakeImages():        
        Id=(txt.get())
        name=(txt2.get())
        if(is_number(Id) and name.isalpha()):
            cam = cv2.VideoCapture(0)
            harcascadePath = "haarcascade_frontalface_default.xml"
            detector=cv2.CascadeClassifier(harcascadePath)
            sampleNum=0
            while(True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x,y,w,h) in faces:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                    #incrementing sample number 
                    sampleNum=sampleNum+1
                    #saving the captured face in the dataset folder TrainingImage
                    cv2.imwrite("TrainingImage\ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                    #display the frame
                    cv2.imshow('frame',img)
                #wait for 100 miliseconds 
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    break
                # break if the sample number is morethan 100
                elif sampleNum>60:
                    break
            cam.release()
            cv2.destroyAllWindows() 
            res = "Images Saved for ID : " + Id +" Name : "+ name
            row = [Id , name]
            with open('StudentDetails\StudentDetails.csv','a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
            csvFile.close()
            message.configure(text= res)
        else:
            if(is_number(Id)):
                res = "Enter Alphabetical Name"
                message.configure(text= res)
            if(name.isalpha()):
                res = "Enter Numeric Id"
                message.configure(text= res)
        
    def TrainImages():
        recognizer = cv2.face_LBPHFaceRecognizer.create()#recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector =cv2.CascadeClassifier(harcascadePath)
        faces,Id = getImagesAndLabels("TrainingImage")
        recognizer.train(faces, np.array(Id))
        recognizer.save("TrainingImageLabel\Trainner.yml")
        res = "Image Trained"#+",".join(str(f) for f in Id)
        message.configure(text= res)

    def getImagesAndLabels(path):
        #get the path of all the files in the folder
        imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
        #print(imagePaths)
        
        #create empth face list
        faces=[]
        #create empty ID list
        Ids=[]
        #now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            #loading the image and converting it to gray scale
            pilImage=PIL.Image.open(imagePath).convert('L')
            #Now we are converting the PIL image into numpy array
            imageNp=np.array(pilImage,'uint8')
            #getting the Id from the image
            Id=int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)        
        return faces,Ids

    def TrackImages():
        recognizer = cv2.face.LBPHFaceRecognizer_create()#cv2.createLBPHFaceRecognizer()
        recognizer.read("TrainingImageLabel\Trainner.yml")
        harcascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath);    
        df=pd.read_csv("StudentDetails\StudentDetails.csv")
        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX        
        col_names =  ['Id','Name','Date','Time']
        attendance = pd.DataFrame(columns = col_names)    
        while True:
            ret, im =cam.read()
            gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
            faces=faceCascade.detectMultiScale(gray, 1.2,5)    
            for(x,y,w,h) in faces:
                cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
                Id, conf = recognizer.predict(gray[y:y+h,x:x+w])                                   
                if(conf < 50):
                    ts = time.time()      
                    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                    aa=df.loc[df['Id'] == Id]['Name'].values
                    tt=str(Id)+"-"+aa
                    attendance.loc[len(attendance)] = [Id,aa,date,timeStamp]
                    confid = "  {0}%".format(round(100 - conf))
                else:
                    Id='Unknown'                
                    tt=str(Id)
                    #conf = "  {0}%".format(round(100 - conf))  
                if(conf > 75):
                    #conf = "  {0}%".format(round(100 - conf))
                    noOfFile=len(os.listdir("ImagesUnknown"))+1
                    cv2.imwrite("ImagesUnknown\Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            

               
                cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)        
               # cv2.putText(im, str(confid), (x+5,y+h-5), font, 1, (255,255,0), 1)
            attendance=attendance.drop_duplicates(subset=['Id'],keep='first')    
            cv2.imshow('im',im) 
            if (cv2.waitKey(1)==ord('q')):
                break
        ts = time.time()      
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        Hour,Minute,Second=timeStamp.split(":")
        fileName="Tracking\Tracking_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
        attendance.to_csv(fileName,index=False)
        cam.release()
        cv2.destroyAllWindows()
        #print(attendance)
        res=attendance
        message2.configure(text= res)

    
    clearButton = tk.Button(window, text="Clear", command=clear  ,fg="black"  ,bg="SkyBlue4"  ,width=10  ,height=1 ,activebackground = "SlateBlue3" ,font=('times', 15, ' bold '))
    clearButton.place(x=950, y=200)
    clearButton2 = tk.Button(window, text="Clear", command=clear2  ,fg="black" ,bg="SkyBlue4"  ,width=10  ,height=1, activebackground = "SlateBlue3" ,font=('times', 15, ' bold '))
    clearButton2.place(x=950, y=300)    
    takeImg = tk.Button(window, text="Take Images", command=TakeImages  ,fg="black"  ,bg="SkyBlue4"  ,width=20  ,height=2, activebackground = "SlateBlue3",font=('times', 15, ' bold '))
    takeImg.place(x=100, y=500)
    trainImg = tk.Button(window, text="Train Images", command=TrainImages  ,fg="black"  ,bg="SkyBlue4"  ,width=20  ,height=2, activebackground = "SlateBlue3" ,font=('times', 15, ' bold '))
    trainImg.place(x=400, y=500)
    trackImg = tk.Button(window, text="Track Images", command=TrackImages  ,fg="black"  ,bg="SkyBlue4"  ,width=20  ,height=2, activebackground = "SlateBlue3" ,font=('times', 15, ' bold '))
    trackImg.place(x=700, y=500)
    quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg="black"  ,bg="SkyBlue4"  ,width=20  ,height=2, activebackground = "SlateBlue3" ,font=('times', 15, ' bold '))
    quitWindow.place(x=1000, y=500)
    copyWrite = tk.Text(window, background=window.cget("background"), borderwidth=0,font=('times', 30, 'italic bold underline'))
    copyWrite.tag_configure("superscript", offset=10)
    copyWrite.insert("insert", "Developed by Ashish","", "TEAM", "superscript")
    copyWrite.configure(state="disabled",fg="red"  )
    copyWrite.pack(side="left")
    copyWrite.place(x=800, y=750)
    
    window.mainloop()




# Designing popup for login invalid password
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()









