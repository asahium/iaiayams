import os
from PIL import Image
import random

def to_pixel_art(image, colors):
    size = (1280, 720)

    palette = colors[:]
    random.shuffle(palette)

    image = image.resize(size)
    pixels = image.load()
    new_image = Image.new("RGB", size)
    new_pixels = new_image.load()

    for x in range(size[0]):
        for y in range(size[1]):
            pixel = pixels[x, y]
            closest_color = min(palette, key=lambda c: sum((c[i] - pixel[i])**2 for i in range(3)))
            new_pixels[x, y] = closest_color

    return new_image

input_folder = "input_images/"
output_folder = "output_images/"
colors = [(255, 255, 255), (128, 128, 128), (0, 0, 0)]

# Создаем папку для выходных изображений, если её еще нет
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Получаем список всех файлов в папке с изображениями
image_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

# Обработка каждого изображения
for image_file in image_files:
    # Открываем изображение
    image_path = os.path.join(input_folder, image_file)
    image = Image.open(image_path)

    # Применяем функцию to_pixel_art
    new_image = to_pixel_art(image, colors)

    # Сохраняем изображение в выходную папку
    output_path = os.path.join(output_folder, os.path.splitext(image_file)[0] + "_pixel_art.png")
    new_image.save(output_path)

print("Все изображения обработаны.")
