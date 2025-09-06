import qrcode
from colorama import Fore, Style
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Data to encode
clear()
def QR_code():
    website = input(Fore.CYAN+"Enter the the name of the website (Example: Facebook): "+Style.RESET_ALL).strip()
    data = f"https://www.{website}.com"
    
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image
    img.save(f"{website}QRcode.png")
    
    
    print(Fore.LIGHTGREEN_EX+"QR code generated and saved as qrcode.png"+Style.RESET_ALL)

if __name__ == "__main__":
    QR_code()
