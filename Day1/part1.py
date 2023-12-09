import pdb
with open(r"/Users/taylorhood/Documents/Projects/AdventOfCode2023/Day1/data.txt") as file:
    data = file.readlines()

def remove_line_break_char(data):
    data = [d[:-1] for d in data]
    return data

def get_first_and_last_number(data):
    numbers = '123456789'

    calibration_values = []

    for d in data:
        for char in d:
            if char in numbers:
                first = char
                break
                
        for char in reversed(d):
            if char in numbers:
                last = char
                break

        values = first + last
        
        calibration_values.append(int(values))
        
    print(f"calibration values **** {sum(calibration_values)}")
    return calibration_values


if __name__ == '__main__':
    clean_data = remove_line_break_char(data)
    calibration_values = get_first_and_last_number(clean_data)
