inputFileOK = False
while (inputFileOK == False):
    try:
        inputFileName = input("Enter name of input file: ")
        inputFile = open(inputFileName, "r")
    except IOError:
        print("File", inputFileName, "could not be opened")
    else:
        print("Opening file", inputFileName, " for reading.")
        inputFileOK = True

        for line in inputFile:
            print(line)
        print("Completed reading of file", inputFileName)
        inputFile.close()
        print("Closed file", inputFileName)
    finally:
        if (inputFileOK == True):
            print("Successfully read information from file", inputFileName)
        else:
            print("Unsuccessfully attempted to read information from file", inputFileName)