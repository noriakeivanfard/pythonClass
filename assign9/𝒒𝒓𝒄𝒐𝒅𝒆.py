import qrcode
qr = qrcode.make("i'm nooria \n my email:noriak2009@gmail.com")

qr.save('qrcode.png',scale=10 , dark='darkgreen ', light='lightgreen', )
