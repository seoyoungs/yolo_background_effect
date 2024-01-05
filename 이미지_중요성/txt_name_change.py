
import cv2
import os


# 주어진 디렉토리에 있는 항목들의 이름을 담고 있는 리스트를 반환합니다.
# 리스트는 임의의 순서대로 나열됩니다.
file_path = 'C:/dacon/230220/123_image/119_output_txt_flip'
file_names = os.listdir(file_path)
file_names

i = 1
for name in file_names:
    src = os.path.join(file_path, name)
    dst = file_path + '/flip2_'+name
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1
