#!/usr/bin/python
import Tkinter as tk

window = tk.Tk()  ## This will create a window object call window
text_box = tk.Entry(window)  ## This will add this text box to the above window
def SaveText():
	str1 = text_box.get()  ## To get the text from the entry text box
	with open("file1", 'w') as fx:
		fx.write(str1)
	text_box.delete(0, 'end')	## To delete the text from the text box
	
## Button have attributes , like text , width , command etc.
button1 = tk.Button(window, text = 'Save', command = SaveText)  ## To create a button widget
## In the order ,, so the pack method also decides the order in which widgets are placed on the window
text_box.pack()  ## Places our widget(text box) , to the window above
button1.pack()  ## Places our widget button , to the window above
window.mainloop()