from PIL import Image,ImageEnhance,ImageFilter
import sys
im=Image.open('E:/python/test.jpeg');
im=im.filter(ImageFilter.MedianFilter())
enhancer=ImageEnhance.Contrast(im);
im=enhancer.enhance(2)
im=im.convert('1');
im.show()