import os
import shutil

# Get the current repository (so that it can run in VS code run button)
workspace = __file__.replace('\\', '/').replace('/app.py', '')

INPUT_DIRECTORY = workspace + '/input/'
OUTPUT_DIRECTORY = workspace + '/output/'


# Empties the output directory
def reset_directory():
    try:
        shutil.rmtree(OUTPUT_DIRECTORY)
    except:
        pass
    os.mkdir(OUTPUT_DIRECTORY)
    return

# Convert the dir to text via pytesseract
def convert(dir, file = ""):
    import pytesseract
    from PIL import Image

    print("Starting conversion of " + file)
    print(dir)
    text = pytesseract.image_to_string(Image.open(dir), lang="chi_tra")
    f = open(OUTPUT_DIRECTORY + file.rsplit(".", maxsplit=1)[0] + '.txt', 'w',  encoding="utf-8")
    f.write(text)
    f.close()


# Loop through all the directories
def loop_directories():
    for subdir, dirs, files in os.walk(INPUT_DIRECTORY):
        for file in files:
            if '.png' in file or '.jpg' in file:
                convert(os.path.join(subdir, file), file)


# Main function
def main():
    reset_directory()
    loop_directories()



main()