''' passwords object '''
import model
from peewee import *
import time

class Password(model.BaseModel):
    ''' password object '''
    email = CharField(128, null=True)
    phone = CharField(20, null=True)
    username = CharField(40)
    password = CharField(40)
    website = CharField(512)
    edit_time = TimestampField()

    class Meta:
        db_table = 'passwords'

    @classmethod
    def new(cls, data):
        ''' add this username and password '''
        if cls.select().where((cls.username == data['username']) & (cls.website == data['website'])).exists():
            return None
        return cls.create(
            website=data['website'],
            username=data['username'],
            password=data['password'],
            email=data['email'],
            phone=data['phone'],
            edit_time=time.time()
        )

    @classmethod
    def search(cls, keyword):
        return cls.select().where((keyword << cls.email) | (keyword << cls.username) | (keyword << cls.website))

    # @classmethod
    # def get_by_user(cls, user):
    #     return

    def edit(self, data):
        ''' edit password information '''
        Password.update(
            email=data['email'],
            phone=data['phone'],
            username=data['username'],
            password=data['password'],
            website=data['website'],
            edit_time=time.time()
        ).where(Password._meta.primary_key == self.id).execute()

