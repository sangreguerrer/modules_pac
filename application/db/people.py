employees=['Виталий Гармохин','Марк Безус', 'Николай Рабочий','Антон Мельник', 'Степан Горилкин']
def get_employees():
    while employees:
        name=input('Введите имя сотрудника:')
        if name in employees:
            print('Есть такой')
        else:
            print('На больничном')
        return ''
