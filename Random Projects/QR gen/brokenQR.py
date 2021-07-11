import pyqrcode
import png

QRstring = "https://twitter.com/Fr0thgar" # paste any url here

url = pyqrcode.create(QRstring)
url.png('C:\Users\orcel\Google Drive\Zenva Projects\Python-Degree\Random Projects', scale = 8)