from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated='auto')


class Hashing:
    @staticmethod
    def get_password_hashing(password):
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password, hashing_password):
        return pwd_context.verify(plain_password, hashing_password)


a = '$2b$12$MxHJ9lX5F0q5gHgMgb83cu9ekNmXnKBpld6LDW.R3sL7aMDaxHor6'
hashing = Hashing
s = hashing.verify_password('123', a)
print(s)
