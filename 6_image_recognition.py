import pyautogui
# file_menu = pyautogui.locateOnScreen("file_menu.png") # file_menu.png 화면을 인식하여 정보를 가져온다.
# print(file_menu) # file_menu.png 정보를 출력한다. box 크기 0,0,0 등 
# pyautogui.click(file_menu) # Png 파일에 해당하는 그림을 클릭한다. 

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen) 

# for i in pyautogui.locateAllOnScreen("checkbox.png"):
#     print(i)
#     pyautogui.click(i, duration=0.25)

# checkbox = pyautogui.locateOnScreen("checkbox.png")
# pyautogui.click(checkbox)

# 속도 개선
# 1. GrayScale
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
# pyautogui.moveTo(trash_icon)

# 2. 범위 지정 
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(1087, 634, 1428-1087, 656-634))
# pyautogui.moveTo(trash_icon)
# pyautogui.mouseInfo()
#1087,634 
#1428,656 

# 3. 정확도 조정
# run_btn = pyautogui.locateOnScreen("run_btn.png", confidence= 0.9) # 90% 이상 비슷한 이미지 인식
# pyautogui.moveTo(run_btn)

# 자동화 대상이 바로 보여지지 않는 경우 
# 1. 계속 기다리기
# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)
# else:
#     print("발견실패")
# while file_menu_notepad is None: 
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견 실패")

# pyautogui.click(file_menu_notepad)

# 2. 일정 시간동안 기다리기 (TimeOut)
import time
import sys

# timeout = 10 # 10초 대기
# start = time.time() # 시작 시간 설정
# file_menu_notepad = None
# while file_menu_notepad is None: 
#      file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#      end = time.time() # 종료 시간 설정 
#      if end - start > timeout : # 지정한 10초를 초과하면
#          print("시간 종료")
#          sys.exit()
def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout: 
            break
    return target

def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program")
        sys.exit()
# pyautogui.click(file_menu_notepad)

my_click("file_menu_notepad.png", 3)