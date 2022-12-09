import pyperclip

def convert(lang_type):
    from PIL import ImageGrab
    image = ImageGrab.grabclipboard()
    image.save("test.png")

    import pytesseract
    pyperclip.copy(pytesseract.image_to_string(image, lang=lang_type))