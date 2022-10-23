# 3. Создайте программу для игры в "Крестики-нолики". Поле 3x3.
# Игрок - игрок, без бота.
game = list(range(1,10))
print(game)
def draw_game(game):
    print ("-" * 19)
    for i in range(3):
        print (f'| {game[0+i*3]:^4}| {game[1+i*3]:^4}| {game[2+i*3]:^4}|')
        print ("-" * 19)

def take_input(player_number):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_number+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(game[player_answer-1]) not in "XO"):
                game[player_answer-1] = player_number
                valid = True
            else:
                print ("Эта клеточка уже занята")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

def check_win(game):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),\
        (0,4,8),(2,4,6))
    for w in win_coord:
        
        if game[w[0]] == game[w[1]] == game[w[2]]:
            
            return game[w[0]]
    return False

def main(game):
    counter = 0
    win = False
    while not win:
        draw_game(game)
        if counter % 2 == 0:
            take_input("\U0000274C")
        else:
            take_input("\U00002B55")
        counter += 1
        if counter > 4:
            tmp = check_win(game)
            if tmp:
                print (tmp, "\033[32m выиграл!\U0001F386")
                win = True
                break
        if counter == 9:
            print ("\033[31m Ничья!\U0001F926")
            break
    draw_game(game)

main(game)