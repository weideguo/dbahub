#coding:utf8
#django password的加密方式



from django.conf import settings
from django.utils.module_loading import import_string
"""
settings.PASSWORD_HASHERS=['django.contrib.auth.hashers.PBKDF2PasswordHasher', 'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher', 'django.contrib.auth.hashers.Argon2PasswordHasher', 'django.contrib.auth.hashers.BCryptSHA256PasswordHasher']
"""
PASSWORD_HASHERS = settings.PASSWORD_HASHERS

def get_hashers():
    hashers = []
    for hasher_path in PASSWORD_HASHERS:
        hasher_cls = import_string(hasher_path)
        hasher = hasher_cls()
        hashers.append(hasher)
    return hashers


def make_password(password, salt=None, hasher='default'):
    hasher = get_hashers()[0]
    salt = salt or hasher.salt()
    return hasher.encode(password, salt)

password = make_password(raw_password)





####################################################################################
from django.utils.crypto import get_random_string

class PBKDF2PasswordHasher(BasePasswordHasher):
    """
    Secure password hashing using the PBKDF2 algorithm (recommended)

    Configured to use PBKDF2 + HMAC + SHA256.
    The result is a 64 byte binary string.  Iterations may be changed
    safely but you must rename the algorithm if you change SHA256.
    """
    algorithm = "pbkdf2_sha256"
    iterations = 150000
    digest = hashlib.sha256

    def encode(self, password, salt, iterations=None):
        assert password is not None
        assert salt and '$' not in salt
        iterations = iterations or self.iterations
        hash = pbkdf2(password, salt, iterations, digest=self.digest)
        hash = base64.b64encode(hash).decode('ascii').strip()
        return "%s$%d$%s$%s" % (self.algorithm, iterations, salt, hash)


    def salt(self):
        """Generate a cryptographically secure nonce salt in ASCII."""
        return get_random_string()
        

def get_random_string(length=12,
                      allowed_chars='abcdefghijklmnopqrstuvwxyz'
                                    'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):        
    ''.join(random.choice(allowed_chars) for i in range(length))
        
        
from django.utils.encoding import force_bytes
import hashlib 
 
#Password-Based Key Derivation Function 2
def pbkdf2(password, salt, iterations, dklen=0, digest=None):
    """Return the hash of password using pbkdf2."""
    if digest is None:
        digest = hashlib.sha256
    dklen = dklen or None
    password = force_bytes(password)
    salt = force_bytes(salt)
    return hashlib.pbkdf2_hmac(digest().name, password, salt, iterations, dklen)


####################################################################################

from django.contrib.auth.hashers import make_password, check_password

from django.contrib.auth.hashers import PBKDF2PasswordHasher

PBKDF2PasswordHasher.iterations=150000

password="my_password"
salt=""                                               #任意长度 为空则自动生成
hasher="pbkdf2_sha256"
password_hash=make_password(password,salt,hasher)     #存储于数据库的实际值


check_password(password,password_hash)                #校验

   
