from tkinter import filedialog
file = str(input('Enter file name: '))


def main():
    value = fileSum(file)
    print("Sum =", value)


def fileSum(filename):
    value = 0
    try:
        with open(file, 'r') as n:
            for line in n:
                value += float(line)
    except FileNotFoundError:
        print('File not found')
    return value


if __name__ == "__main__":
    main()
