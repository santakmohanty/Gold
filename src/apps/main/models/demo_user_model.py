import datetime
import random
import string

from passlib.hash import pbkdf2_sha256
from sqlalchemy import Column, Integer, String, DateTime, BigInteger

from apps.main.models.base import session, BaseModel

class Gender:
    MALE = 10
    FEMALE = 20
    OTHER = 30


class DemoUser(BaseModel):
    # 'user' is a reserved word in postgres
    __tablename__ = 'demo_user'
    id = Column(BigInteger, primary_key = True, autoincrement = True, unique = True)
    first_name = Column(String(40))
    last_name = Column(String(40))
    email = Column(String(50), unique = True)
    mobile_number = Column(String(10))
    gender = Column(Integer, nullable = True)
    date_of_birth = Column(DateTime, nullable = True)
    password = Column(String(100))
    created_at = Column(DateTime, default = datetime.datetime.now())
    updated_at = Column(DateTime, onupdate = datetime.datetime.now())

    def __repr__(self):
        return u"User(%s, %s)" % (self.first_name, self.email)

    @classmethod
    def add(cls, data):
        user = cls()
        if data.get('password') is None:
            password = cls._generate_random_password(6)
            data['password'] = cls._hash_password(password)
        user.fill(**data)
        user.save()
        return user, password

    @classmethod
    def authenticate(cls, email, password):
        user = cls.get_by_email(email)
        if user:
            if cls._match_password(password, user.password):
                return user
        return None

    @staticmethod
    def _generate_random_password(string_length = 12):
        """Generate a random string of letters, digits and special characters """
        password_characters = string.ascii_letters
        return ''.join(random.choice(password_characters) for i in range(string_length))

    @classmethod
    def _hash_password(cls, password_plain):
        hashed_password = pbkdf2_sha256.encrypt(password_plain, rounds = 200000, salt_size = 16)
        return hashed_password

    @classmethod
    def _match_password(cls, password_plain, hashed_password):
        return pbkdf2_sha256.verify(password_plain, hashed_password)
