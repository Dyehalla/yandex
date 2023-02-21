from PIL import Image, ImageDraw

im = Image.open("lesson-26-3.jpg")
pixels = im.load()

x, y = im.size

my_image = Image.new("RGB", (x, y), (0, 0, 0))
new_pixels = my_image.load()

for i_y in range(y):
    for i_x in range(x):
        new_pixels[i_x, i_y] = pixels[x - i_x - 1, i_y]

my_image.save('dammit.jpg')