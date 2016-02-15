from PIL import Image
import glob, os

for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    width = im.size[0] / 2
    height = im.size[1] / 2
    size = width, height
    im.thumbnail(size, Image.ANTIALIAS)
    im.save('resized_'+file + ".jpg", "JPEG")