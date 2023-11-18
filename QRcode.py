import qrcode
import os
folderpath = "\\Users\sammi\Documents\Application Team\Inventory Project\QRcode"

def create_qr_code(Name, Location,Category):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        data = f"Item: {Name}\nLocation: {Location}\nCategory :{Category}"
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img_name = f"{Name}_{Location}_{Category}_qr.png"
        file_path = os.path.join(folderpath,img_name)
        img.save(file_path)

def delete_qr_code(Name, Location, Category):
    img_name = f"{Name}_{Location}_{Category}_qr.png"
    file_path = os.path.join(folderpath,img_name)
    if os.path.exists(file_path):
        os.remove(file_path)