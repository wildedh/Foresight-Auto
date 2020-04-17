import ocrmypdf


def ocr(file_path, save_path):
    ocrmypdf.ocr(file_path, save_path, rotate_pages=True,
    remove_background=True,language="en", deskew=True, force_ocr=True)

ocr()
