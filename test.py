# import json
# from jose import jwt, jwe
# from jose.constants import ALGORITHMS
#
#
# secret = "95f2e972ded27544d5c11c8f8ab4047e"
#
# name = input("Name: ")
#
# payload = {"name": name}
#
# jwt_token = jwt.encode(payload, secret, algorithm=ALGORITHMS.HS256)
#
# print(jwt_token)
#
# print("\n", secret.encode('utf-8'))
#
# jwe_token = jwe.encrypt(json.dumps(payload), secret.encode('utf-8'), algorithm=ALGORITHMS.DIR, encryption=ALGORITHMS.A256GCM)
#
# print("\n", jwe_token.decode('utf-8'))

from litera import ltest


ltest()