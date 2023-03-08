import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo", background_color="#FBF199")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),
                      key="todos",
                      enable_events=True,
                      size=[45, 10], font="Ariel")
edit_button = sg.Button("Edit")

main_window = sg.Window("My To-Do App",
                        layout=[[label], [input_box, add_button], [list_box, edit_button]],
                        font=('Helvetica', 12))

while True:
    event, values = main_window.read()

    print(event)
    print(values)

    todos = functions.get_todos()

    match event:
        case "Add":
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break;


main_window.close()


