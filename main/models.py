# -*- coding: utf-8 -*-
from django.db import models

class Task(models.Model):
    IMPORTANCE = (
        (0, 'Low'),
        (1, 'Average'),
        (2, 'High'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    parent = models.ForeignKey('Task', null=True, blank=True, related_name='children')
    importance = models.IntegerField(choices=IMPORTANCE)


    def __unicode__(self):
        return '%s - %s' % (self.parent.title, self.title)