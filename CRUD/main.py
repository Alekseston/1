from C_create import create_user
from R_read import user_info, all_users_info
from U_update import update_user
from D_delete import delete_user


def main():
    """
    This program help you to create account or: read, update, delete your data in account
    """
    user_emails = []
    users_storage = {}
    print('For help enter "--Help"')

    while True:
        action = input('Please enter action command: ')
                       # '\n    "c" to create,'
                       # '\n or "ra" to read all,'
                       # '\n or "ru" to read user,'
                       # '\n or "u" to update, '
                       # '\n or "d" to delete actions: ')
        action = action.lower()
        action = action.strip()
        if action == 'c':
            print('action = ', action)

            email = input('Email: ')
            if email not in user_emails:
                name = input('Name: ')
                password = input('Password: ')
                phone = input('Phone: ')
                create_user(email, name, password, phone, user_emails, users_storage)
                print('user_emails = ', user_emails)
                print('users_storage: "' + email + '" = ', users_storage[email])
            else:
                print('User with this email address already exists')

        elif action == 'ra':
            print('action= ', action)
            all_users_info(users_storage)

        elif action == 'ru':
            user_e = input('Enter user email')
            message = user_info(user_e, user_emails, users_storage)

            print('action= ', action)
            print('User: ', message)

        elif action == 'u':
            print('action= ', action)
            update_user(users_storage, user_emails)

        elif action == 'd':
            print('action= ', action)
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
