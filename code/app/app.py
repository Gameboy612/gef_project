import os
import shutil

workspace = __file__.replace('\\', '/').replace('/app.py', '')

INPUT_DIRECTORY = workspace + '/input/'


def convert(dir, file):
    import pytesseract
    from PIL import Image

    print("Starting conversion of " + file)
    print(dir)
    text = pytesseract.image_to_string(Image.open(dir), lang="chi_tra")
    f = open(workspace + '/out.txt', 'w')
    f.write(text)
    f.close()

def loop_directories():
    for subdir, dirs, files in os.walk(INPUT_DIRECTORY):
        for file in files:
            if '.png' in file or '.jpg' in file:
                convert(os.path.join(subdir, file), file)


def main():
    loop_directories()



main()