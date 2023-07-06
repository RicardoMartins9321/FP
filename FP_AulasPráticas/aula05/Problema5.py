list = ['SCP', 'SLB', 'FCP']


def allMatches(list):
    matches = []
    for i in list:
        for x in list:
            if i != x:
                matches.append((i, x))
    return matches


print(allMatches(list))
