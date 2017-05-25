#!/usr/bin/python

import sys
from os import listdir
import Tkinter as tk
from Tkinter import *
from PIL import Image as PImage, ImageTk
from random import shuffle

root = tk.Tk()
root.title('Image Pair')

#return a created list of image names
def ImagesList(path):
    imagesList = listdir(path)
    mylist = []
    for image in imagesList:
        mylist.append(image)
    shuffle(mylist)
    return mylist

#find paired Answer image and show (as button)
def update(myimg, mywidth, myheight, updatedindex):
    qstring = '-Q.png'
    astring = '-A.png'
    answerimg = myimg.replace(qstring, '')+astring
    ansimg = ImageTk.PhotoImage(PImage.open(answerimg))

    myclick.config(image=ansimg, command=lambda: newpair(updatedindex, imgs), width=mywidth, height=myheight)
    myclick.image = ansimg

#find the next Question image in the list and show (as button)
def newpair(myindex, mylist):
    newindex = myindex+1
    if newindex == len(mylist)-1:
        root.destroy()
        return

    newimgname = mylist[newindex]
    newimageFile = path+newimgname

    for item in mylist:
        if 'A' in newimgname:
            newindex += 1
            if newindex == len(mylist) - 1 :
                root.destroy()
                return
            newimgname = mylist[newindex]
            newimageFile = path+newimgname

        if 'Q' in newimgname:
            newimage = ImageTk.PhotoImage(PImage.open(newimageFile))

            w = newimage.width()
            h = newimage.height()

            myclick.config(image=newimage, command=lambda: update(newimageFile, w, h, newindex), width=w, height=h)
            myclick.image = newimage

            break

path = "/Users/ekdlsjubilee/Documents/CS/ImagePair/ImageFolder/"

imgs = ImagesList(path) #call list of image names
index = 0
imgname = imgs[index]
imageFile = path+imgname #location of the image file

#go through list until first Question image is found
for img in imgs:
    if 'A' in imgname:
        index += 1
        imgname = imgs[index]
        imageFile = path+imgname

if 'Q' in imgname:
    image1 = ImageTk.PhotoImage(PImage.open(imageFile))

    w = image1.width()
    h = image1.height()
    x = 0
    y = 0

    #show Question image as button when found
    #if clicked, find paired Answer image and show using update function
    myclick = Button(root, command=lambda: update(imageFile, w, h, index), height=h, width=w)
    myclick.config(image=image1, width=w, height=h)  #this creates a button as the image
    myclick.pack()

root.mainloop()