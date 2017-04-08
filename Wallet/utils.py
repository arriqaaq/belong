import hashlib
import time
import random
import string

from django.contrib.auth.models import User
from django.contrib import auth

from constants import RESPONSE_CODE_INVALID_SESSION, RESPONSE_STRING_INVALID_SESSION, RESPONSE_JSON_TYPE

def unique_id_generator():
    """
    Generates a universally unique ID.
    Any arguments only create more randomness.
    """
    t = long( time.time() * 1000 )
    r = long( random.random()*100000000000000000L )
    a = random.random()*100000000000000000L
    data = str(t)+' '+str(r)+' '+str(a)
    data = hashlib.md5(data).hexdigest()
    return data



class decorator_4xx(object):

    def __init__(self, request_method_list, reqd_params):

        self.request_method_list = request_method_list
        self.reqd_params = reqd_params
        

    def get_all_params(self, request):

        params_dict = dict()

        if request.method == 'GET':
            params_dict = request.GET

        elif request.method == 'POST':
            params_dict = request.POST

    '''Authenticates session token coming in request body and validates 
    whether the token is active or not. If not active 
    returns  Http status 401'''

    def authenticate_token(self, token):
        token = Token.objects.get(token = token)
        if not token:
            return False, RESPONSE_CODE_SESSION_EXPIRED, \
                                RESPONSE_STRING_SESSION_EXPIRED 
        return  True, None, None     


    '''Makes the decorator callable by view.'''

    def __call__(self, func, *args, **kwargs):

        '''Makes the passed view function persists its name, docstring
         instead of being overriden by inner function'''
        # @wraps(func, assigned=available_attrs(func))

        def inner(*args, **kwargs):
            
            request = args[1]
            if request.method not in self.request_method_list:
                response_text = "Http methods allowed: " + \
                    ",".join(self.request_method_list)
                return HttpResponseNotAllowed(response_text)

            params_dict = self.get_all_params(request)

            '''Checks all required parametes are present or not,
            if not return 400 HTTP bad request'''

            is_valid = reduce(operator.and_, ((
                True if param in params_dict else False) for param in self.reqd_params))

            if not is_valid:
                missing_params = filter(lambda param: (
                    param if param not in params_dict else ''), self.reqd_params)

                response_text = "Parameters missing: " + \
                    ",".join(missing_params)
                return HttpResponseBadRequest(response_text)


            is_active, res_code, res_str = self.authenticate_token(params_dict['token'])


            response= {
                "resCode": res_code,
                "resDet": {},
                "resStr": res_str
                }

            if not is_active or not is_valid:
                return HttpResponse(json.dumps(response), content_type = RESPONSE_JSON_TYPE)

            return func(*args, **kwargs)
        return inner
