# 파일 기본 
import os
# print(os.getcwd()) # current working directory 현재 작업공간
# os.chdir("rpa_basic") #rpa_basic 으로 작업 공간 이동 
# print(os.getcwd())
# os.chdir("..") # 부모 폴더로 이동
# print(os.getcwd())
# os.chdir("../..") # 조부모 폴더로 이동
# print(os.getcwd())
# os.chdir("c:/") # 주어진 절대 경로로 이동 (윈도우의 경우)
# print(os.getcwd())

# 파일 경로
# print(os.path.join(os.getcwd(), "dd.xlsx")) # 절대 경로 생성
# print(dd.xlsx)

# 파일 경로에서 폴더 정보 가져오기 
# print(os.path.dirname(r"/Users/jwoh/Desktop/python/dd.xlsx"))

# 파일 정보 가져오기 
import time
import datetime

# 파일의 생성 날짜
ctime = os.path.getctime("run_btn.png")
print(ctime)
# 날짜 정보를 strftime 을 통해서 연월일 시분초 형태로 출력
print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# 파일의 수정 날짜
mtime = os.path.getmtime("run_btn.png")
print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

# 파일의 마지막 접근 날짜 
atime = os.path.getatime("run_btn.png")
print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

# 파일 크기 
size = os.path.getsize("run_btn.png")
print(size) # 바이트 단위로 파일크기 출력 