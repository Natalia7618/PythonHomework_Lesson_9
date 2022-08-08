import func

game_over = False
human = True
 
while game_over == False:
    func.print_fields()
    if human == True:
        symbol = "X"
        step = int(input("Ваш ход: "))
    else:
        print("Ход компьютера: ")
        symbol = "O"
        step = func.comp_step()
    if step != "":
        func.step_fields(step,symbol) 
        win = func.get_result() 
        if win != "":
            game_over = True
            win = 'компьютер'
        else:
            game_over = False
    else:
        print("Ничья!")
        game_over = True
        win = "мир"
    human = not(human)        
 
func.print_fields()
print("Победил", win)