"""
Considere que a1, b1 são os extremos de um intervalo real [a1, b1[
e que a2, b2 são os extremos de outro intervalo [a2, b2[.
Complete a função para verificar se os intervalos se itersectam.
Admita que a1 < b1 e a2 < b2.  (A função já verifica isso.)

Consider that a1, b1 are the endpoints of an interval of values [a1, b1[
and a2, b2 are the endpoints of another interval [a2, b2[.
Complete the function to check if the intervals intersect each other.
You may assume that a1 < b1 and a2 < b2.
"""

def intersects(a1, b1, a2, b2):
    # Estas instruções assert especificam e verificam o domínio da função.
    assert a1 < b1
    assert a2 < b2

    #for i in range(a1, b1+1):
      #return(a2 <= i <= b2)

    if a1<=a2 < b1 or a2<=a1 < b2:
      return True
    else:
      return False
