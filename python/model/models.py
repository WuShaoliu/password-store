''' Initialize database, such as tables, data '''
import peewee

from model import db

from model.password import Password
from model.password_ask import PasswordAsk


try:
    db.create_tables([
        Password,
        PasswordAsk
    ])
except peewee.OperationalError as event:
    print('OperationalError', event)
    pass
except peewee.ProgrammingError as event:
    # 错误:  关系 "bloglabels" 已经存在
    pass
