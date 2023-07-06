# Vês como tu consegues
s = input("Sexo(m/f): ")

while s != "m" and s != "f":
    print("Responda com m ou f")
    s = input("Sexo(m/f): ")
    
p = float(input("Peso(kg): "))
q = float(input("Alcool(g): "))
    
if s == "m":
    TA = q / (0.7 * p)
elif s =="f":
    TA = q / (0.6 * p)
    
print(f"TA: {TA:.2f} g/l")
