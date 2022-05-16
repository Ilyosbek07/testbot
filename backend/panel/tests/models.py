import os
from uuid import uuid4

from django.core.validators import FileExtensionValidator
from django.db import models


def filename_tests(instance, filename):
    try:
        test_id = Tests.objects.latest('id')
        f = uuid4().hex + f'.{filename.split(".")[1]}'
        path = f"files/tests/{test_id.id}"
    except Tests.DoesNotExist:
        f = f'1.{filename.split(".")[1]}'
        path = f"files/tests"
    return os.path.join(path, f)


def filename_keys(instance, filename):
    try:
        test_id = Tests.objects.latest('id')
        f = uuid4().hex + f'.{filename.split(".")[1]}'
        path = f"files/keys/{test_id.id}"
    except Tests.DoesNotExist:
        f = f'1.{filename.split(".")[1]}'
        path = f"files/keys"

    return os.path.join(path, f)


class Language(models.Model):

    class Meta:
        verbose_name = " Bot tili "
        verbose_name_plural = " Bot tillari "

    id = models.AutoField(primary_key=True)
    language_name = models.CharField(max_length=30, null=False, verbose_name="Til nomi")
    language_code = models.CharField(max_length=5, null=False, verbose_name="Til codi")

    def __str__(self):
        return self.language_name


class User(models.Model):

    class Meta:
        verbose_name = " Foydalanuvchi "
        verbose_name_plural = " Foydalanuvchilar "

    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(unique=True, verbose_name="User ID")
    name = models.CharField(max_length=100, verbose_name="Foydalanuvchi ismi")
    language = models.ForeignKey(Language, on_delete=models.PROTECT, verbose_name="Foydalanuvchi tili")
    is_active = models.BooleanField(default=True, verbose_name="Foydalanuvchi faol")

    def __str__(self):
        return self.name


class Tests(models.Model):

    class Meta:
        verbose_name = " Test "
        verbose_name_plural = " Testlar "

    id = models.AutoField(primary_key=True)
    language = models.ForeignKey(Language, on_delete=models.PROTECT, null=False, verbose_name="Test tili")
    directions = models.ForeignKey('Direction', on_delete=models.PROTECT, null=False, verbose_name="Yo'nalish")
    price = models.DecimalField(verbose_name="Narxi", decimal_places=2, max_digits=8, default=0.00)

    def __str__(self):
        return self.directions.direction_name


class Subjects(models.Model):

    class Meta:
        verbose_name = " Fan "
        verbose_name_plural = " Fanlar "

    id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=60, verbose_name="Fan nomi", null=False)

    def __str__(self):
        return self.subject_name


class Direction(models.Model):

    class Meta:
        verbose_name = " OTM yo'nalishi "
        verbose_name_plural = " OTM yo'nalishlari "

    id = models.AutoField(primary_key=True)
    direction_name = models.CharField(max_length=60, verbose_name="Yo'nalish nomi", null=False)

    def __str__(self):
        return self.direction_name


class DirectionSubjects(models.Model):

    class Meta:
        verbose_name = " Fanlar majmuasi "
        verbose_name_plural = " Fanlar majmuasi "

    id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(Subjects, on_delete=models.PROTECT, verbose_name="Fan nomi")
    file = models.FileField(
        verbose_name="Test fayli",
        null=False,
        validators=[FileExtensionValidator(['pdf', 'docx', 'doc'])],
        upload_to=filename_tests
    )
    keys = models.FileField(
        verbose_name="Javoblar",
        null=False,
        validators=[FileExtensionValidator(['xlsx'])],
        upload_to=filename_keys
    )
    test = models.ForeignKey(Tests, on_delete=models.PROTECT, null=False, verbose_name="Test")

    def __str__(self):
        return self.test.directions.direction_name


class SelectedTest(models.Model):

    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField()
    test_id = models.BigIntegerField(null=True)


class SelectedAnswers(models.Model):

    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(null=False)
    subject_id = models.BigIntegerField(null=False)
    right_answers = models.IntegerField(null=False)
    wrong_answers = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now=True)

