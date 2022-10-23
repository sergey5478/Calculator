board = list(map(str, range(1, 10)))

def draw_board():
    print('-' * 20)
    for i in range(3):
        for k in range(3):
            print(f"{board[k + i * 3]:^5}", end=" ")
        print(f"\n{'-' * 20}")
    print()

def check_win():
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    n = [board[x[0]] for x in win_coord if board[x[0]] == board[x[1]] == board[x[2]]]
    return n[0] if n else n
check_win(0)

# def place_sign(token):
#     global board
#     while True:
#         answer = input(f"Enter a number from 1 to 9.\nSelect a position {token}? ")
#         if answer.isdigit() and int(answer) in range(1, 10):
#             answer = int(answer)
#             pos = board[answer - 1]
#             if pos not in (chr(10060), chr(11093)):
#                 board[answer - 1] = chr(10060) if token == "X" else chr(11093)
#                 break
#             else:
#                 print(f"This cell is already occupied{chr(9995)}{chr(129292)}")
#         else:
#             print(f"Incorrect input{chr(9940)}. Are you sure you entered a correct number?")


# def check_win():
#     win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
#     n = [board[x[0]] for x in win_coord if board[x[0]] == board[x[1]] == board[x[2]]]
#     return n[0] if n else n


# def main():
#     counter = 0
#     #draw_board()
#     while True:
#         place_sign("O") if counter % 2 else place_sign("X")
#         #draw_board()

#         if counter > 3:
#             if check_win():
#                 # print(f"{check_win()} - WIN{chr(127942)}{chr(127881)}!")
#                 break
#         if counter == 8:
#             # print(f"Drawn game {chr(129318)}{chr(129309)}!")
#             break
#         counter += 1

#main()

