import os

script_dir = os.path.dirname(__file__)
rel_path = "seat_number.txt"
abs_file_path = os.path.join(script_dir, rel_path)


def get_seat_number():
    f = open(abs_file_path, "r")
    res = f.readline()
    f.close()
    
    return res

def set_seat_number(number):
    f = open(abs_file_path, "w")
    f.write(str(number))
    f.close()

def decrement_seat_number(number):
    res = get_seat_number()
    
    f = open(abs_file_path, "w")
    f.write(str(int(res) - number))
    f.close()
