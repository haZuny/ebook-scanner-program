import tkinter
from tkinter import filedialog
import MouseAction
import ImageProcess

# Set entry text
def setEntry(entry, msg):
    entry.configure(state='normal')
    entry.delete(0,'end')
    entry.insert(0, msg)
    entry.configure(state='readonly')

# Create a new window
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
def btnSaveLoc():
    fileDir = filedialog.askdirectory()
    print("directory is selected: ", fileDir)
    setEntry(entSaveLoc, fileDir)
btnSaveLoc = tkinter.Button(windowMain, width=10, text = "Search", command=btnSaveLoc)
btnSaveLoc.grid(row=3, column=5)

# about run button
def btnRun():
    pageNumStr = entPageNum.get()
    capArea1Str = entGrabArea1.get()
    capArea2Str = entGrabArea2.get()
    nextPageStr = entNextPagePos.get()
    saveLocStr = entSaveLoc.get()
    #check is all items valid
    if pageNumStr == "" or not(pageNumStr.isdigit()):
        return
    if capArea1Str == "":
        return
    if capArea2Str == "":
        return
    if nextPageStr == "":
        return
    if saveLocStr == "":
        return
    pageNum = int(pageNumStr)
    capArea1 = (int(capArea1Str.split(", ")[0]), int(capArea1Str.split(", ")[1]))
    capArea2 = (int(capArea2Str.split(", ")[0]), int(capArea2Str.split(", ")[1]))
    nextPage = (int(nextPageStr.split(", ")[0]), int(nextPageStr.split(", ")[1]))

    for i in range(pageNum):
        ImageProcess.grabImg(capArea1[0], capArea1[1], capArea2[0], capArea2[1], saveLocStr, 'file'+str(i)+".png")
        MouseAction.mouseClick(nextPage[0], nextPage[1])


btnRun = tkinter.Button(windowMain, width=20, text = "Run", command=btnRun)
btnRun.grid(row=4, column=2, columnspan=2)


windowMain.mainloop()
