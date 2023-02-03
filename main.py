def ask_password(login, password, success, failure):
    vowels_lst = {'e', 'a', 'o', 'u', 'i', 'u', 'y'}
    vowels = 0
    for sym in password:
        if sym in vowels_lst:
            vowels += 1
    login_cons = ''
    password_cons = ''
    for sym in login:
        if sym.isalpha() and not sym in vowels_lst:
            login_cons += sym

    for sym in password:
        if sym.isalpha() and not sym in vowels_lst:
            password_cons += sym

    if login_cons == password_cons and vowels == 3:
        success()
        return True
    else:
        failure()
        return False


def main(login, password):
