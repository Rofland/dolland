import os
import sys
from PIL import Image


if len(sys.argv) != 3:
    print('python3 {} ROOT_FOLDER HEIGHT'.format(sys.argv[0]))
    exit()

root = sys.argv[1]
height = int(sys.argv[2])



for product in os.listdir():
    productRoot = root + '/' + product
    originalRoot = productRoot + '/original'
    resizeRoot = "{}/h{}".format(productRoot, height)
    if not os.path.isdir(productRoot):
        continue
    if not os.path.exists(originalRoot):
        print('{} has no original image.'.format(product))
    if not os.path.exists(resizeRoot):
        os.mkdir(resizeRoot)
    imageNames = os.listdir(originalRoot)
    print('{} has {} images.'.format(product, len(imageNames)))
    for name in imageNames:
        img = Image.open(originalRoot + '/' + name)
        width = height * img.width // img.height
        result = img.resize((width, height))
        result.save(resizeRoot + '/' + name)


