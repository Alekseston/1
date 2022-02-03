def delete_user(us, ue):
    """
    This function help you to delete your account
    """
    print(us)
    user_ue = input('Enter user email: ')
    if user_ue in ue:
        print('password: ', us[user_ue]['password'])
        print(us[user_ue])
        while True:
            user_p = input('Enter user password: ')
            if user_p == us[user_ue]['password']:
                e = input('If you want to Delete account Enter "delete": ')
                if e.strip() == "" or len(e) == 0:
                    print('Email will not change')
                else:
                    if e == 'delete':
                        us.pop(user_ue)
                        ue.remove(user_ue)

                        print(us)
                        print(ue)
                        print('User', user_ue, 'was Deleted')
                    break

            else:
                print('Wrong password')

    else:
        print('There is no user with this email')

