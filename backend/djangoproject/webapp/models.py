from django.db import models
from .utils import AvatarTypes
# Create your models here.
class login(models.Model):
    username = models.CharField(max_length=10, unique=True)
    #avatar = models.IntegerField() #Imagem relacionada (avatar1)
    avatar = models.IntegerField(choices=AvatarTypes.choices(), default=AvatarTypes.MENINA_NEGRA)

    def __str__(self):
        return self.username

    def get_avatar_type_label(self):
        return AvatarTypes(self.avatar).name.title()