from PyInquirer import prompt
import csv

path_file_user = 'users.csv'

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New user - Name: "
    }
]

def add_user():
    infos = prompt(user_questions)
    print(infos)
    file = open(path_file_user, mode='a')
    writer = csv.writer(file)
    writer.writerow([infos['name']])
    file.close()
    print("New user added !")

    # This function should create a new user, asking for its name
    return