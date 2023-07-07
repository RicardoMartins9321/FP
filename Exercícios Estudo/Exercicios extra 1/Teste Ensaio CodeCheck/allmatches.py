"""
Escreva uma função que, dada uma lista de equipas de futebol,
crie e devolva uma lista de todos os jogos que se podem fazer entre elas.
Cada jogo deve ser representado por um tuplo de duas equipas distintas.
Por exemplo:
   allMatches(["FCP", "SCP", "SLB"])  ->
      [('FCP', 'SCP'), ('FCP', 'SLB'), ('SCP', 'FCP'), ..., ('SLB', 'SCP')]
Com 3 equipas deve obter 6 jogos, com 4 equipas deve obter 12 jogos.
"""

def allMatches(teams):
    assert len(teams) >= 2, "Requires two or more teams!"
    x = []
    for i in range(0, len(teams)):
        for n in range(0, len(teams)):
            if teams[i] != teams[n] and x.count((teams[i], teams[n])) == 0:
                x.append((teams[i], teams[n]))
    return x
