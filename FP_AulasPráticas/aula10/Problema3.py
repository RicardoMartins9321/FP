import os


def printDirFiles(d):
    lst = os.listdir(d)
    for fname in lst:
        path = os.path.join(d, fname)
        if os.path.isfile(path):
            ftype = "FILE"
        elif os.path.isdir(path):
            ftype = "DIR"
        else:
            ftype = "?"
        print(ftype, path)
    return


def findFiles(path, ext):
    dirlist = os.listdir(path)
    filelist = []
    filelist.extend([x for x in dirlist if x.endswith(ext)])
    for folder in [x for x in dirlist if os.path.isdir(os.path.join(path, x))]:
        filelist.extend(findFiles(os.path.join(path, folder), ext))
    return filelist


def main():
    print("Testing printDirFiles('..'):")
    printDirFiles("..")

    print("\nTesting findFiles('.', '.py'):")
    lst = findFiles(".", ".py")
    print(lst)
    assert isinstance(lst, list)

    print("\nTesting findFiles('..', '.csv'):")
    lst = findFiles("..", ".csv")
    print(lst)


if __name__ == "__main__":
    main()
