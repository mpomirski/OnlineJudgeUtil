import argparse, os, shutil

def createFiles(inputFile):
    cwd = os.getcwd()
    org_path = os.path.join(cwd, "output")
    outputFileName = inputFile.split(".")[0]
    if not os.path.exists(org_path):
        os.mkdir(org_path)
    
    with open(inputFile, "r") as mainFile:
        ins = []
        outs = []
        mainFile = mainFile.read()
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

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filein", help="input file", metavar="<inputFile>")
    arguments = parser.parse_args()

    createFiles(arguments.filein)

if __name__ == "__main__":
    main()
