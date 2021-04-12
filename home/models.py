from django.db import models
from django.utils import timezone
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=16)
    message = models.TextField()
    services = models.CharField(max_length=50, default='Unchosen')
    date = models.DateField()
    comments = models.TextField(default='')

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    fullname = models.CharField(max_length=122)
    email = models.CharField(max_length=122)

    def __str__(self):
        return self.fullname

# Adding CVerify


class CVerify(models.Model):
    verify_code = models.CharField(max_length=122)
    name = models.CharField(max_length=122, default="")
    classwork = models.CharField(max_length=122, default="")
    course = models.CharField(max_length=122, default="")
    coursecode = models.CharField(max_length=122, default="")
    start_date = models.DateField(default=timezone.now)
    c_issued_date = models.DateField(default=timezone.now)
    cert_max_marks = models.CharField(max_length=122, default="")
    cert_marks_gained = models.CharField(max_length=122, default="")
    cert_pass_fail = models.CharField(max_length=122, default="")

    def __str__(self):
        return self.verify_code
