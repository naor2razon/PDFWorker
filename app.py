from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter,PdfFileMerger
import csv
"""ISSUE 0"""
"""DEFINE PDF LOCATION - IN FUTURE - NEED TO IMPORT ONE"""
pdf_path = (
    Path.home()
    / "Pride_and_Prejudice.pdf"
)

"""CREATE A NEW PDF FILE WITH SPECIFIC PAGES FROM OTHER FILE"""
input_pdf = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

"""ISSUE 1"""
for n in range(1, 4):
    page = input_pdf.getPage(n)
    pdf_writer.addPage(page)

"""open output_file_path in write mode and assign the file object returned by .open() to the variable output_file"""
with Path("first_page.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)


"""GET THE NUMBER OF PAGES IN PDF"""
pdf = PdfFileReader(str(pdf_path))
print("Number of pages in file: ", pdf.getNumPages())

"""GET THE META DATA OF A PDF"""
print("Meta Data : " , pdf.documentInfo)


"""EXTRACT FIRST PAGE DATA AS A STRING"""
first_page = pdf.getPage(0)
first_page.extractText()

"""EXTRACT ALL PAGES DATA AS A STRING"""
for page in pdf.pages:
    print(page.extractText())





def delete_row_from_csv(user_id):
    lines = list()
    members = user_id
    with open('mycsv.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == members:
                    lines.remove(row)
    with open('mycsv.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)







"""ISSUES TO SOLVE:
        ISSUE 0 - NEED ADD IMPORT FUNC FOR PDF FILES
        ISSUE 1 - NEED TO MAKE THE RANG DYNAMIC
        
"""
