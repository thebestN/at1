from django.test import TestCase

# Create your tests here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Question(models.Model):
    English_text = models.CharField(max_length=200)
    Morse_text = models.TextField()

    def __str__(self):
        return self.English_text