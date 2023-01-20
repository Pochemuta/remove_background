import os
from PIL import Image, ImageFile
from rembg import remove

ImageFile.LOAD_TRUNCATED_IMAGES = True

input = os.listdir('./input')


for file in input:
    input_path = './input/' + file  # raw file address
    output_path = './output/' + file  # result file address
    img = Image.open(input_path, 'r')  # open photo
    cover = Image.open('./cover.jpg', 'r')  # open cover

    ratio = img.size[0] / img.size[1]  # new ratio
    new_height = 1450
    new_width = int(new_height * ratio)  # new width

    resize_image = img.resize((new_width, new_height))  # change size

    transparent_image = remove(resize_image)  # remove background

    cover.paste(transparent_image,
                ((cover.width - transparent_image.width) // 2,
                 (cover.height - transparent_image.height)),
                mask=transparent_image)

    cover.save(output_path)
