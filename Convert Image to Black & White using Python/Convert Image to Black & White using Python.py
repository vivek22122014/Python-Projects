from PIL import Image

c=Image.open('CI.JPG')
b=c.convert('L')
b.save('Bandw.jpg')
c.show()
b.show()
