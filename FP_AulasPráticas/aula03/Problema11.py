def sec2hms(sec):
    min = sec // 60
    m = min % 60
    h = min // 60
    s = sec % 60
    return h, m, s
