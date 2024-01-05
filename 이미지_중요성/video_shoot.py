import cv2
import os

# 한글인 경로는 잘 못 읽음
#오픈cv의 함수인 VideoCaputre 함수 사용
file_list=os.listdir('C:/Users/ka005/OneDrive/바탕 화면/서영/230217 쿠팡, 22L3, 23B1 테스트 블랙박스 영상/23B1/000000040_2018_01_28') #동영상 파일이 들어가 있는 폴더 파일들 리스트
file_list.sort()

file_na = 'C:/Users/ka005/OneDrive/바탕 화면/서영/230217 쿠팡, 22L3, 23B1 테스트 블랙박스 영상/23B1/000000040_2018_01_28/'

a,b,getnum=next(os.walk('C:/data/coupang/23B1/40'))

count = len(getnum) #현재 존재하는 파일이름에 들어간 숫자 다음 숫자로 지정

for i in file_list:

    path=file_na+i #폴더의 각 파일에 대한 경로
    vidcap=cv2.VideoCapture(path)

    ret=True
    while(ret):
        ret, image = vidcap.read()#return 값과 image를 읽어옴
        if(ret==False):
            break

        if(int(vidcap.get(1)) % 30 == 0):#50 frame당 한 frame만 저장
            print('Saved frame number: '+str(int(vidcap.get(1))))
            cv2.imwrite("C:/data/coupang/23B1/40/frame%d.jpg" % count, image)#새롭게 .jpg 파일로 저장
            print('Saved frame%d.jpg' % count)
            count += 1
    vidcap.release()

