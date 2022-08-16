################################################################
# FILE : temperature.py
# WRITER : Omer Ferster , omerferster , 206893653
# EXERCISE : intro2cse ex2 2021
# DESCRIPTION: A simple program that checks if day's temperature
# is hotter than a specific min temp - boolean value returned
################################################################

MIN_REQUIREMENTS = 2  # minimum hotter days needed is 2


def is_it_summer_yet(min_temp, day1_temp, day2_temp, day3_temp):
    """ The function returns True if there is at least 2 or more hotter days
        during the week than min_temp, False otherwise.
        param min_temp: The minimum temperature
        param days1/2/3: three days temperature """
    hotter_days = 0  # index of hotter days - initial value as 0
    if min_temp < day1_temp:
        hotter_days += 1
    if min_temp < day2_temp:
        hotter_days += 1
    if min_temp < day3_temp:
        hotter_days += 1
    if hotter_days >= MIN_REQUIREMENTS:
        return True  # there are 2 or more hotter days
    else:
        return False  # there are less than 2 hotter days
