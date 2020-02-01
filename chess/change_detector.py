import json

empty = 0

pawn_w = 1
king_W = 2
queen_w = 3
bishop_w = 4
knight_w = 5
tower_w = 6

pawn_w = 7
king_W = 8
queen_w = 9
bishop_w = 10
knight_w = 11
tower_w = 12

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


board0_str = open("old_board.json", "r").read()
board0 = json.loads(board0_str)

board1_str = open("new_board.json", "r").read()
board1 = json.loads(board1_str)


for row_tup in board0:
    row_num = row_tup[0]
    row_list = row_tup[1]

    parallel_row_tup = board1[board0.index(row_tup)]
    parallel_row_num = parallel_row_tup[0]
    parallel_row_list = parallel_row_tup[1]
    
    for row_spot in row_list:
        row_column = row_spot[0]
        actual_spot = row_spot[1]

        parallel_row_spot = parallel_row_list[row_list.index(row_spot)]
        parallel_row_column = parallel_row_spot[0]
        parallel_actual_spot = parallel_row_spot[1]
        
        if actual_spot != parallel_actual_spot: 
            print(row_num, row_column, " board0: ", actual_spot, "board1: ", parallel_actual_spot)

