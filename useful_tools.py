import random

feet_in_mile = 5280
meters_in_kilometer = 1000
beatles = ["John Lennon", "Paul McCartney", "Ringo Starr",
        "George Harrison", "Stuart Sutcliffe", "Pete Best",
        "Norman Chapman", "Jimmie Nicol", "Chas Newby", "Tommy Moore"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)














