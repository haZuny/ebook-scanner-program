import tkinter
import MouseAction

# Set entry text
def setEntry(entry, msg):
    entry.configure(state='normal')
    entry.delete(0,'end')
    entry.insert(0, msg)
    entry.configure(state='readonly')

windowMain = tkinter.Tk()

windowMain.title("ebook")
# windowMain.geometry("600x400")  # window size and position
windowMain.resizable(False, False)

# about page number
lbPageNum = tkinter.Label(windowMain, text = "page number: ")
lbPageNum.grid(row=0, column=0)
entPageNum = tkinter.Entry(windowMain, width=10)
entPageNum.grid(row=0, column=1)

# about grab area1
lbGrabArea1 = tkinter.Label(windowMain, text = "Capture area1: ")
lbGrabArea1.grid(row=1, column=0)
entGrabArea1 = tkinter.Entry(windowMain, width=10, state="readonly")
entGrabArea1.grid(row=1, column=1)
# button event
def btnGrabArea1Clicked():
    locX, locY = MouseAction.returnMousePos()
    setEntry(entGrabArea1,str(locX) + ", " + str(locY))
btnGrabArea1 = tkinter.Button(windowMain, width=10, text = "Set", command=btnGrabArea1Clicked)
btnGrabArea1.grid(row=1, column=2)

# about grab area2
lbGrabArea2 = tkinter.Label(windowMain, text = "Capture area2: ")
lbGrabArea2.grid(row=1, column=3)
entGrabArea2 = tkinter.Entry(windowMain, width=10, state="readonly")
entGrabArea2.grid(row=1, column=4)
def btnGrabArea2Clicked():
    locX, locY = MouseAction.returnMousePos()
    setEntry(entGrabArea2,str(locX) + ", " + str(locY))
btnGrabArea2 = tkinter.Button(windowMain, width=10, text = "Set", command=btnGrabArea2Clicked)
btnGrabArea2.grid(row=1, column=5)

# about next page key
lbNextPagePos = tkinter.Label(windowMain, text = "Next page key: ")
lbNextPagePos.grid(row=2, column=0)
entNextPagePos = tkinter.Entry(windowMain, width=10, state="readonly")
entNextPagePos.grid(row=2, column=1)
def btnNextPagePosClicked():
    locX, locY = MouseAction.returnMousePos()
    setEntry(entNextPagePos,str(locX) + ", " + str(locY))
btnNextPagePos = tkinter.Button(windowMain, width=10, text = "Set", command=btnNextPagePosClicked)
btnNextPagePos.grid(row=2, column=2)

#about save location
lbSaveLoc = tkinter.Label(windowMain, text = "Save location: ")
lbSaveLoc.grid(row=3, column=0)
entSaveLoc = tkinter.Entry(windowMain, width=50, state="readonly")
entSaveLoc.grid(row=3, column=1, columnspan=4)
btnSaveLoc = tkinter.Button(windowMain, width=10, text = "Set")
btnSaveLoc.grid(row=3, column=5)

# about run button
btnRun = tkinter.Button(windowMain, width=20, text = "Run")
btnRun.grid(row=4, column=2, columnspan=2)


windowMain.mainloop()
