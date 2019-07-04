import os
import datetime


def CountLines():
    inputPath = r"C:\input.txt"
    outputFile = r"C:\Users\Michael\Desktop\output.txt"
    numOfLines = 0

    try:
        with open(inputPath, 'r') as input:
            for line in input:
                numOfLines += 1

            with open(outputFile, 'w') as output:
                output.write(str(numOfLines))
                output.write(os.linesep)
                output.write(os.path.basename(inputPath))
    except Exception as e:
        print("Exception:" + str(e))
    finally:
        input.close()
        output.close()


def Clean(path):
    list = os.listdir(path)
    for l in list:
        element = os.path.join(path, l)

        timeDiff = (datetime.datetime.now() - datetime.timedelta(days=365)
                    ) >= datetime.datetime.fromtimestamp(os.stat(element).st_mtime)

        sizeDiff = os.stat(element).st_size >= 1024**2

        if(os.path.isfile(element) and timeDiff and sizeDiff):
            print("Removing file: " + l)
            os.remove(element)
        elif os.path.isdir(element):
            print("Diving into:" + l)
            Clean(element)


def main():
   CountLines()
   folderPath = r"C:\Users\Michael\Desktop\Pytong"
   Clean(folderPath)


if __name__ == "__main__":
    main()
