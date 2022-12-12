import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass


sg.theme("BlueMono")
clock = sg.Text("", key="clock")
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter TODO", key="todo")
add_button = sg.Button(
    size=10,
    image_source="TODO APP/plus-2.png",
    tooltip="Add todo",
    key="Add",
)
list_box = sg.Listbox(
    values=functions.get_todos(), key="todos", enable_events=True, size=[45, 10]
)
edit_button = sg.Button(
    size=10, image_source="TODO APP/edit-2.png", tooltip="Edit Todo", key="Edit"
)
remove_button = sg.Button(
    size=10,
    image_source="TODO APP/pngwing.com-2.png",
    tooltip="Removes the completed todo",
    key="Remove",
)
exit_button = sg.Button(
    size=10,
    image_source="TODO APP/logout.png",
    tooltip="Exits the app",
    key="Exit",
)

window = sg.Window(
    "My TO-DO App",
    layout=[
        [clock],
        [label],
        [input_box, add_button],
        [list_box, edit_button, remove_button],
        [exit_button],
    ],
    font=("Helvetica", 20),
)

while True:

    event, values = window.read(timeout=300)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(1, event)
    print(2, values)
    print(3, values["todos"])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item to edit", font=("Helvetica", 20))

        case "todos":
            window["todo"].update(value=values["todos"][0])
        case "Remove":
            try:
                todo_to_remove = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_remove)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item to remove", font=("Helvetica", 20))

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break


window.close()
