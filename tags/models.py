from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_tags(text):
    tags = text.split(',')
    for tag in tags:
        tag = tag.strip()
        if ' ' in tag:
            raise ValidationError(_('"%(tag)s" is not a valid tag'), params={'tag': tag})


class Tag(models.Model):
    term = models.CharField(max_length=255)
    tags = models.TextField(blank=True, validators=[validate_tags])

    class Meta:
        ordering = ["-id"]

    def get_absolute_url(self):
        return reverse('tags:root')

    def __str__(self):
        return self.term



