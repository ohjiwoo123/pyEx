from tkinter import *

# 함수 선언 부분
def loadImage(fname):
    global inImage, XSIZE, YSIZE
    fp = open(fname, 'rb')

    for i in range(0,XSIZE):
        tmpList=[]
        for k in range(0,YSIZE):
            data=int(ord(fp.read(1)))
            tmpList.append(data)
            inImage.append(tmpList)

        fp.close()


def displayImage(image):
    global XSIZE, YSIZE
    for i in range(0, XSIZE):
        for k in range(0,YSIZE):
            data=image[i][k]
            paper.put("#%02x%02x%02x" % (data, data, data), (k,i))

#전역 변수 선언 부분

window = None
canvas = None
XSIZE, YSIZE = 256, 256
inImage = []    # 2차원 리스트 메모리 

# 메인코드 부분 

window = Tk()
window.title("흑백 사진 보기")
canvas = Canvas(window, height = XSIZE, width = YSIZE)
paper = PhotoImage(width = XSIZE, height = YSIZE)

canvas.create_image((XSIZE / 2, YSIZE /2), image = paper, state ="normal")

# 파일 --> 메모리

filename = "C:\CookPython\RAW\tree.raw" # 파일명 지정
loadImage(filename) # loadImage 함수에 파일명 전달하여 해당 파일을 inImage 리스트에 불러들임

# 메모리 --> 화면

displayImage(inImage)   #displayimage 함수에 inImage 리스트를 전달해 윈도창에 출력

canvas.pack()
window.mainloop()