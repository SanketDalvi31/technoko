from django.db import models
from django.contrib.auth.models import User

FILTER_COURSES = (
    ('IOT', 'IOT'),
    ('Ethical Hacking', 'Ethical Hacking'),
    ('Augmented Reality', 'Augmented Reality'),
    ('Machine Learning', 'Machine Learning'),
)


# Create your models here.
class Detail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    course = models.CharField(max_length=30, choices=FILTER_COURSES)
    score = models.IntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name + ' - ' + str(self.score)


class IOT(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    q1 = models.IntegerField(default=None, blank=True, null=True)
    q2 = models.IntegerField(default=None, blank=True, null=True)
    q3 = models.IntegerField(default=None, blank=True, null=True)
    q4 = models.IntegerField(default=None, blank=True, null=True)
    q5 = models.IntegerField(default=None, blank=True, null=True)
    q6 = models.IntegerField(default=None, blank=True, null=True)
    q7 = models.IntegerField(default=None, blank=True, null=True)
    q8 = models.IntegerField(default=None, blank=True, null=True)
    q9 = models.IntegerField(default=None, blank=True, null=True)
    q10 = models.IntegerField(default=None, blank=True, null=True)
    score = models.IntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "IOT"

class EH(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    q1 = models.IntegerField(default=None, blank=True, null=True)
    q2 = models.IntegerField(default=None, blank=True, null=True)
    q3 = models.IntegerField(default=None, blank=True, null=True)
    q4 = models.IntegerField(default=None, blank=True, null=True)
    q5 = models.IntegerField(default=None, blank=True, null=True)
    q6 = models.IntegerField(default=None, blank=True, null=True)
    q7 = models.IntegerField(default=None, blank=True, null=True)
    q8 = models.IntegerField(default=None, blank=True, null=True)
    q9 = models.IntegerField(default=None, blank=True, null=True)
    q10 = models.IntegerField(default=None, blank=True, null=True)
    score = models.IntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "EH"


class AR(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    q1 = models.IntegerField(default=None, blank=True, null=True)
    q2 = models.IntegerField(default=None, blank=True, null=True)
    q3 = models.IntegerField(default=None, blank=True, null=True)
    q4 = models.IntegerField(default=None, blank=True, null=True)
    q5 = models.IntegerField(default=None, blank=True, null=True)
    q6 = models.IntegerField(default=None, blank=True, null=True)
    q7 = models.IntegerField(default=None, blank=True, null=True)
    q8 = models.IntegerField(default=None, blank=True, null=True)
    q9 = models.IntegerField(default=None, blank=True, null=True)
    q10 = models.IntegerField(default=None, blank=True, null=True)
    score = models.IntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "AR"


class ML(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    q1 = models.IntegerField(default=None, blank=True, null=True)
    q2 = models.IntegerField(default=None, blank=True, null=True)
    q3 = models.IntegerField(default=None, blank=True, null=True)
    q4 = models.IntegerField(default=None, blank=True, null=True)
    q5 = models.IntegerField(default=None, blank=True, null=True)
    q6 = models.IntegerField(default=None, blank=True, null=True)
    q7 = models.IntegerField(default=None, blank=True, null=True)
    q8 = models.IntegerField(default=None, blank=True, null=True)
    q9 = models.IntegerField(default=None, blank=True, null=True)
    q10 = models.IntegerField(default=None, blank=True, null=True)
    score = models.IntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "ML"


'''class IOT_Q(models.Model):
    quest = models.CharField(max_length=200)
    op1 = models.CharField(max_length=30)
    op2 = models.CharField(max_length=30)
    op3 = models.CharField(max_length=30)
    op4 = models.CharField(max_length=30)
    ans = models.IntegerField(default=None)

    def __str__(self):
        return self.quest'''
