from tkinter import filedialog
file = str(input('Enter file name: '))


def main():
    value = fileSum(file)
    print("Sum:", value)


def fileSum(filename):
    value = 0
    with open(file, 'r') as n:
        for line in n:
            value += float(line)
    return value


if __name__ == "__main__":
    main()
