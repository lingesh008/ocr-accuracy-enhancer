import pytesseract
import cv2
from PIL import Image
from difflib import SequenceMatcher
import os

# Set Tesseract path (Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# -------------------- Functions --------------------

def extract_text(image_path):
    """Extract text without preprocessing"""
    img = Image.open(image_path)
    return pytesseract.image_to_string(img)

def preprocess_image(image_path, output_path):
    """Apply grayscale and thresholding"""
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]
    cv2.imwrite(output_path, thresh)

def extract_text_preprocessed(preprocessed_path):
    """Extract text from preprocessed image"""
    img = Image.open(preprocessed_path)
    return pytesseract.image_to_string(img)

def get_accuracy(extracted_text, expected_text):
    return round(SequenceMatcher(None, extracted_text, expected_text).ratio() * 100, 2)

def save_output(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)

# -------------------- Main Execution --------------------

def run_ocr_pipeline(input_img, expected_text):
    print(f"\nProcessing image: {input_img}")

    # Step 1: Raw OCR
    raw_text = extract_text(input_img)
    save_output(raw_text, 'output/ocr_result.txt')

    # Step 2: Preprocessing
    preprocessed_img = 'output/preprocessed.png'
    preprocess_image(input_img, preprocessed_img)

    # Step 3: OCR on preprocessed image
    clean_text = extract_text_preprocessed(preprocessed_img)
    save_output(clean_text, 'output/ocr_preprocessed_result.txt')

    # Step 4: Accuracy comparison
    acc_raw = get_accuracy(raw_text, expected_text)
    acc_clean = get_accuracy(clean_text, expected_text)

    print("\n--- OCR Accuracy Report ---")
    print(f"Original Image Accuracy     : {acc_raw} %")
    print(f"Preprocessed Image Accuracy : {acc_clean} %")

# Run the pipeline
if __name__ == "__main__":
    input_image = 'input/sample_image.jpg'
    expected_output = "This is a sample document for OCR testing"
    run_ocr_pipeline(input_image, expected_output)
