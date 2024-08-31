import PyPDF2

pdf_path = 'report2.pdf'  
try:
    with open(pdf_path, 'rb') as pdf_file_obj:
        pdf_file_reader = PyPDF2.PdfReader(pdf_file_obj)
        
        all_page = pdf_file_reader.pages[0]
        text = all_page.extract_text('\n')

    with open('extracted_text.txt', 'w') as text_file:
        text_file.write(text)

    print("Text has been successfully extracted to extracted_text.txt.")
except FileNotFoundError:
    print(f"Error: The file {pdf_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
