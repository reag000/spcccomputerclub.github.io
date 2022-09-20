---
title: "Repeating Calendars"
date: 2022-09-17T20:38:49+08:00
draft: false
---

{{< katex >}}

# Repeating Calendars

## Gregorian Calendar

The **Gregorian Calendar** is principled to space **leap years** differently to approximate the actual **tropical year**. The mean tropical year, determined by the period of the Earth's revolution around the Sun, is approximately 365.2422 days <a href='https://asa.hmnao.com/SecM/Glossary.html#_Y'>[1]</a>, which is not a whole number. As a consequence, with the usual Julian Calendar's leap year rule, a leap year following every three normal years, every 100 years, the Julian Calendar is "one day more" and every 400 years, it is "three days more". Let \\(n\\) be the number of years, \\(a_n\\) the actual number of days in \\(n\\) tropical years, and \\(j_n\\) the number of days in \\(n\\) years in Julian Calendar, and \\(d_n\\) the difference in number of days between \\(a_n\\) and \\(j_n\\). Then:

$$
d_{100} = j_{100} - a_{100} = (365 \times 100 + 25) - 365.2422 \times 100 = (365 - 365.2422) \times 100 + 25 = 0.78 \approx 1
$$

$$
d_{400} = j_{400} - a_{400} = (365 - 365.2422) \times 400 + 100 = 3.12 \approx 3
$$

To offset the difference, the Gregorian Calendar has a special leap year rule:

> Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400. For example, the years 1700, 1800, 1900 are not leap years, but the year 2000 is. <a href='https://en.wikipedia.org/wiki/Gregorian_calendar'>[2]</a>

Let \\(g_n\\) be the number of days in Gregorian Calendar, then by a simple calculation:

$$
d_{100} = g_{100} - a_{100} = (365 - 365.2422) \times 100 + 24 = -0.22 \approx 0
$$

$$
d_{400} = g_{400} - a_{400} = (365 - 365.2422) \times 400 + 97 = 0.12 \approx 0
$$

we know that the Gregorian Calendar is more accurate than the Julian Calendar.

## Repeating Calendars in the Julian Calendar

Julian Calendars repeat regularly. Let \\(y\\) be a year in the Julian Calendar. If \\(y \equiv 0\pmod{4}\\), then \\(y + 28\\) is the next year with repeating calendar; if \\(y \equiv 1,\ 2 \pmod{4}\\), then \\(y+11\\) is the next year; else \\(y \equiv 3 \pmod{4}\\), and the next year is \\(y+6\\). A function \\(r\\) that gives the next year such that is has the same calendar with year \\(y\\) will be so:

$$
r(y) = y + 28,\ y \equiv 0 \pmod{4};
$$
$$
r(y) = y + 11,\ y \equiv 1,\ 2 \pmod{4};
$$
$$
r(y) = y + 6,\ y \equiv 3 \pmod{4}
$$

Proofs are shown below:

For two calendars of different years to be the same, they must start with the same day of week on 1th Jan, and either both years are leap years or both are not. Let \\(h_y\\) be the day of week on 1th Jan a particular year \\(y\\) starts with. Two years \\(i\\) and \\(j\\) having the same calendar implies that \\(h_i = h_j\\). Given \\(h_y\\), a \\(h_{y + k}\\) is given by \\((h_y + p) \pmod{7}\\), where \\(p\\) is the shift in day of week in \\(k\\) years. For example, suppose \\(h_y = 1\\) and \\(y\\) is a leap year, then \\(h_{y + 3} = (1 + 4) \pmod{7} = 5\\), and \\(h_{y+5} = (1 + 7) \pmod{7} = 1\\), and thus \\(h_{y+5} = h_y\\).

Suppose \\(y \equiv 0 \pmod{4}\\). Let \\(k\\) be the smallest positive integer such that years \\(y\\) and \\(y + k\\) have the same calendar. We prove that it is \\(k = 28\\) in this case. The condition implies that \\(y + k \equiv 0 \pmod{4}\\) and \\(h_y = h_{y+k} = (h_y + p) \pmod{7}\\). For \\(k = 28\\), \\(y + 28 \equiv 0 \pmod{4}\\) and \\(h_y = h_{y + 28} = (h_y + 35) \pmod{7}\\). Therefore, years \\(y\\) and \\(y + 28\\) have the same calendar. Then we prove that \\(28\\) is the smallest \\(k\\) for which this is true. It is trivial that for every \\(k < 28\\) such that \\(k \equiv 0 \pmod{4}\\), \\(h_y \neq (h_y + p) \pmod{7}\\) for the corresponding \\(p\\). The calculation is left to the readers.

Suppose \\(y \equiv 1, 2 \pmod{4}\\) and let \\(k = 11\\) this time. In both cases, \\(y + 11 \not \equiv 0 \pmod{7}\\) and \\(h_y = h_{y+11} = (h_y + 14) \pmod{7}\\). For \\(y \equiv 3 \pmod{4}\\), a similar proof follows. \\(\blacksquare\\)


## Repeating Calendars in the Gregorian Calendar

Gregorian Calendars repeat rather complicatedly compared to Julian Calendars. In the previous calculation, we use the fact that given any starting known \\(y\\), especially \\(y \pmod{4}\\), not necessarily the \\(h_y\\), we can calculate \\(p\\) after \\(k\\) years by adding the number of leap years in between to \\(k\\). Then we base our function on this fact. However in the case of Gregorian Calendar, the leap year rule is not simple, thus the math is not simple as well. We have to pay attention to it whenever \\(y + k\\) is cross the century and the centurial year is not a leap year.

I shall leave here the algorithm of finding the next repeating calendar in the Gregorian Calendar for a particular year, as these are easy to varify:

```python
# python
if is_leap_year(y):
    if is_cross_century_and_centurial_year_not_leap(y, y+12): y += 12
    elif is_cross_century_and_centurial_year_not_leap(y, y+28): y += 40
    else: y + 28
elif is_leap_year(y+1):
    if is_cross_century_and_centurial_year_not_leap(y, y+6): y += 6
    elif is_cross_century_and_centurial_year_not_leap(y, y+11): y += 12
    else: y += 11
elif is_leap_year(y+2):
    if is_centurial_year(y+6): y += 6
    elif is_cross_century_and_centurial_year_not_leap(y, y+6): y += 12
    else: y += 11
elif is_cross_century_and_centurial_year_not_leap(y, y+6): y += 12
else: y += 6
```

### Generating the Repeating Calendars

Here we generate the repeating calendars in the next 50 years for you:

## Brain Teasers on Calendar Calculation

Problem 1: Suppose there are:

1. 6 days in a week
2. 3 weeks in a month
3. 11 months in a year
4. Jan, Mar, May, July, Aug, Oct have 20 days in a month
5. Apr, Jun, Sep, Nov have 19 days in a month
6. Feb has 18 days in a month
7. Feb has 17 days if \\(y \equiv 0 \pmod{3}\\) and \\(y \not \equiv 0 \pmod{99}\\), or \\(y \equiv 0 \pmod{297}\\)

Given that 16th Sep 2022 is a Friday, what is the next repeating calendar for 2022?
