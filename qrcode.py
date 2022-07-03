import pyqrcode
 
def qr_code():
    s='This is Power python class'
    d=pyqrcode.create(s)
    d.png('')
