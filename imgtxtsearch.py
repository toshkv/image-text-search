# Image text search script
from PIL import Image
import pytesseract as pt
import os
import re


def main():
    print("Image text search script!\r\n")
    # request image input path from user
    orig_path = input("Enter source image path:")

    # request text output path from user
    out_path = input("Enter text output path:")

    # iterate over each image in the directory
    for imagename in os.listdir(orig_path):
        input_path = os.path.join(orig_path, imagename)
        img = Image.open(input_path)

        # apply ocr using pytesseract
        text = pt.image_to_string(img, lang="eng")

        # remove .jpg extension
        #        image_path = image_path[0:-4]

        # "time_" is a reference to images using a datestamp as their filename
        fulltemppath = os.path.join(out_path, 'time_' + imagename + ".txt")

        # save the text for every image in a separate file
        write_file = open(fulltemppath, "w")
        write_file.write(text)
        write_file.close()


def grep(regex, dirpath):
    compiled_regex = re.compile(regex, re.DOTALL)
    matches = list()
    for filename in os.listdir(dirpath):
        full_filename = os.path.join(dirpath, filename)
        if not os.path.isfile(full_filename):
            continue
        with open(os.path.join(dirpath, filename)) as fh:
            content = fh.read()
            if compiled_regex.search(content):
                matches.append(full_filename)
    return matches


if __name__ == '__main__':
    main()
