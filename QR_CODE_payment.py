# Sonu Kumar UPI QR Code Generator Project
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import qrcode

def generate_qr():
    upi_id = upi_entry.get()
    amount = amount_entry.get()
    
    if not upi_id:
        messagebox.showerror("Error", "Please enter UPI ID")
        return
    
    # UPI QR Code format
    upi_url = f"upi://pay?pa={upi_id}&pn=Sonu Kumar&am={amount}&cu=INR"
    
    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(upi_url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    
    img.save("upi_qr.png")
    
    # Display QR code in GUI
    qr_img = Image.open("upi_qr.png")
    qr_img = qr_img.resize((250, 250))
    qr_photo = ImageTk.PhotoImage(qr_img)
    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo

# Tkinter GUI
root = tk.Tk()
root.title("Sonu Kumar UPI QR Generator")
root.geometry("400x450")

tk.Label(root, text="Enter UPI ID:").pack(pady=5)
upi_entry = tk.Entry(root, width=30)
upi_entry.insert(0, "sonukumar9303343@okhdfcbank")
upi_entry.pack(pady=5)

tk.Label(root, text="Enter Amount (optional):").pack(pady=5)
amount_entry = tk.Entry(root, width=30)
amount_entry.pack(pady=5)

tk.Button(root, text="Generate QR Code", command=generate_qr).pack(pady=10)

qr_label = tk.Label(root)
qr_label.pack(pady=10)

root.mainloop()
