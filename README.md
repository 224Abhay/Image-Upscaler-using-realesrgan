# Image Upscaler using Real-ESRGAN

This project automates the process of upscaling images using Real-ESRGAN while cleaning filenames and organizing outputs into timestamped folders.

## 🚀 Features
- Automatically **removes spaces and parentheses** from filenames.
- **Detects GPU** being used (NVIDIA, Intel, or AMD).
- **Uses `tqdm` progress bar** for clean status updates.
- Creates a **new timestamped folder** for every upscale session.
- **Suppresses unnecessary console logs** from Real-ESRGAN.

## 📂 Folder Structure
```
/image_upscaler_project
│── main.py                   # Run this to start upscaling
│── image_upscaler.py          # Core processing logic
│── requirements.txt           # Dependencies list
│── inputs/                    # Place images here
│── outputs/
│   ├── 2025-03-24_14-30-15/   # Timestamped output folder
│   │   ├── image1.jpg
│   │   ├── image2.png
```

## 🔧 Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/224Abhay/Image-Upscaler-using-realesrgan.git
cd Image-Upscaler-using-realesrgan
```

### 2️⃣ Install Real-ESRGAN

Use the Ones i have provided.

OR

Download **Real-ESRGAN** from the official GitHub:
👉 [Real-ESRGAN Releases](https://github.com/xinntao/Real-ESRGAN/releases)

Ensure `realesrgan-ncnn-vulkan.exe` is placed in your system PATH or in the project directory.

### 3️⃣ Install Python Dependencies
```bash
pip install -r requirements.txt
```

## 🎯 How to Use
### 1️⃣ Add Images
Place your images inside the `inputs/` folder.

### 2️⃣ Run the Script
Run the following command:
```bash
python main.py
```

### 3️⃣ Output
- The script will detect your GPU and upscale images.
- Upscaled images will be saved in `outputs/YYYY-MM-DD_HH-MM-SS/`.
- A progress bar will show the upscaling process.

## 🛠 Troubleshooting
- If you see **"Real-ESRGAN not found!"**, make sure `realesrgan-ncnn-vulkan.exe` is installed and accessible.
- If `inputs/` is empty, the script will prompt you to add images before running.

## 📜 License
This project is open-source under the **MIT License**.

MIT License

Copyright (c) 2025 Abhay Shinde

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


Enjoy your upscaled images! 🚀✨

