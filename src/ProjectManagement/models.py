# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Project(models.Model):
    projectName = models.CharField(max_length=30)
    projectDescribe=models.TextField()
    is_active = models.BooleanField(
        default=True,
        help_text=(
            'Designates whether this project should be treated as active. '
        ),
    )
    
    def __str__(self):
        return self.projectName