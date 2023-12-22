import pprint
import pdb
with open(r"/Users/taylorhood/Documents/Projects/AdventOfCode2023/Day2/data.txt") as file:
    data = file.readlines()

def remove_line_break_char(data):
    data = [d[:-1] for d in data]
    return data

# 12 red cubes, 13 green cubes, and 14 blue cubes

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
                

def find_possible_game(game):
    """takes a list of dicts
    dicts {color: amount}

    """
    # bag contains
    # 12 red cubes, 13 green cubes, and 14 blue cubes

    # values = [{blue: 1, green: 2}, {red: 6, green: 8}]    

    bag = {'blue': 14, 'green': 13, 'red': 12}

    for round in game:
        print('round=', round)
        for k, v in round.items():
            if v > bag[k]:
                print("failed", k, v)
                return False
    return True

def sort_games(data):
    """take a dictionary
    
    key is game number
    value is a list of dicts of each round
        key is color; value is number
    """

    pprint.pprint(data)
    qualifying_games = []
    for k,v in data.items():
        if find_possible_game(v): 
            qualifying_games.append(int(k))
    
    print('total==', sum(qualifying_games))
    return qualifying_games
        


if __name__ == '__main__':
    clean_data = remove_line_break_char(data)
    test = data_to_game_dict(clean_data)
    pprint.pprint(test)

    sorted_games = sort_games(test)
    print('sorted games=', sorted_games)