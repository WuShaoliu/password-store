''' password view '''
import time
import json
import datetime
from view import router, BaseHandler, SecureHandler, get_post_json
from playhouse.shortcuts import model_to_dict
from peewee import DoesNotExist

from model.password import Password
from model.password_ask import PasswordAsk
from config import RESP

@router('/passwords')
class PasswordsHandler(BaseHandler):
    def get(self):
        password_list = []

        passwords = Password.get_all()
        if passwords:
            for password in passwords:
                password_dict = model_to_dict(password)
                password_dict['edit_time'] = float(time.mktime(password_dict['edit_time'].timetuple()))
                password_dict['asks'] = []
                password_asks = PasswordAsk.get_by_password(password)
                if password_asks:
                    for password_ask in password_asks:
                        password_dict['asks'].append(model_to_dict(password_ask, exclude=[PasswordAsk.password]))
                
                password_list.append(password_dict)
        return self.finish(
            {'code': RESP['SUCCESS']['CODE'], 'data': password_list, 'msg': RESP['SUCCESS']['MSG']}
            )

    def post(self):
        return self.finish({'code': RESP['FORBID'], 'msg': RESP['FORBID']['MSG']})

@router('/password/add')
class PasswordAddHandler(BaseHandler):
    def get(self):
        return self.finish({'code': RESP['FORBID'], 'msg': RESP['FORBID']['MSG']})

    def post(self):
        request = get_post_json(self.request)
        if (not request):
            return self.finish(
                {'code': RESP['ERROR']['CODE'], 'msg': RESP['ERROR']['MSG']}
                )

        password = Password.new(request)
        if not password:
            return self.finish(
                {'code': RESP['REPEAT']['CODE'], 'msg': RESP['REPEAT']['MSG']}
                )

        for ask in request['asks']:
            ask['password'] = password
            PasswordAsk.new(ask)
        return self.finish(
            {'code': RESP['SUCCESS']['CODE'], 'msg': RESP['SUCCESS']['MSG']}
            )

    def options(self):
        return self.finish(
            {'code': RESP['SUCCESS']['CODE'], 'msg': RESP['SUCCESS']['MSG']}
            )

@router('/password/edit')
class PasswordAddHandler(BaseHandler):
    def get(self):
        return self.finish({'code': RESP['FORBID'], 'msg': RESP['FORBID']['MSG']})

    def post(self):
        request = get_post_json(self.request)
        if (not request):
            return self.finish(
                {'code': RESP['ERROR']['CODE'], 'msg': RESP['ERROR']['MSG']}
                )
        password = Password.get_by_pk(request['id'])
        password.edit(request)
        old_asks = PasswordAsk.get_by_password(password)

        update_asks_id = []
        times = 0
        for new_ask in request['asks']:
            try:
                password_ask = PasswordAsk.get_by_ask(password, new_ask['ask'])
                password_ask.edit(new_ask)
                update_asks_id.append(new_ask['id'])
            except DoesNotExist:
                new_ask['password'] = password
                pass_ask = PasswordAsk.new(new_ask)
                update_asks_id.append(pass_ask.id)
        for old_ask in old_asks:
            if not old_ask.id in update_asks_id:
                old_ask.remove()

        return self.finish(
            {'code': RESP['SUCCESS']['CODE'], 'msg': RESP['SUCCESS']['MSG']}
            )
    def options(self):
        return self.finish(
            {'code': RESP['SUCCESS']['CODE'], 'msg': RESP['SUCCESS']['MSG']}
            )

@router('/password/delete')
class PasswordDeleteHandler(BaseHandler):
    def get(self):
        password_id = self.get_argument('id', '')
        password = Password.get_by_pk(password_id)
        if not password:
            return self.finish(
                {'code': RESP['ERROR']['CODE'], 'msg': RESP['ERROR']['MSG']}
                )
        PasswordAsk.remove_by_password(password)
        password.remove()
        return self.finish(
            {'code': RESP['SUCCESS']['CODE'], 'msg': RESP['SUCCESS']['MSG']}
            )

    def post(self):
        request = get_post_json(self.request)
        if (not request):
            return self.finish(
                {'code': RESP['FORBID']['CODE'], 'msg': RESP['FORBID']['MSG']}
                )
        new_password = Password.new(request)
        for ask in request['asks']:
            ask['password'] = new_password
            PasswordAsk.new(ask)

    def options(self):
        return self.finish({'code': RESP['FORBID'], 'msg': RESP['FORBID']['MSG']})
