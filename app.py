from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True


for file in input:
    input_path = './input/' + file  # raw file address
    output_path = './output/' + file  # result file address
    img = Image.open(input_path, 'r')  # open file
    cover = Image.open('./cover.jpg', 'r')  # open logo

    ratio = img.size[0] / img.size[1]  # new ratio
    new_height = 1450
    new_width = int(new_height * ratio)  # new width

    resize_image = img.resize((new_width, new_height))  # change size

    cover.paste(resize_image, ((cover.width - resize_image.width) // 2,
                (cover.height - resize_image.height)),
                mask=resize_image)

    cover.save(output_path)
