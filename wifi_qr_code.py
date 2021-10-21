import qrcode
from PIL import Image
import sys
import time


#read user input
SSID = input("enter Wifi SSID (Wifi name): ")
print("your SSID is :"+SSID)
print("----------------------")
pwd = input("enter wifi password (#muchsecure): ")
print("your password is :"+pwd)
print("----------------------")
print("choose security: WPA or WPA and maybe WPA... na it's WPA. We do not joke with security.")
time.sleep(1)
print("printing your QR code. I'm a good boy.")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)
qr.add_data('WIFI:S:'+SSID+';T:WPA;P:'+pwd+';;')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("wifi_"+SSID+".png")
print("done. share it, scan it, that's it. ")