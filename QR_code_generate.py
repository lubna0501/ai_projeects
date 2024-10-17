import qrcode
from PIL import Image
import os

data = "https://www.youtube.com/"
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill="black", back_color="white")
image_path = "qr_code.png"
image.save(image_path)

# Open the QR code image using the default image viewer
try:
    os.startfile(image_path)  # For Windows
except AttributeError:
    try:
        os.system("xdg-open " + image_path)  # For Linux
    except:
        try:
            os.system("open " + image_path)  # For macOS
        except:
            print("Could not open the image. Please open '{}' manually.".format(image_path))
