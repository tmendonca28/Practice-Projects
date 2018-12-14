"""
Calculates number of seconds in 7 hours, 21 minutes and 37 seconds: To be passed in as time string HH:MM:SS
Coursera Python: Rice University
"""


def convert_to_seconds(time_string):
    h, m, s = time_string.split(':')
    return (int(h)*3600) + (int(m)*60) + int(s)


print(convert_to_seconds("07:21:37"))
