import ocrmypdf

"""
def ocr(file_path, save_path):
    ocrmypdf.ocr(file_path, save_path, rotate_pages=True,
    remove_background=True,language="en", deskew=True, force_ocr=True)
"""

def ocr(input_pdf_or_image, output_pdf):
    ocrmypdf.ocr(input_pdf_or_image, output_pdf, rotate_pages=True,
    remove_background=True, language="en", deskew=True, force_ocr=True)

ocr("/Users/danielwilde/Desktop/BP1982_UK.pdf", "‎/Users/danielwilde/Desktop/BP1982_UK_searchable.pdf")
