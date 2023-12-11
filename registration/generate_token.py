#  generate tokens for all existing users 

from models import UserModel
from rest_framework.authtoken.models import Token

for user in UserModel.objects.all():
    Token.objects.get_or_create(user=user)