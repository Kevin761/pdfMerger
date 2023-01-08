import PyPDF2
import sys
import os

merger = PyPDF2.PdfMerger()

input_dir = './input'

for file in os.listdir(input_dir):
    if file.endswith(".pdf"):
        file_path = os.path.join(input_dir, file)
        try:
            with open(file_path, 'rb') as f:
                merger.append(f)
        except Exception as e:
            print(f'Error occurred while reading {file}: {e}')
            sys.exit(1)

try:
    with open('FinalPDF.pdf', 'wb') as f:
        merger.write(f)
except Exception as e:
    print(f'Error occurred while writing FinalPDF.pdf: {e}')
    sys.exit(1)
