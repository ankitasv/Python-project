from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
root=Tk()
root.title("Wheather App")
root.geometry("900x500+300+200")
root.resizable(False,False)
#search box
Search_image=PhotoImage(file="Copy of search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

root.mainloop()
