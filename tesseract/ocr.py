import pytesseract
from PIL import Image
import os

def extract_text_from_image(file_path):
    """
    Extract text from an image using Tesseract OCR.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        # Open the image file
        image = Image.open(file_path)
    except Exception as e:
        raise ValueError("Invalid image file.")
    
    # Perform OCR using Tesseract
    extracted_text = pytesseract.image_to_string(image)
    
    return extracted_text

if __name__ == "__main__":
    sample_file_path = "C:/Users/nares/Documents/OCR/1.jpg" #replace your own image path
    result = extract_text_from_image(sample_file_path)
    print(result)