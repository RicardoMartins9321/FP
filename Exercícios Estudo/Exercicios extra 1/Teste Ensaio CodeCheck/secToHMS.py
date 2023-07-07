"""
Complete a função sec2hms de forma a converter um número de segundos sec
em h horas, m minutos e s segundos.
Por exemplo, sec2hms(3723) deve devolver o terno (1, 2, 3).
"""

def sec2hms(sec):
   # Calcule as horas, minutos e segundos e guarde em h, m e s.
   h = int(sec // 3600)
   seg_resto = int(sec%3600)
   m = seg_resto//60
   s = seg_resto%60

   return h, m, s   # devolve os valores
