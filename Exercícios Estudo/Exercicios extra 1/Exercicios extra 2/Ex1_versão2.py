import re

def valid_phone(phone):
    return bool(re.match(r'^\+?\d{3,}$', phone))

calls = []

while True:
    print("1) Register call")
    print("2) Read file")
    print("3) List customers")
    print("4) Fatura")
    print("5) Terminate")

    option = input("Choose an option: ")

    if option == '1':
        while True:
            src = input("Source number: ")
            if valid_phone(src):
                break
            print("Invalid number!")

        while True:
            dst = input("Destination number: ")
            if valid_phone(dst):
                break
            print("Invalid number!")

        dur = int(input("Duration in seconds: "))
        calls.append({'src': src, 'dst': dst, 'dur': dur})

    elif option == '2':
        filename = input("File name: ")
        with open(filename) as f:
            for line in f:
                src, dst, dur = line.split()
                calls.append({'src': src, 'dst': dst, 'dur': int(dur)})
    elif option == '3':
        customers = set(call['src'] for call in calls)
        for customer in sorted(customers):
            print(customer)

    elif option == '4':
        src = input("Enter source phone number: ")
        totalDur = sum([int(call['dur']) for call in calls if call['src'] == src])
        print(f'Total duration for {src} is {totalDur} seconds')

    elif option == '5':
        break
