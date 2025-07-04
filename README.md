# ocr-accuracy-enhancer
A Python OCR pipeline using Tesseract and OpenCV to improve text extraction accuracy
🧠 OCR Accuracy Enhancer

This project helps improve the accuracy of OCR (Optical Character Recognition) by using image preprocessing techniques before extracting text from images.

📌 What It Does

- Takes an image with text (like scanned documents or photos)
- Extracts text using Tesseract OCR
- Applies grayscale and thresholding to clean the image
- Compares text accuracy **before and after** preprocessing
- Shows which version gives better results

🧰 Tools & Technologies Used

- Python 🐍
- Tesseract OCR 🔍
- OpenCV (for image processing)
- Pillow (for handling images)
- difflib (to compare text similarity)

## 🛠 How to Use

1. Install the Required Libraries
pip install pytesseract opencv-python pillow
2. Install Tesseract OCR engine:
- Windows: [Tesseract Installer](https://github.com/UB-Mannheim/tesseract/wiki)
3. Clone the repo and navigate to the folder:
python main.py

## Sample Output
--- OCR Accuracy Report ---
Original Image Accuracy     : 64.22 %
Preprocessed Image Accuracy : 89.46 %
