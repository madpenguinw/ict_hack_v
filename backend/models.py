from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from .validators import validate_username


class CustomUserManager(UserManager):

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = User(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        assert extra_fields['is_staff']
        assert extra_fields['is_superuser']
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(
        max_length=254,
        unique=True,
        blank=False,
        null=False
    )
    username = models.CharField(
        validators=(validate_username,),
        max_length=150,
        unique=True,
        blank=False,
        null=False
    )
    phone = models.CharField(
        max_length=20,
        unique=True,
        blank=False,
        null=False
    )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone']

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Student(User):
    # first_name = models.CharField(
    #     verbose_name='Имя',
    #     max_length=50,
    #     blank=False,
    #     unique=False,
    # )
    # last_name = models.CharField(
    #     verbose_name='Фамилия',
    #     max_length=50,
    #     blank=False,
    #     unique=False,
    # )
    patronymic = models.CharField(
        verbose_name='Отчество',
        max_length=50,
        blank=True,
        unique=False,
    )
    education = models.CharField(
        verbose_name='Образование',
        max_length=500,
        blank=False,
        unique=False,
    )
    birth_date = models.DateField(
        verbose_name='Дата рождения',
        max_length=500,
        blank=False,
        unique=False,
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Skill(models.Model):
    skill = models.CharField(
        verbose_name='Скилл',
        max_length=150,
        blank=False,
        unique=False,
    )
    is_hard = models.BooleanField(
        verbose_name='Хард скилл',
        null=False,
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='skill'
    )

    class Meta:
        ordering = ('skill',)
        verbose_name = 'Скилл'
        verbose_name_plural = 'Скиллы'

    def __str__(self):
        return self.skill


class Company(User):
    name = models.CharField(
        verbose_name='Имя',
        max_length=50,
        blank=False,
        unique=False,
    )
    activities = models.CharField(
        verbose_name='Деятельность',
        max_length=500,
        blank=False,
        unique=False,
    )
    address = models.CharField(
        verbose_name='Адрес',
        max_length=500,
        blank=False,
        unique=False,
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Project(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=150,
        blank=False,
        unique=False,
    )
    description = models.CharField(
        verbose_name='Описание',
        max_length=500,
        blank=False,
        unique=False,
    )
    precondition = models.CharField(
        verbose_name='Предпосылки',
        max_length=500,
        blank=False,
        unique=False,
    )
    result = models.CharField(
        verbose_name='Результат',
        max_length=500,
        blank=False,
        unique=False,
    )
    criterias = models.CharField(
        verbose_name='Критерии оценки',
        max_length=500,
        blank=False,
        unique=False,
    )
    host_company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name='Компания',
        related_name='host_company',
        blank=False,
        unique=False,
    )
    # host_student = models.ForeignKey(
    #     Student,
    #     on_delete=models.CASCADE,
    #     related_name='host_student',
    #     blank=True,
    # )

    class Meta:
        ordering = ('title',)
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        # constraints = [
        #     models.UniqueConstraint(
        #         fields=['host_student', 'id'],
        #         name='unique_host_student_for_project'
        #     ),
        #     models.UniqueConstraint(
        #         fields=['host_company', 'id'],
        #         name='unique_host_company_for_project'
        #     )]

    def __str__(self):
        return self.title


class Participants(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='student'
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='project'
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

    def __str__(self):
        msg = f'Студент "{self.student}", проект "{self.project}"'
        return msg
