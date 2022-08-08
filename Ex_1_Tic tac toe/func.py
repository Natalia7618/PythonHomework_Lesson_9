import data

def print_fields():
    print(data.fields[0], end = " ")
    print(data.fields[1], end = " ")
    print(data.fields[2])
 
    print(data.fields[3], end = " ")
    print(data.fields[4], end = " ")
    print(data.fields[5])
 
    print(data.fields[6], end = " ")
    print(data.fields[7], end = " ")
    print(data.fields[8])
     
def step_fields(step,symbol):
    ind = data.fields.index(step)
    data.fields[ind] = symbol
 
def get_result():
    win = ""
    for i in data.victories_terms:
        if data.fields[i[0]] == "X" and data.fields[i[1]] == "X" and data.fields[i[2]] == "X":
            win = "X"
        if data.fields[i[0]] == "O" and data.fields[i[1]] == "O" and data.fields[i[2]] == "O":
            win = "O"         
    return win
 
def check_line(sum_O,sum_X):
    step = ""
    for line in data.victories_terms:
        o = 0
        x = 0
        for j in range(0,3):
            if data.fields[line[j]] == "O":
                o = o + 1
            if data.fields[line[j]] == "X":
                x = x + 1
        if o == sum_O and x == sum_X:
            for j in range(0,3):
                if data.fields[line[j]] != "O" and data.fields[line[j]] != "X":
                    step = data.fields[line[j]]              
    return step
 
def comp_step():        
    step = ""
    step = check_line(2,0)
    if step == "":
        step = check_line(0,2)        
    if step == "":
        step = check_line(1,0)           
    if step == "":
        if data.fields[4] != "X" and data.fields[4] != "O":
            step = 5           
    if step == "":
        if data.fields[0] != "X" and data.fields[0] != "O":
            step = 1           
    return step