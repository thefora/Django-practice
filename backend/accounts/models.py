from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    # 일반 user 생성
    def create_user(self, email, nickname, name, password=None):
        if not email:
            raise ValueError('must have email')
        if not nickname:
            raise ValueError('must have nickname')
        if not name:
            raise ValueError('must have name')
        user = self.model(
            email = self.normalize_email(email),
            nickname = nickname,
            name = name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 user 생성
    def create_superuser(self, email, nickname, name, password=None):
        user = self.create_user(
            email,
            password = password,
            nickname = nickname,
            name = name
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    gender_choices=(
        ('male', "남성"),
        ('female', '여성')
    )
    
    id = models.AutoField(primary_key=True)
    email = models.EmailField(default='', max_length=100, null=False, blank=False, unique=True, verbose_name="이메일")
    nickname = models.CharField(default='', max_length=100, null=False, blank=False, unique=True, verbose_name="닉네임")
    name = models.CharField(default='', max_length=100, null=False, blank=False, verbose_name="이름")
    gender = models.CharField(null=False, choices=gender_choices, max_length=20, verbose_name="성별")
    
    # User 모델의 필수 field
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)
    
    # 헬퍼 클래스 사용
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname', 'name']

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
            return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin

    