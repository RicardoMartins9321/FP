def bodyMassIndex(height, weight):
    bmi = float(weight/height**2)
    return bmi


def bmiCategory(bmi):
    assert bmi > 0
    if bmi < 18.5:
        category = 'Underweight'
    elif 18.5 <= bmi < 25:
        category = 'Normal weight'
    elif 25 <= bmi < 30:
        category = 'Overweight'
    else:
        category = 'Obesity'
    return category


def main():
    print("Índice de Massa Corporal")

    altura = float(input("Altura (m)? "))
    if altura < 0:
        print("ERRO: altura inválida!")
        exit(1)

    peso = float(input("Peso (kg)? "))
    if peso < 0:
        print("ERRO: peso inválido!")
        exit(1)

    imc = bodyMassIndex(height=altura, weight=peso)
    cat = bmiCategory(imc)

    print("BMI:", imc, "kg/m2")
    print("BMI category:", cat)


main()
