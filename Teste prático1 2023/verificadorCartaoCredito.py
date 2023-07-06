def ccnumber(ccnumber): 

    totalOddDigits = 0
    totalEvenDigits = 0
    totalSoma = 0

    if " " in ccnumber:
        ccnumber = ccnumber.replace(" ","")
    elif "-" in ccnumber:
        ccnumber = ccnumber.replace("-","")

    ccnumber = ccnumber[::-1]

    for i in ccnumber[0::2]:
        i = int(i)
        if i*2 > 9:
             i = i*2 - 9
        else:
            i = i*2
        totalOddDigits += i
    print(totalOddDigits)

    for j in ccnumber[1::2]:
        j = int(j)
        totalEvenDigits += j

    totalSoma = totalOddDigits + totalEvenDigits
    if totalSoma % 10 == 0:
        return True
    else:
        return False
    


def main():
    ccnumber2 = input("Enter a credit card number: ")

    print(f"You have entered a {ccnumber(ccnumber2)} credit card number.")
    print(ccnumber("378282246310005"))
    print(ccnumber("371449635398431"))
    print(ccnumber("5610591081018250"))
    print(ccnumber("5555555555554444"))
    print(ccnumber("5105105105105100"))
    print(ccnumber("38520000023237"))

main()