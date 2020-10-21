from PIL import Image, ImageDraw

img = Image.new('RGBA', (100, 100), (255, 0, 0, 0))

draw = ImageDraw.Draw(img)

# null.png
# draw.ellipse((25, 25, 75, 75), fill=(0, 0, 0))
# draw.ellipse((28, 28, 72, 72), fill=(255, 255, 255,0))

# cross.png
draw.line((25, 25, 75, 75), fill=(0, 0, 0), width=3)
draw.line((25, 75, 75, 25), fill=(0, 0, 0), width=3)

img.save(fp='../files/cross.png', format='PNG')
