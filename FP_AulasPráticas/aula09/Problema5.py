import bisect

lst = []
with open('wordlist.txt', 'r') as words:
    for line in words:
        lst.append(line.strip())


def suggestWords(lst, exp):
    lst2 = [x[:len(exp)] for x in lst]
    first = bisect.bisect_left(lst2, exp)
    last = bisect.bisect_right(lst2, exp)
    return [x[len(exp):] for x in lst[first:last]]


print('Suggestions for "Ab":')
print(suggestWords(lst, 'ea'))
