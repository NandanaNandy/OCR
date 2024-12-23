import paddleocr

class PaddleOCR:
    def __init__(self, lang='en'):
        self.ocr = paddleocr.OCR(lang=lang)

    def process_image(self, image_path):
        results = self.ocr.ocr(image_path, cls=True)
        return results

    def extract_text(self, results):
        extracted_text = []
        for line in results:
            for word_info in line:
                extracted_text.append(word_info[1][0])
        return " ".join(extracted_text)

def main(image_path):
    ocr = PaddleOCR()
    results = ocr.process_image(image_path)
    text = ocr.extract_text(results)
    return text

if __name__ == "__main__":
    sample_image_path = "C:/Users/nares/Documents/OCR/1.jpg" #replace your own image path
    extracted_text = main(sample_image_path)
    print(extracted_text)