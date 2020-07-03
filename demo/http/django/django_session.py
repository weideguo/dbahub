
#settings.py  #设置session的存储格式
#SESSION_ENGINE = 'django.contrib.sessions.backends.file'           # 文件存储session
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'           # 缓存存储session
#SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'      # 数据库+缓存存储session
#SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies' # 加密cookie存储session
#SESSION_ENGINE = 'django.contrib.sessions.backends.db'             # 数据库存储session

MIDDLEWARE += [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',]
    
    
    
    

######################session
from importlib import import_module
from django.conf import settings
engine = import_module(settings.SESSION_ENGINE)
SessionStore = engine.SessionStore

#session_key使用cookie前端的cookie存储
session_key="k1jk1qyguptrufpzdk6oc9ayu7wadb2c"
x=SessionStore(session_key) 

#request.session=x
#session所存储的信息
x.items()



####################auth
from django.utils.module_loading import import_string
#from django.contrib.auth import load_backend
def load_backend(path):
    return import_string(path)()


import hmac
from django.utils.encoding import force_bytes
def constant_time_compare(val1, val2):
    """Return True if the two strings are equal, False otherwise."""
    return hmac.compare_digest(force_bytes(val1), force_bytes(val2))
    
    

SESSION_KEY = '_auth_user_id'
BACKEND_SESSION_KEY = '_auth_user_backend'
HASH_SESSION_KEY = '_auth_user_hash'

def get_user(request):
    """
    Return the user model instance associated with the given request session.
    If no user is retrieved, return an instance of `AnonymousUser`.
    """
    from .models import AnonymousUser
    user = None
    try:
        user_mode = django_apps.get_model(settings.AUTH_USER_MODEL, require_ready=False)
        user_id = user_mode._meta.pk.to_python(request.session[SESSION_KEY])
        backend_path = request.session[BACKEND_SESSION_KEY]
    except KeyError:
        pass
    else:
        if backend_path in settings.AUTHENTICATION_BACKENDS:
            backend = load_backend(backend_path)
            user = backend.get_user(user_id)
            # Verify the session
            if hasattr(user, 'get_session_auth_hash'):
                session_hash = request.session.get(HASH_SESSION_KEY)
                session_hash_verified = session_hash and constant_time_compare(
                    session_hash,
                    user.get_session_auth_hash()
                )
                if not session_hash_verified:
                    request.session.flush()
                    user = None

    return user or AnonymousUser()


 
from django.utils.functional import SimpleLazyObject
user = SimpleLazyObject(lambda: get_user(request))





