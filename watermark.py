# from __future__ import print_function
from wand.image import Image 
from wand.display import display
from wand.drawing import Drawing



with Image(filename = 'e:\\water\\images\\image5.jpg') as img:
	img.transform(resize='640x480>')

	with Image(filename='e:\\water\\nike_black.png') as img2:
		img2.transform(resize='50x50>')
		with img.clone() as demo:
			demo.watermark(img2, 0, 0,0)
			demo.save(filename="watermark.jpg")


