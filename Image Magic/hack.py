from PIL import Image

image = Image.open('out copy.jpg')
output = Image.new('RGB', (304, 92))
for i in range(304):
    part = image.crop((i * 92, 0, (i + 1) * 92, 1))
    part = part.transpose(Image.ROTATE_270)
    output.paste(part, (i, 0, i + 1, 92))
output.save('flag.jpg')