#  Внедрение полноценной DB через SQLite3
import crud


def main():
    begin = input('Are you registered (y/n)? ')
    if begin == 'n':
        regist()
    elif begin == 'y':
        enter()


def enter():
    print('ENTER')
    name = input('Enter your name: ')
    password = input('Enter your password: ')
    chek_user = crud.login(name, password)
    print(chek_user)  # ПРОВЕРКА СТРОКИ ИЗ БД - ЧТО ВОЗВРАЩАЕТ
    if chek_user is None:
        print('Wrong username or password!')
        main()
    elif chek_user[3] == 0:
        print(f"Welcome, to user panel, {name}!")
        user_panel()
        return
    elif chek_user[3] == 1:
        print(f"Welcome, to Admin panel, {name}!")
        admin_panel()
        return


def regist():
    print('REGISTRATION')
    username = input('Enter your name: ')
    password = input('Enter your password: ')
    chek_user = crud.create_user(username, password)
    if chek_user is True:
        print(f"Registration Successful, {username}!\n"
              f"Please repeat your name and password!")
        enter()
    else:
        regist()


def admin_panel():
    print('ADMIN MENU')
    print('1. User List')
    print('2. Delete User')
    print('3. Add User') # ДОДЕЛАТЬ
    print('4. Exit')
    action = input('What’s next (1/2/3)?: ')

    if action == '1':
        count = 0
        for user in crud.read_users():
            count += 1
            print(f'{count}) User ID:',user[0],'| User Name:',user[1],'| User Password: ****')
        back = input('Return to the admin panel? (y/n)? ')
        if back == 'y':
            admin_panel()


    elif action == '2':
        count = 0
        for user in crud.read_users():
            count += 1
            print(f'{count}) User ID:', user[0], '| User Name:', user[1], '| User Password: ****')

        user_id = int(input('Enter User ID to delete: '))

        chek_id = crud.get_user(user_id)

        if chek_id is None:
            print(f'User {user_id} not found!')
            admin_panel()
        else:
            crud.delete_user(user_id)
            print(f'User {user_id} successfully deleted!')
        count = 0
        for user in crud.read_users():
            count += 1
            print(f'{count}) User ID:', user[0], '| User Name:', user[1], '| User Password: ****')
        back = input('Return to the admin panel? (y/n)? ')
        if back == 'y':
            admin_panel()

    elif action == '4':
        logout = input('Do you want to go out? (y/n)? ')
        if logout == 'y':
            print('Exit complete')
            main()
        else:
            admin_panel()
    elif action == '3':
        add_user()
        count = 0
        for user in crud.read_users():
            count += 1
            print(f'{count}) User ID:', user[0], '| User Name:', user[1], '| User Password: ****')
        admin_panel()





def user_panel():  # ДОДЕЛАТЬ (функция изменить пароль и еще придумать что-нибудь)
    print('USER MENU')
    print('1. At work')
    print('2. At work')
    print('3. At work')



def add_user():
     print('ADD A NEW USER')
     name = input('Enter user name: ')
     password = input('Enter user password: ')
     crud.create_user(name, password)
     print(f'User {name} successfully added!')



if __name__ == '__main__':
    main()
