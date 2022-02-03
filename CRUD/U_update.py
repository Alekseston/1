def update_user(us, ue):
    """
    This function help you to update your data in account
    """
    print(us)
    user_ue = input('Enter user email: ')

    if user_ue in ue:
        print('password: ', us[user_ue]['password'])
        print(us[user_ue])
        while True:
            user_p = input('Enter user password: ')
            if user_p == us[user_ue]['password']:
                print('Enter only data to update')
                e = input('Enter New Email: ')
                if e.strip() == "" or len(e) == 0:
                    print('Email will not change')
                else:
                    us[e] = us.pop(user_ue)
                    idx = ue.index(user_ue)
                    ue[idx] = e
                    user_ue = e
                    print(us)
                    print('New Email:', user_ue)
                n = input('Enter New Name: ')
                if n.strip() == "" or len(n) == 0:
                    print('Name will not change')
                else:
                    us[user_ue]['name'] = n
                    print('New Name: ', us[user_ue]['name'])
                pw = input('Enter New Password: ')
                if pw.strip() == "" or len(pw) == 0:
                    print('Password will not change')
                else:
                    us[user_ue]['password'] = pw
                    print('New Password: ', us[user_ue]['password'])
                ph = input('Enter New Phone: ')
                if ph.strip() == "" or len(ph) == 0:
                    print('Phone will not change')
                else:
                    us[user_ue]['phone'] = ph
                    print('New Phone: ', us[user_ue]['phone'])
                print(us)
                break
            else:
                print('Wrong password')
    else:
        print('There is no user with this email')
