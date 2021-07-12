from tkinter import *

# 변수 선언 부분

window = None

canvas = None

XSIZE, YSIZE = 256, 256

# 메인 코드 부분 

window =Tk()
canvas = Canvas(window, height = XSIZE, width = YSIZE)

paper = PhotoImage(width=XSIZE, height = YSIZE)
canvas.create_image((XSIZE/2,YSIZE/2),image=paper,state="normal")

canvas.pack()
window.mainloop()

for i in range(0,XSIZE):
    tmpList=[]
    for k in range(0,YSIZE):
        data=int(ord(fp.read(1)))
        tmpList.append(data)
    inImage.append(tmpList)

for i in range(0,XSIZE):
    for k in range(0,YSIZE):
        data = image[i][k]
        paper.put("#%02x%02x%02x" % (data, data, data),(k,i))

    
