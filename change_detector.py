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

board0 = [
[0, [["A", 12], ["B", 11], ["C", 10], ["D", 9], ["E", 8], ["F", 10], ["G", 11], ["H", 12]]],
[1, [["A", 7], ["B", 7], ["C", 7], ["D", 7], ["E", 7], ["F", 7], ["G", 7], ["H", 7]]],
[2, [["A", 0], ["B", 0], ["C", 0], ["D", 0], ["E", 0], ["F", 0], ["G", 0], ["H", 0]]],
[3, [["A", 0], ["B", 0], ["C", 0], ["D", 0], ["E", 0], ["F", 0], ["G", 0], ["H", 0]]],
[4, [["A", 0], ["B", 0], ["C", 0], ["D", 0], ["E", 0], ["F", 0], ["G", 0], ["H", 0]]],
[5, [["A", 0], ["B", 0], ["C", 0], ["D", 0], ["E", 0], ["F", 0], ["G", 0], ["H", 0]]],
[6, [["A", 1], ["B", 1], ["C", 1], ["D", 1], ["E", 1], ["F", 1], ["G", 1], ["H", 1]]],
[7, [["A", 6], ["B", 5], ["C", 4], ["D", 3], ["E", 2], ["F", 4], ["G", 5], ["H", 6]]]
]

board1 = [
[0, [["A", 12], ["B", 11], ["C", 10], ["D", 9], ["E", 8], ["F", 10], ["G", 11], ["H", 12]]],
[1, [["A", 7], ["B", 7], ["C", 7], ["D", 7], ["E", 7], ["F", 7], ["G", 7], ["H", 7]]],
[2, [["A", 0], ["B", 0], ["C", 0], ["D", 0], ["E", 0], ["F", 0], ["G", 0], ["H", 0]]],
[3, [["A", 0], ["B", 0], ["C", 0], ["D", 0], ["E", 0], ["F", 0], ["G", 0], ["H", 0]]],
[4, [["A", 0], ["B", 0], ["C", 0], ["D", 0], ["E", 0], ["F", 0], ["G", 0], ["H", 0]]],
[5, [["A", 0], ["B", 0], ["C", 0], ["D", 0], ["E", 1], ["F", 0], ["G", 0], ["H", 0]]],
[6, [["A", 1], ["B", 1], ["C", 1], ["D", 1], ["E", 0], ["F", 1], ["G", 1], ["H", 1]]],
[7, [["A", 6], ["B", 5], ["C", 4], ["D", 3], ["E", 2], ["F", 4], ["G", 5], ["H", 6]]]
]


for row_tup in board0:
    row_num = row_tup[0]
    row_list = row_tup[1]

    parallel_row_tup = board1[board0.index(row_tup)]
    parallel_row_num = parallel_row_tup[0]
    parallel_row_list = parallel_row_tup[1]
    
    '''print(row_num, row_list)
    print(parallel_row_num, parallel_row_list)'''

    for row_spot in row_list:
        row_column = row_spot[0]
        actual_spot = row_spot[1]

        parallel_row_spot = parallel_row_list[row_list.index(row_spot)]
        parallel_row_column = parallel_row_spot[0]
        parallel_actual_spot = parallel_row_spot[1]
        
        if actual_spot != parallel_actual_spot: 
            print(row_num, row_column, " board0: ", actual_spot, "board1: ", parallel_actual_spot)
        # print(parallel_row_num, parallel_row_column, " - ", parallel_actual_spot)