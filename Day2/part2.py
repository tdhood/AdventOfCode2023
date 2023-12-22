import pprint
import pdb
with open(r"/Users/taylorhood/Documents/Projects/AdventOfCode2023/Day2/data.txt") as file:
    data = file.readlines()

def remove_line_break_char(data):
    data = [d[:-1] for d in data]
    return data


def data_to_game_dict(data):
    #game_num : [
    #   { green: 10, blue: 9 },
    #   {}
# ]
    notes = {}

    for d in data:
        game, game_data= d.split(": ")
        game_key = game.split(' ')[1]

        rounds = game_data.split('; ') # list of rounds = [10 green, 9 blue], [7 green, 1 red], ...
        round_list = []
        for r in rounds:
            color_data = r.split(', ') # [10 green, 9 blue]
            round_dict = {}
            for c in color_data:
                color_value, color_key = c.split(" ")
                round_dict[color_key] = int(color_value) 
            round_list.append(round_dict)
        
        notes[game_key] = round_list
    
    return notes

def find_max_gems_per_game(game_dict):
    """takes a list of dicts
    dicts {color: amount}

    """
    # bag contains
    # 12 red cubes, 13 green cubes, and 14 blue cubes

    # values = [{blue: 1, green: 2}, {red: 6, green: 8}]    
    max_bag_for_all = {}
    for key, game in game_dict.items():
        # game = list
        max_bag = {'blue': 0, 'green': 0, 'red': 0}
        for round in game:
            for color, amount in round.items():
                if amount > max_bag[color]:
                    max_bag[color] = amount
        max_bag_for_all[key] = max_bag

    return max_bag_for_all

def calc_bag_power(max_gems_dict):
    """takes a dict 
    {
        '1': {'green': int, 'blue': int, 'red': int}, 
        '2': ...
    }

    multiply each int per game, then sum
    """

    powers = []

    for key, max_gems in max_gems_dict.items():
        power = 1
        for gems, value in max_gems.items():
            power*=value
        powers.append(power)
    
    print('powers+++', powers)
    print('sum of powers===', sum(powers))



clean_data = remove_line_break_char(data)
organized_data = data_to_game_dict(clean_data)

max_gems_per_game = find_max_gems_per_game(organized_data)
pprint.pprint(max_gems_per_game)

powers = calc_bag_power(max_gems_per_game)
