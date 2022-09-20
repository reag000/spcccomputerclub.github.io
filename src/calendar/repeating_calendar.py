import static_vars
from mycalendar import *


res = []
def years_repeating_calendar(y, range):
    # y1 is fixed, y2 is a variable
    def _years_repeating_calendar(y1, y2, range):
        if not in_range(y1, y2, range):
            return res
        if is_leap_year(y2):
            if is_cross_century_and_centurial_year_not_leap(y2, y2+12): y2 += 12
            elif is_cross_century_and_centurial_year_not_leap(y2, y2+28): y2 += 40
            else: y2 + 28
        elif is_leap_year(y2+1):
            if is_cross_century_and_centurial_year_not_leap(y2, y2+6): y2 += 6
            elif is_cross_century_and_centurial_year_not_leap(y2, y2+11): y2 += 12
            else: y2 += 11
        elif is_leap_year(y2+2):
            if is_centurial_year(y2+6): y2 += 6
            elif is_cross_century_and_centurial_year_not_leap(y2, y2+6): y2 += 12
            else: y2 += 11
        else:
            if is_cross_century_and_centurial_year_not_leap(y2, y2+6): y2 += 12
            else: y2 += 6
        if is_leap_same(y1, y2) and in_range(y1, y2, range):
            res.append(y2)
        _years_repeating_calendar(y1, y2, range)
    _years_repeating_calendar(y, y, range)
    return res


year = int(input('Enter a year: '))
years = years_repeating_calendar(year, 50)
for y in years: print(y)
