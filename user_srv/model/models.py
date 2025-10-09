from tkinter.font import names

from peewee import *
from user_srv.settings import settings

class BaseModel(Model):
    class Meta:
        database = settings.DB

class User(BaseModel):
    GENDER_CHOICES = (
        (1, "男"),
        (2, "女"),
    )
    ROLE_CHOICES = (
        (1, '普通用户'),
        (2, "管理员")
    )
    mobile = CharField(max_length=11, index=True, unique=True, verbose_name="手机号")
    password = CharField(max_length=100, verbose_name="密码")
    nickname = CharField(max_length=20, verbose_name="昵称", null=True)
    head_url = CharField(max_length=200, verbose_name="头像", null=True)
    birthday = DateField( verbose_name="生日", null=True)
    address = CharField(max_length=200, verbose_name="地址", null=True)
    desc = TextField(verbose_name="个人简介", null=True)
    gender = CharField(verbose_name="性别", null=True, max_length=6, choices=GENDER_CHOICES)
    role = IntegerField(default=1, verbose_name="性别", choices=ROLE_CHOICES)

if __name__ == "__main__":
    import hashlib
    m = hashlib.md5()
    m.update(b"123456")
    print(m.hexdigest())
    # settings.DB.create_tables([User])
