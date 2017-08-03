''' password ask object '''
import model
from peewee import *
import time
from model.password import Password

class PasswordAsk(model.BaseModel):
    ''' password object '''
    password = ForeignKeyField(Password, related_name='password_ask')
    ask = CharField(64)
    answer = CharField(64)

    class Meta:
        db_table = 'passwordAsk'

    @classmethod
    def new(cls, data):
        ''' add this username and password '''
        return cls.create(
            password=data['password'],
            ask=data['ask'],
            answer=data['answer']
        )

    @classmethod
    def get_by_password(cls, password):
        return cls.select().where(cls.password == password)

    @classmethod
    def remove_by_password(cls, password):
        ''' delete label '''
        cls.delete().where(cls.password == password).execute()

    @classmethod
    def get_by_ask(cls, password, ask):
        return cls.get((cls.password == password) & (cls.ask == ask))

    def edit(self, data):
        ''' edit password information '''
        PasswordAsk.update(
            ask=data['ask'],
            answer=data['answer']
        ).where(PasswordAsk._meta.primary_key == self.id).execute()

