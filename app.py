from flask import Flask, render_template, request, jsonify
import os
from PyPDF2 import PdfFileReader
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        pdf_file = request.files['pdfFile']
        if pdf_file and pdf_file.filename.endswith('.pdf'):
            # Convert PDF to Excel
            excel_data = convert_pdf_to_excel(pdf_file)
            
            # Save Excel file
            excel_file_path = 'output.xlsx'
            excel_data.to_excel(excel_file_path, index=False)

            return jsonify({'success': True, 'downloadLink': excel_file_path})
        else:
            return jsonify({'success': False, 'message': 'Invalid file format'})
    except Exception as e:
        print('Error:', e)
        return jsonify({'success': False, 'message': 'An error occurred during conversion'})

def convert_pdf_to_excel(pdf_file):
    pdf_reader = PdfFileReader(pdf_file)
    num_pages = pdf_reader.numPages

    data = {'Page': [], 'Text': []}

    for page_num in range(num_pages):
        page = pdf_reader.getPage(page_num)
        text = page.extract_text()
        data['Page'].append(page_num + 1)
        data['Text'].append(text)

    df = pd.DataFrame(data)
    return df

if __name__ == '__main__':
    app.run(debug=True)
