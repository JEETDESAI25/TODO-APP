# from functions import get_todos, write_todos

import functions
import time 

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True :

    #Get user input and strip space chars from it 

    user_action = input("Type add, Show, Edit, remove or Exit : ")
    user_action = user_action.strip()

    #check if user action is "add" 

    if user_action.startswith("add") :
        todo = user_action[4:]
        
        todos = functions.get_todos(filepath="todos.txt")
        
        todos.append(todo + '\n')

        functions.write_todos(filepath="todos.txt", todos_arg= todos)
       
    
    elif user_action.startswith("show") :
        todos = functions.get_todos("todos.txt")



        for index , item in enumerate(todos) :
            item = item.strip('\n')
            row = f"{index}-{item}"
            print(row)
    
    elif user_action.startswith("edit") :

        try:

            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()
            
            new_todo = input("Enter the new todo : ")
            todos[number] = new_todo + '\n'

            functions.write_todos("todos.txt", todos)
        
        except ValueError:
            print("Your command is not valid.")
            continue    
             
        
    elif user_action.startswith("remove") :

        try:
            todo = int(user_action[7:])

            todos = functions.get_todos()

            index = todo - 1 
            removed = todos.pop(index)

            functions.write_todos("todos.txt", todos)
            
            print('Removed todo :' , removed)

        except IndexError:
            print("There is no item with that number.")
            continue        
            
    elif user_action.startswith("exit") : 
        break 

    else :
        print("This Command is not valid")


print("BYE")




    


    
