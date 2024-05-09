#tkinter imports etc
from tkinter import scrolledtext
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import PhotoImage
from tkinter import ttk


#root window 
root = Tk()
#root window title
root.title('Your Recipes')



#ADD WINDOW, (SECOND WINDOW), USED FOR USER TO TYPE IN RECIPES
def addWindow():
    addWindow = Toplevel()
    addWindow.title('Enter Recipe')
    text_area = scrolledtext.ScrolledText(addWindow, width=40, height=10)
    text_area.pack(expand=True, fill='both')


#DEFINING COMMAND FOR RECIPE DISPLAYS
def recipeEntry():
    recipeEntry = Label(addWindow, text=get(text_area))
    recipeEntry.pack()



#DYK WINDOW
def dykWindow():
    dykWindow = Toplevel()
    dykWindow.title('Did you know?')
    myLabel50 = Label(dykWindow, text="Did you know.... that cooking at home is far healthier for us?", padx=20, pady=15, font="bold")
    myLabel60 = Label(dykWindow, text="Read this article from Harvard for more info!>> https://www.health.harvard.edu/blog/home-cooking-good-for-your-health-2018081514449", padx=20, pady=15, font="bold")
    myLabel50.pack()
    myLabel60.pack()

#INFO WINDOW, (FOURTH WINDOW), USED FOR USER TO SEE SOME COOKING BASICS INFO
def infoWindow():
    global my_img2
    infoWindow = Toplevel()
    infoLabel = Label(infoWindow, text="Some Cooking Basics")
    infoWindow.title('Cooking Basics')
    myLabel4 = Label(infoWindow, text="Check if the recipe is in Metric or Imperial measurements!", padx=20, pady=15, font="bold")
    myLabel5 = Label(infoWindow, text="Never scoop flour. Use a scale for accuracy.", padx=20, pady=15, font="bold") 
    myLabel6 = Label(infoWindow, text="Dull knives cause accidents-keep them sharp!", padx=20, pady=15, font="bold") 
    myLabel7 = Label(infoWindow, text="Get all your items measured and ready before you start mixing it together", padx=20, pady=15, font="bold") 
    myLabel8 = Label(infoWindow, text="Last but certainly not least-WASH YOUR HANDS, and keep good sanitary and food safety practices!", padx=20, pady=15, font="bold") 
    infoLabel.grid(row=2, column=0)
    myLabel4.grid(row=3, column=0)
    myLabel5.grid(row=4, column=0)
    myLabel6.grid(row=5, column=0)
    myLabel7.grid(row=7, column=0)
    myLabel8.grid(row=9, column=0)


#IMAGE NUMBER 2 FOR INFO WINDOW
    my_img2 = ImageTk.PhotoImage(Image.open("C:\\Users\\Chris\\OneDrive\\Desktop\\Intro to Software Development\\MO1 Prog Assignments\\C to F assignment\\apron.png"))
    myLabelImg2 = Label(infoWindow, image=my_img2, text="Man in Apron")
    myLabelImg2.grid(row=1, column=0)


#IMAGE
#IMAGE NUMBER 1, WITH ALTERNATE TEXT ADDED
my_img = ImageTk.PhotoImage(Image.open("C:\\Users\\Chris\\OneDrive\\Desktop\\Intro to Software Development\\MO1 Prog Assignments\\C to F assignment\\pinkcake.png"))
myLabelImg = Label(root, image=my_img, text="Pink Cupcake")
myLabelImg.grid(row=10, column=3)


#ENTRY WIDGET to get the user name on root page
e = Entry(root, width=30, borderwidth=5)
e.grid(row=5, column=3)


#DEFINING BUTTON COMMAND TO SAY A SPECIFIC HELLO
def hello():
    userGreeting = Label(root, text="Hello " + e.get() + "!", padx=25, pady=20, font="bold")
    userGreeting.grid(row=6, column=3)

#USER VALIDATION ON GREETING
def userVal():
    if e == "":
        command=hello
    

#BUTTONS  
#myButton1 = the button the user pushes after entering name
myButton1 = Button(root, text="Enter", padx=20, pady=15, command=hello)    
myButton1.grid(row=7, column=3)


#LABEL WIDGETS
#root page label creation
myLabel1 = Label(root, text="Welcome to Your Recipes!")
myLabel2 = Label(root, text="Enter your name to begin then click Enter")


#LABELS    
#main root page for the welcome window positioning
myLabel1.grid(row=2, column=3)
myLabel2.grid(row=4, column=3)


#BUTTON  ADD RECIPE BUTTON
addButton = Button(root, text="Add Recipe", padx=20, pady=15, command=addWindow)   
addButton.grid(row=11, column=3)

#BUTTON  VIEW RECIPE BUTTON
viewButton = Button(root, text="Did you Know?", padx=20, pady=15, command=dykWindow) 
viewButton.grid(row=13, column=3)

#BUTTON  BASIC COOKING INFO BUTTON
infoButton = Button(root, text="Cooking Basics", padx=20, pady=15, command=infoWindow)  
infoButton.grid(row=15, column=3)

#EXIT BUTTON
exit_button = Button(root, text="Exit Program", command=root.quit)
exit_button.grid(row=20, column=3)

#CLOSING THE ROOT LOOP
root.mainloop()
