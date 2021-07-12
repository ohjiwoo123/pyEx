import pyautogui
# pyautogui.mouseInfo() # 화면 좌표를 보여주는 것이 뜬다. f1을 누르면 현재 좌표가 3초 후 복사된다.
# pyautogui.FAILSAFE = False # 중간에 움직여도 끊는 거 금지, 계속해서 움직임. 비추천 
# pyautogui.PAUSE =1 # 모든 동작에 1초씩 sleep 적용 
for i in range(10):
    pyautogui.move(100,100)
    pyautogui.sleep(1)