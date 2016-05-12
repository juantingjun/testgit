import Image,ImageEnhance,ImageFilter
import sys
image_name="./test.jpeg";
im=Image.open(image_name);
im=im.filter(ImageFilter.MedianFilter())
enhancer=ImageEnhance.Contrast(im);
im=enhancer.enhance(2)
im=im.convert('1');
im.show()