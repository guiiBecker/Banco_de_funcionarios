import mysql.connector as mysql
import PySimpleGUI as sg

# Dados para conexão entre a solução e a database
# substitua as opções user e password para que funcione de acordo com a sua instalação.
cnx = mysql.connect(
    host ='localhost',
    user = 'guilherme',
    password = '@becker',
    database = 'banco_funcionarios'
)
cursor = cnx.cursor()


# Define as funções com comandos de SQL Querie

#Função de pesquisar no banco de dados
def search():
    try:
        query = "Select * FROM funcionarios"
        cursor.execute(query)
        results=cursor.fetchall()
        return results
    except mysql.Error as err:
        sg.popup_erro(f'error to search employees: {err}')    
        return []
    
#Função de deleltar um empregado do banco de dados  
def del_employer(employeeid, employee_name):
    try:
        delete = "DELETE FROM funcionarios WHERE id_func = %s AND nome = %s"
        cursor.execute(delete, (employeeid, employee_name))
        cnx.commit()
    except mysql.Error as err:
        sg.popup_erro(f'error to search employees: {err}')    
      
#Função de adicionar um novo empregado ao banco de dados 
def newemp(func_id, nome, salario, carg, data_contratacao, id_depto):
    try:
        add = "INSERT INTO funcionarios (id_func, nome, salario, cargo, data_contratacao, id_depto) VALUES (%s,%s,%s,%s,%s,%s)"
        values = (func_id, nome, salario, carg, data_contratacao, id_depto)   
        cursor.execute(add, values)
        cnx.commit()
    except mysql.Error as err:
        sg.popup_error(f"Erro ao adicionar novo funcionário: {err}")