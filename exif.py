import PIL.Image
import PIL.ExifTags
img = PIL.Image.open('img.jpg')

exif = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in img._getexif().items()
    if k in PIL.ExifTags.TAGS
}
print(exif)


'''from PIL import Image
from PIL import ExifTags

exifData = {}
img = Image.open('img.jpg')
exifDataRaw = img._getexif()
for tag, value in exifDataRaw.items():
    decodedTag = ExifTags.TAGS.get(tag, tag)
    exifData[decodedTag] = value
	print(exifData)'''