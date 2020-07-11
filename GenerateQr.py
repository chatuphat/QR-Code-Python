import pyqrcode
link="https://github.com/chatuphat"
image=pyqrcode.create(link)
image.svg("page.svg",scale=8)