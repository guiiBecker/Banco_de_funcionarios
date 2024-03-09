
import PySimpleGUI as sg
import conn

# realiza a conexão com o banco de dados
cnx = conn.cnx
cursor = conn.cursor
print("Connection established")


# Define o layout da janela para adicionar um empregado
def layout_add():
    layout_add = [
          [sg.Text("What is the employee ID?"), sg.Input(key='func_id')],
          [sg.Text("What is the name of the employee?"), sg.Input(key='nome')],
          [sg.Text("What is the job of the employee?"), sg.Input(key='carg')],
          [sg.Text("When was this employee hired? (YYYY-MM-DD)"), sg.Input(key='data_contratacao')],
          [sg.Text("What is the ID of the department?"), sg.Input(key='id_depto')],
          [sg.Text("What is the salary of this employee?"), sg.Input(key='salario')],
          [sg.Button("Send"), sg.Button("Cancel"), sg.Button("Back")]
      ]  
    return layout_add


# Define layout para remover um empregado
def layout_remove():
    layout_remove = [
        [sg.Text("What is the employee ID?"), sg.Input(key='func_id')],
        [sg.Text("What is the name of the employee?"), sg.Input(key='nome')],
        [sg.Button("Send"), sg.Button("Cancel"), sg.Button("Back")]
    ]
    return layout_remove

# Define layout para fazer uma busca
def layout_search():
    layout_search = [
      [sg.Table(values= conn.search(), headings=['ID', 'Nome', 'Salário', 'Cargo', 'Data de Contratação', 'Departamento'],
              justification='left', num_rows=10, auto_size_columns=False,
              col_widths=[10, 20, 10, 20, 20, 15])],
    [sg.Button('Done'), sg.Button("Back")]
    ]
    return layout_search

# Define layout inicial
layout =[
    [sg.Button("search")],
    [sg.Button("Add a employee")],
    [sg.Button("Delete a employee")],
    [sg.Button("Cancel")]
]
window = sg.Window("Manager Database", layout)


# evento de loop principal
while True:
    event, values = window.read()
# evento de janela fechada ou opção cancel
    if event == sg.WINDOW_CLOSED or event =="Cancel":
        break
# evento de voltar para a página anterior
    elif event == "Back":
        window.close()
        window = sg.Window("Manager Database", layout)
# ADD um novo empregado
    elif event == "Add a employee":
        window = sg.Window("Add a employee", layout_add())
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event =="Cancel":
                break
# coletar infos para add o novo empregado
            elif event == "Send":
                try:
                    employeeid= int(values['func_id'])
                    employee_name = values['nome']
                    employee_job = values['carg']
                    employee_hired = values['data_contratacao']
                    department_id = int(values['id_depto'])
                    employee_salary = int(values['salario'])
                    conn.newemp(employeeid, employee_name, employee_salary, employee_job, employee_hired, department_id)
                    print("The new employer was been added")
                    window.close()
                except ValueError:
                     sg.popup_error("Erro: Verifique os valores inseridos")

# Del um empregado
    elif event == "Delete a employee":
        window = sg.Window("Add a employee", layout_remove())
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event =="Cancel":
                break
            
# coletar informações para deletar um empregado
            elif event == "Send":
                try:
                    employeeid= int(values['func_id'])
                    employee_name = values['nome']
                    conn.del_employer(employeeid, employeeid)
                    print("The employee has been removed")
                    window.close()
                except ValueError:
                    sg.popup_error("Erro: Verifique os valores inseridos")

# realizar uma pesquisa no bd
    elif event == "search":
        window_search = sg.Window('Search Results', layout_search())
        while True:
            event_search, values_search = window_search.read()
            if event_search == sg.WINDOW_CLOSED:
                break
            elif event_search == "Done":
                window.close()

# eventos para finalizar a execução
cursor.close()
cnx.close()           
window.close()