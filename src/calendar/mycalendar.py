def in_range(y1, y2, range):
    return y1 <= y2 + range


# According to the Gregorian Calendar leap year rule
def is_leap_year(y):
    return (y%4 == 0 and y%100 != 0) or y%400 == 0


def is_centurial_year(y):
    return y%100 == 0


def is_cross_century_and_centurial_year_not_leap(y1, y2):
    def _next_centurial_year(y):
        return (y//100 + 1) * 100 if y%100 != 0 else y
    cy = _next_centurial_year(y1)
    return y1 < cy and y2 > cy and cy%400 != 0


# Return true if both years are leap years, or both are not leap years
def is_leap_same(y1, y2):
    return (is_leap_year(y1) and is_leap_year(y2)) or not (is_leap_year(y1) or is_leap_year(y2))


# Zeller congruence returns the day of week of a particular date
# q is the day of month, m is the month
# In zeller_congruence, 3 = March ... 12 = December ... 14 = February
# In zeller_congruence, y: m == 13 or m == 14 is counted as the previous year 
def zeller_congruence(y, q=1, m=13):
    def _to_ISO_week_day(h):
        return (h+5) % 7 + 1 # ISO day of week: 1 = Monday ... 7 = Sunday
    y = y-1 if m == 13 or m == 14 else y # Offset
    k = y%100 # year of the century
    j = y//100 # zero-based century
    h = (q + 13*(m+1)//5 + k + k//4 + j//4 - 2j) % 7 # Day of Week in the Greogorian Calendar: 0 = Saturday ... 6 = Friday
    return _to_ISO_week_day(h)
