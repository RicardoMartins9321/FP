# Transformar segundos em horas, minutos e segundos
seg = int(input('Quantos segundos se passaram? '))
min = seg // 60
restmin = min % 60
hor = min // 60
rest = seg % 60

print("{:02d}:{:02d}:{:02d}".format(hor, restmin, rest))
