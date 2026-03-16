from random import randbytes
import base64

DOMAIN = "edu.t-lem.com/?forget={byte_key}"

def password_recovery():
    domain_key = base64.urlsafe_b64encode(randbytes(32)).decode()
    byte_key2 = randbytes(16).hex()
    
    return DOMAIN.format(byte_key=domain_key), byte_key2