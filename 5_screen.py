import pyautogui

# # 스크린 샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png") # 파일로 저장 

# pyautogui.mouseInfo()
# 220,95 NA_Pillow_unsupported NA_Pillow_unsupported

pixel = pyautogui.pixel(220,95) # 이 위치의 픽셀 rgb컬러 정보를 수집
print(pixel) # 위의 위치의 rgb 값을 출력 

# print(pyautogui.pixelMatchesColor(220,95 (60,60,60)))
print(pyautogui.pixelMatchesColor(220,95 pixel)) # rgb 값이 같으면 true 안 같으면 false 를 반환함.