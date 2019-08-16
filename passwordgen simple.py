import string
import secrets

def password_char():
    charset = string.ascii_letters + string.digits + '!"§$%&/()=?´^{[]}\/+#-.,;:_*/<>'

    return charset

def generate_pw(charset):
    password = []

    for c in range(40):
        password += secrets.choice(charset)

    pw_new = ''.join(password)
    print(pw_new)

def main():
    stub = password_char()
    generate_pw(stub)

if __name__ == "__main__":
    main()
