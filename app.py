import pdfplumber

def extract_text_from_pdf(pdf_path, txt_path):
    text = ""
    
    # PDFファイルを読み込む
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    
    # テキストファイルに保存
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)

# 使用例
pdf_path = r"put your PDF path in here"  # PDFファイルのパスを指定
txt_path = 'output.txt'   # 保存するテキストファイルのパスを指定
extract_text_from_pdf(pdf_path, txt_path)
