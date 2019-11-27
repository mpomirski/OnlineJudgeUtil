import sys, getopt, os, shutil

def createFiles(inputFile):
    cwd = os.getcwd()
    org_path = os.path.join(cwd, "output")
    if not os.path.exists(org_path):
        os.mkdir(org_path)
    
    with open(inputFile, "r") as mainFile:
        ins = []
        outs = []
        mainFile = mainFile.read()
        mainFile = mainFile.split(" : ")
        mainFile = [sub.split(", ") for sub in mainFile]
        ins = mainFile[0]
        outs = mainFile[1]

    for i, inputArg in enumerate(ins):
        filename = str(i+1) + ".in"
        with open(os.path.join(org_path, filename), "w+") as inFile:
            inFile.write(inputArg)

    for i, outputArg in enumerate(outs):
        filename = str(i+1) + ".out"
        with open(os.path.join(org_path, filename), "w+") as outFile:
            outFile.write(outputArg)

    shutil.make_archive("output", "zip", org_path)
    shutil.rmtree(org_path)

def main(argv):
    inputFile = ""
    outputFile = ""
    try:
        opts, args = getopt.getopt(argv, "hi:", ["ifile="])
    except getopt.GetoptError:
        print("makeFiles.py -i <plik_wejsciowy>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("Zamienia plik wzorcowy na pliki .in, .out, spakowane do formatu .zip")
            print("Plik wzorcowy powinien być w formacie 'test1, test2, test3 : wynik1, wynik2, wynik3', zapisany jako .txt")
            print ("Sposób używa: makeFiles.py -i <plik_wejsciowy>")
            sys.exit(2)
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        createFiles(inputfile)

if __name__ == "__main__":
    main(sys.argv[1:])