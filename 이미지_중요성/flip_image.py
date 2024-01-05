


import cv2
import os
#오픈cv의 함수인 VideoCaputre 함수 사용
file_list=os.listdir('C:/dacon/230220/123_image/3_output_image') #동영상 파일이 들어가 있는 폴더 파일들 리스트
file_list.sort()

file_na = 'C:/dacon/230220/123_image/3_output_image/'

a,b,getnum=next(os.walk('C:/dacon/230220/123_image/3_output_image_flip'))
label_save = 'C:/dacon/230220/123_image/3_output_image_flip/'

count = len(getnum) #현재 존재하는 파일이름에 들어간 숫자 다음 숫자로 지정


for i in file_list:
    # 이미지 열기
    path=file_na+i
    im = cv2.imread(path)
    # dst = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

    # 이미지 resize
    im = cv2.flip(im, 1)
    # 이미지 JPG로 저장
    # im = im.convert('RGB')
    out= label_save + i
    cv2.imwrite(out, im)#새롭게 .jpg 파일로 저장
    count += 1
# print('end ::: ' + token)






