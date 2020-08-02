import pyqrcode as qrcode


# http://www.iamfaheem.tk/

my_web = qrcode.create("http://www.iamfaheem.tk/")

my_web.png("myweb.png")