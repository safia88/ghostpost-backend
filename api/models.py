"""
Ghost: Boasts, Roasts
    Boolean if boast or roast
    Charfield for content of post
    integer field for up and down votes
    datetime field for submit time
"""
import random
import string
from django.utils.crypto import get_random_string
from django.db import models


class Post(models.Model):
    is_boast = models.BooleanField(default=True)
    content = models.CharField(max_length=280)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    submit_time = models.DateTimeField(auto_now_add=True, blank=True)
    total_votes = models.IntegerField(default=0)
    secret_key = models.CharField(
        max_length=6,
        blank=True,
        default=get_random_string(6).lower(),
        editable=False
    )

    def __str__(self):
        return self.content

    def total_votes(self):
        return self.up_votes - self.down_votes
