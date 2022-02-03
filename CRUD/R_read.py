def user_info(email, user_emails, users_storage):
    """
    This function help you to read your data in account
    """
    if email in user_emails:
        # a = 'User email: '
        # b = 'User_info: '
        # c = str(users_storage[email])
        message = 'User email: "' + email + '"\n' + 'User_info: ' + str(users_storage[email])
        return message
    else:
        message = 'No user with email:', email
        return message

def all_users_info(users_storage):
    for k, v in users_storage.items():
        user_email = ' User_email: ' + k
        user_info_1 = 'User_info: ' + str(v)
        print(str(user_email), '\n', user_info_1)
