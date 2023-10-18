import PyPDF2
import re


def write_list_to_file(file_path, data_list):
    try:
        with open(file_path, 'w') as file:
            for item in data_list:
                file.write(str(item) + '\n')
    except IOError:
        print("写入文件时发生错误。")

def split_questions(text):
    # 定义题目的正则表达式模式
    pattern = r'\d+ \(\w\).*?(?=\d+ \(\w\)|$)'
    
    # 使用re.findall函数找到所有匹配的题目
    questions = re.findall(pattern, text, flags=re.DOTALL)
    
    return questions




def extract_text_from_pdf(pdf_file):
    pdf_text = ""
    with open(pdf_file, "rb") as pdf:
        pdf_reader = PyPDF2.PdfReader(pdf)
        for page_num in range(len(pdf_reader.pages)):
            Page = pdf_reader.pages[page_num]
            pdf_text += Page.extract_text()
    return pdf_text


# Usage
pdf_file = "sample.pdf"
extracted_text = extract_text_from_pdf(pdf_file)
print("pdf文字提取成功")
text=extracted_text
questions = split_questions(text)
write_list_to_file("question.txt",questions)
print("问题提取中 50%/100%")
file="question.txt"
pattern = r'\d+\s+(9608|9618)(\/)\d+(\/)[A-Z](\/)[A-Z](\/)\d+( © UCLES )\d\d\d\d( \[Turn over|)'
with open(file, 'r') as f:
    content = f.read()
    result = re.sub(pattern, "", content)

with open(file,"w") as f:
    f.write(result)
print("问题提取完毕")



