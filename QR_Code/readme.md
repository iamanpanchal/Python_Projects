# 🎯 Custom QR Code Generator (Python)

A simple Python project that generates a **custom colored QR code** from any URL entered by the user and saves it as an image file. This project uses the `qrcode` library and demonstrates QR customization like size, border, and colors.

---

## 🚀 Features

* Take URL input from user
* Generate QR code image
* Custom QR settings (version, size, border)
* High error correction level
* Custom colors (orange on white)
* Save QR image to a chosen folder path

---

## 🧰 Requirements

Install required package:

```bash
pip install qrcode[pil]
```

---

## ▶️ How It Works

1. User enters a URL.
2. Program creates a QRCode object with custom settings.
3. URL data is added to the QR.
4. QR image is generated with custom colors.
5. Image is saved to the specified path.
6. Success message is printed.

---

## ⚙️ Customization Options

You can change:

* `version` → controls QR complexity
* `box_size` → size of QR blocks
* `border` → white margin around QR
* `fill_color` → QR color
* `back_color` → background color

Example:

```python
fill_color="blue"
back_color="black"
```

---

## 📁 Output

The QR code image will be saved as:

```
qrcode.png
```

inside your specified folder path.

---

## 🎓 Learning Outcomes

This project helps you practice:

* Using external Python libraries
* Taking user input
* Object configuration
* Image generation and saving
* File path handling (Windows raw paths)
* Basic customization features

---

## 📜 License

Free to use for learning and personal projects.
