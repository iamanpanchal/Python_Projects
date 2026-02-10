import qrcode

#This is input from user.
url = input("Enter URL: ")

qr = qrcode.QRCode(
    version=3,
    box_size=10,
    border=4,
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

qr.add_data(url)
qr.make(fit=True)

#Convert url into QR.
img = qrcode.make(url)

path = r"D:\sem2\New folder\QR_Code\qrcode.png"

img = qr.make_image(
    fill_color="orange",
    back_color="white"
)

img.save(path)
# Shows success message
print("✅ Your QR code is generated!")
