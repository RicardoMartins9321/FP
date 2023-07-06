import os


def tamanho(folder_dir="./"):
    print("{:50}{:3}".format("File", "Size"))
    for f in os.listdir(folder_dir):
        print("{:50}{:3}".format(f, os.stat(f).st_size))


tamanho()
