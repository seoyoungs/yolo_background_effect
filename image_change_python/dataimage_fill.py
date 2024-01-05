import pygame
import os
import sys

# 초기화
pygame.init()

# 화면 설정
screen_size = (1280, 720)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Image Display")

# 이미지를 저장할 폴더와 파일 확장자
image_folder = "person"
output_folder = "test3_dark"
file_extension = ".jpg"

# 이미지 파일 목록 가져오기
image_files = [f for f in os.listdir(image_folder) if f.endswith(file_extension)]
if not image_files:
    print("No images found in the specified folder.")
    sys.exit()

# 이미지 파일 목록을 정렬
image_files.sort()

# 메인 루프
for image_file in image_files:
    # 이미지 불러오기
    image_path = os.path.join(image_folder, image_file)
    try:
        image = pygame.image.load(image_path)
    except pygame.error as e:
        print(f"Unable to load image '{image_file}': {e}")
        continue

    # 이미지 크기 변경 없이 화면에 표시
    image_rect = image.get_rect()
    image_rect.center = screen.get_rect().center

    # 화면에 이미지 표시
    screen.fill((0, 0, 0))  # screen.fill((255, 255, 255))  화면을 흰색으로 채웁니다.
    screen.blit(image, image_rect)

    pygame.display.flip()

    # 이미지 저장
    output_folder_path = os.path.join(os.getcwd(), output_folder)
    os.makedirs(output_folder_path, exist_ok=True)
    
    output_filename = f"{os.path.splitext(image_file)[0]}_output.png"
    output_path = os.path.join(output_folder_path, output_filename)
    pygame.image.save(screen, output_path)
    
    print(f"Image '{image_file}' saved as '{output_path}'")

    # 대기 시간 (예: 2초)
    pygame.time.delay(2000)
    
    
    
    