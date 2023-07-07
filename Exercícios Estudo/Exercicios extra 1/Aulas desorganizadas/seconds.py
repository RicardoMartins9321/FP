# Function that shows the amount of seconds in the given time
def hms2sec(h, m, s):
    sec_h = h * 3600
    sec_m = m * 60
    sec = sec_h + sec_m + s
    return sec


# Function that transforms the given seconds to the h m s layout
def sec2hms(sec):
    min = sec // 60
    m = min % 60
    h = min // 60
    s = sec % 60
    return h, m, s