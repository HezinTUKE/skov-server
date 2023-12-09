from django.db import models

from items_list.models import Item
from registration.models import UserModel

class Like(models.Model) :
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=False)
