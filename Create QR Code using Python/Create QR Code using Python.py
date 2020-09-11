import pyqrcode

url='https://www.youtube.com/channel/UCK4cj4J9783c3X5n4iMcB0g?view_as=subscriber'
v=pyqrcode.create(url)
v.svg('Qr.svg',scale=10)
