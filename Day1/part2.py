import part1 
with open(r"/Users/taylorhood/Documents/Projects/AdventOfCode2023/Day1/data.txt") as file:
    data = file.readlines()

def words_into_numbers(data):
    numbers = {
        'one' : '1',
        'eno' : '1',
        'two' : '2',
        'owt' : '2', 
        'three' : '3',
        "eerht" : '3',
        'four' : '4',
        'ruof' : '4',
        'five' : '5',
        'evif' : '5',
        'six' : '6',
        'xis' : '6',
        'seven' : '7',
        'neves' : '7',
        'eight' : '8',
        'thgie' : '8',
        'nine' : '9',
        'enin' : '9'
    }

    calibration_values = []
    for d in data:
        print(d)
        stack = ''
        for char in d:
            stack += char
            for k, v in numbers.items():
                if k in stack:
                    stack = stack.replace(k, v)
        first = get_first_number(stack)
        stack = ''

        for char in reversed(d):
            stack += char
            for k, v in numbers.items():
                if k in stack:
                    stack = stack.replace(k, v)
        
        last = get_last_number(''.join(reversed(stack)))
        value = first + last
        print('value=', value)

        calibration_values.append(int(value))

    print('calib values', sum(calibration_values))
        
        

def get_first_number(word):
    numbers = '123456789'

    for char in word:
        if char in numbers:
            value = char
            return value
        
def get_last_number(word):
    numbers = '123456789'

    for char in reversed(word):
        if char in numbers:
            value = char
            return value


if __name__ == '__main__':
    clean_data = part1.remove_line_break_char(data)
    words_to_numbers = words_into_numbers(clean_data)