import PyPDF2
import cv2

def extract_images_from_pdf(pdf_file):
    images = []
    try:
        with open(pdf_file, "rb") as pdf:
            pdf_reader = PyPDF2.PdfReader(pdf)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                xObject = page['/Resources'][/XObject].getObject()
                for obj in xObject:
                    if isinstance(xObject[obj], dict) and xObject[obj]['/Subtype'] == '/Image':
                        images.append(xObject[obj])
    except FileNotFoundError:
        print("文件不存在或无法打开。")
    return images




# Usage
pdf_file = "sample.pdf"
extracted_images = extract_images_from_pdf(pdf_file)
# 读取图像
image = cv2.imread('image.jpg')

# 显示图像
cv2.imshow('Image', image)