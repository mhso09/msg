from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class User(AbstractUser):
    REGION_CHOICES = [
        ('seoul', '서울'),
        ('gwangju', '광주'),
        ('daegu', '대구'),
        ('daejeon', '대전'),
        ('busan', '부산'),
        ('ulsan', '울산'),
        ('incheon', '인천'),
        ('sejong', '세종'),
        ('gyeonggi', '경기'),
        ('gangwon', '강원'),
        ('chungbuk', '충북'),
        ('chungnam', '충남'),
        ('gyeongbuk', '경북'),
        ('gyeongnam', '경남'),
        ('jeonbuk', '전북'),
        ('jeonnam', '전남'),
        ('jeju', '제주'),
    ]

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'None'),
    ]

    name = models.CharField(_('이름'), max_length=255)
    user_name = models.CharField(_('유저이름'),max_length=255)
    profile_photo = models.ImageField(blank=True)
    email = models.CharField(blank=True, max_length=255)
    phone_number = models.CharField(blank=True, max_length=255)
    gender = models.CharField(
        blank=True, max_length=255, choices=GENDER_CHOICES)
    region = models.CharField(
        blank=True, max_length=255, choices=REGION_CHOICES)

    class Meta:
        db_table = 'Users_user'
