def telToName(tel, telList, nameList):
    name = 'Not found'
    for x in telList:
        if x == tel:
            name = nameList[telList.index(x)]
            break
    return name


def nameToTels(partName, telList, nameList):
    tels = []
    for i in nameList:
        if partName in i:
            tels.append(telList[nameList.index(i)])
    return tels


def main():
    # Lists of telephone numbers and names
    telList = ['975318642', '234000111', '777888333', '911911911']
    nameList = ['Angelina', 'Brad',      'Claudia',   'Bruna']

    # Test telToName:
    tel = input("Tel number? ")
    print(telToName(tel, telList, nameList))
    print(telToName('234000111', telList, nameList) == "Brad")
    print(telToName('222333444', telList, nameList) == "222333444")

    # Test nameToTels:
    name = input("Name? ")
    print(nameToTels(name, telList, nameList))
    print(nameToTels('Clau', telList, nameList) == ['777888333'])
    print(nameToTels('Br', telList, nameList) == ['234000111', '911911911'])


if __name__ == "__main__":
    main()
