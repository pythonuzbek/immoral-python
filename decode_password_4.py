import hashlib
from urllib.request import urlopen

target = '65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5'

password_list = str(urlopen(
    'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read(),
                 'utf-8')
c = 0
for password in password_list.split():
    c += 1
    guess = hashlib.sha256(bytes(password, 'utf-8')).hexdigest()
    print(guess)
    if guess == target:
        print(f"password found: {password}")
        break
    else:
        print(f"{guess}  --- password didn't match")
print(c)
