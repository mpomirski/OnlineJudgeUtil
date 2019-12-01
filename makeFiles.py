import argparse, os, shutil

def showTests(t):
    num = t.count('::')
    tem = t.split('\n\n')
    t = []
    for i in tem:
        t.append(i.split('\n'))
    col_width = max(len(word) for row in t for word in row) + 2
    for idi, row in enumerate(t):
        print ("Test " + str(idi) + ": "+ "".join(word.ljust(col_width) for word in row))
    print("Total number of tests: " + str(num))

def createFiles(args):
    inputFile = args.filein
    cwd = os.getcwd()
    org_path = os.path.join(cwd, "output")
    if args.fileout == None:
        outputFileName = inputFile.split(".")[0]
    else:
        outputFileName = args.fileout
    if not os.path.exists(org_path):
        os.mkdir(org_path)
    
    with open(inputFile, "r") as mainFile:
        ins = []
        outs = []
        mainFile = mainFile.read()
        if args.show:
            showTests(mainFile)
        cpMain = mainFile
        mainFile = []
        for sub in cpMain.split('\n\n'):
            mainFile.append(sub.split('::')[0])
            mainFile.append(sub.split('::')[1])
        mainFile = [sub.split("\n") for sub in mainFile]
        mainFile = [(list(filter(None, sub))) for sub in mainFile]
        for i in range(0, len(mainFile)):
            if i % 2 == 0:
                ins.append(mainFile[i])
            else:
                outs.append(mainFile[i])

    for i, inputArg in enumerate(ins):
        filename = str(i+1) + ".in"
        with open(os.path.join(org_path, filename), "w+") as inFile:
            inFile.write("\n".join(inputArg))

    for i, outputArg in enumerate(outs):
        filename = str(i+1) + ".out"
        with open(os.path.join(org_path, filename), "w+") as outFile:
            outFile.write("\n".join(outputArg))

    shutil.make_archive(outputFileName, "zip", org_path)
    shutil.rmtree(org_path)
    
    print("Finished building " + outputFileName + ".zip")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filein", help="input file", metavar="<inputFile>")
    parser.add_argument("-o", "--fileout", help="output file", metavar="<outputFile>")
    parser.add_argument("-s", "--show", help="show test cases", action="store_true")
    arguments = parser.parse_args()

    createFiles(arguments)

if __name__ == "__main__":
    main()
