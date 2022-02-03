from C_create import create_user
from R_read import user_info, all_users_info
from U_update import update_user
from D_delete import delete_user

Password_d = 'qweasd123'


def main():
    """
    This program help you to create account or: read, update, delete your data in account
    """
    user_emails = []
    users_storage = {}

    while True:
        print('For help enter "--Help"')
        action = input('Please enter action command: ')
        # '\n    "c" to create,'
        # '\n or "ra" to read all,'
        # '\n or "ru" to read user,'
        # '\n or "u" to update, '
        # '\n or "d" to delete actions: ')
        action = action.lower()
        action = action.strip()
        if action == 'c':
            print('action = Create account')
            email = input('Email: ')
            if email not in user_emails:
                name = input('Name: ')
                password = input('Password: ')
                phone = input('Phone: ')
                create_user(email, name, password, phone, user_emails, users_storage)
                # print('user_emails = ', user_emails)
                print('Created user: Email: "' + email + '" User_info: ', users_storage[email])
            else:
                print('User with this email address already exists')

        elif action == 'ra':
            print('action = Read all')
            while True:
                passw = input('Enter password to read all data: ')
                if passw == Password_d:
                    all_users_info(users_storage)
                    break
                else:
                    print('Wrong password')

        elif action == 'ru':
            print('action = Read user')
            user_e = input('Enter user email: ')
            if user_e in user_emails:
                # print('password: ', users_storage[user_e]['password'])
                # print(users_storage[user_e])
                while True:
                    user_p = input('Enter user password: ')
                    if user_p == users_storage[user_e]['password']:
                        message = user_info(user_e, user_emails, users_storage)
                        print(message)
                        break
                    else:
                        print('Wrong password')

        elif action == 'u':
            print('action = Update')
            update_user(users_storage, user_emails)

        elif action == 'd':
            print('action = Delete')
            delete_user(users_storage, user_emails)
        elif 'help' in action:
            print('c --Please enter "c" to create action',
                  'ra --Please enter "ra" to read all action',
                  'ru --Please enter "ru" to read user action',
                  'u --Please enter "u" to update action',
                  'd --Please enter "d" to delete action',
                  sep='\n')


if __name__ == "__main__":
    main()
