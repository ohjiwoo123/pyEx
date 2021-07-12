import pyautogui
w = pyautogui.getWindowsWithTitle("제목 없음")[0] # 메모장 1개 뛰운 상태에서 가져옴. 
w.activate() 

# pyautogui.write("1234") # 윈도우 기준 메모장 띄우고 1234 적음.
# pyautogui.write("NadoCoding", interval=0.25) # 0.25 인터벌 가지고 나도코딩 입력.
# pyautogui.write("t","e","s","t","left","left","right","l","a","enter"], interval=0.25)
# t e s t 순서대로 적고 왼쪽 방향키 2번, 오른쪽 방향키 2번, 1 a 순서대로 적고 enter 입력

# 특수 문자 
# shift 4 -> $ 
# pyautogui.keyDown("shift") # keydown 키보드를 누른다
# pyautogui.press("4") # 숫자 4를 입력하고
# pyautogui.keyup("shift") # shift 키를 뗀다 

# 조합키 (Hot Key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a") # press("a")
# pyautogui.keyUp("ctrl") # Ctrl + A 

# 간편한 조합키 
# pyautogui.hotkey("ctrl", "alt", "shift", "a")
# Ctrl 누르고 > Alt 누르고 > Shift 누르고 > A 누르고 > A 떼고 > Shift 떼고 > Alt 떼고 > Ctrl 뗀다.
# pyautogui.hotkey("ctrl, "a")p

import pyperclip
# pyperclip.copy("나도코딩") # "나도코딩" 글자를 클립보드에 저장
# pyautogui.hotkey("ctrl","v") # 클립보드에 있는 내용을 붙여넣기 

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")

my_write("나도코딩")

# 자동화 프로그램 종료 
# win : ctrl + alt + del 
# mac : cmd + shift + option + q 