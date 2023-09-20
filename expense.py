import csv
from PyInquirer import prompt

path_file_expense = 'expense_report.csv'

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },

]

# Fonction pour écrire les données dans un fichier CSV
#def write_expense(data):
 #   with open("./expense_report.csv", mode='a', newline='') as fichier:
  #      writer = csv.writer(fichier)
   #     writer.writerow(data.values())

def new_expense(*args):
    infos = prompt(expense_questions)
    print(infos)
    file = open(path_file_expense, mode='a')
    writer = csv.writer(file)
    writer.writerow(['amont: ' + infos['amount'], 'label: ' + infos['label'], 'spender: ' + infos['spender']])
    file.close()
    #write_expense(data)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    print("Expense Added !")
    return True


