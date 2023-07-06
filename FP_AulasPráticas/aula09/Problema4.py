import bisect

lst = []
with open('wordlist.txt', 'r') as words:
    for line in words:
        lst.append(line.strip())


def countWords(lst, exp):
    lst2 = [x[:len(exp)] for x in lst]
    print(lst2)
    first = bisect.bisect_left(lst2, exp)
    last = bisect.bisect_right(lst2, exp)
    if first == last:
        return lst2[last][-1]
    return len(lst[first:last])


print(countWords(lst, 'ea'))
