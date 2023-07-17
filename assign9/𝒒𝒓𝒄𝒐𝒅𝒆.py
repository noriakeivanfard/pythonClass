import qrcode
qr = qrcode.make("noriak2009@gmail.com \n Hi🖐️ \n make me happy by sending an email.")

qr.save('qrcode.png',scale=10 , dark_dark='darkgreen ', light='lightgreen', )
