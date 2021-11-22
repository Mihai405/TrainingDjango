import jwt
from apps.users.models import User
from rest_framework import exceptions

def decode_session_user(request):
    token = request.session.get('user', None)
    if not token:
        raise exceptions.AuthenticationFailed('No such user')
    decode_token = jwt.decode(token, 'secret', algorithms=["HS256"])
    user = User.objects.get(id=decode_token['id'])
    return user

def encode_session_user(request,id):
    payload = {
        'id':id,
    }
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    request.session["user"]=token
    return token

def delete_session_user(request):
    request.session.flush()