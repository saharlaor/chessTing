import json
from enum import Enum


class soldier(Enum):
    
    empty = 0

    pawn_w = 1
    king_W = 2
    queen_w = 3
    bishop_w = 4
    knight_w = 5
    tower_w = 6

    pawn_b = 7
    king_b = 8
    queen_b = 9
    bishop_b = 10
    knight_b = 11
    tower_b = 12


default_board = [
[0, [["A", 0], ["B", 0], ["C", 0], ["D", 0], ["E", 0], ["F", 0], ["G", 0], ["H", 0]]],
[1, [["A", 0], ["B", 0], ["C", 0], ["D", 0], ["E", 0], ["F", 0], ["G", 0], ["H", 0]]],
[2, [["A", 0], ["B", 0], ["C", 0], ["D", 0], ["E", 0], ["F", 0], ["G", 0], ["H", 0]]],
[3, [["A", 0], ["B", 0], ["C", 0], ["D", 0], ["E", 0], ["F", 0], ["G", 0], ["H", 0]]],
[4, [["A", 0], ["B", 0], ["C", 0], ["D", 0], ["E", 0], ["F", 0], ["G", 0], ["H", 0]]],
[5, [["A", 0], ["B", 0], ["C", 0], ["D", 0], ["E", 0], ["F", 0], ["G", 0], ["H", 0]]],
[6, [["A", 0], ["B", 0], ["C", 0], ["D", 0], ["E", 0], ["F", 0], ["G", 0], ["H", 0]]],
[7, [["A", 0], ["B", 0], ["C", 0], ["D", 0], ["E", 0], ["F", 0], ["G", 0], ["H", 0]]]
                ]


board0_str = open("./data/old_board.json", "r").read()
board0_list = json.loads(board0_str)

board1_str = open("./data/new_board.json", "r").read()
board1_list = json.loads(board1_str)

old_spot = []
new_spot = [] 

for row_tup in board0_list:
    row_num = row_tup[0]
    row_list = row_tup[1]

    parallel_row_tup = board1_list[board0_list.index(row_tup)]
    parallel_row_num = parallel_row_tup[0]
    parallel_row_list = parallel_row_tup[1]
    
    for row_spot in row_list:
        row_column = row_spot[0]
        actual_spot = row_spot[1]

        parallel_row_spot = parallel_row_list[row_list.index(row_spot)]
        parallel_row_column = parallel_row_spot[0]
        parallel_actual_spot = parallel_row_spot[1]
        
        if actual_spot != parallel_actual_spot: 
            print(row_num, row_column, " board0: ", actual_spot, " --> ","board1: ", parallel_actual_spot)
            if parallel_actual_spot == 0:
                soldier_moved = soldier(actual_spot)
                old_spot.append(row_num)
                old_spot.append(row_column)
            else:
                new_spot.append(row_num)
                new_spot.append(row_column)


print(soldier_moved.name, " moved from " , old_spot, "to ", new_spot)