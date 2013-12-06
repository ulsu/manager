# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    IMPORTANCE = (
        (0, 'Low'),
        (1, 'Average'),
        (2, 'High'),
    )
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    parent = models.ForeignKey('Task', null=True, blank=True, related_name='children')
    importance = models.IntegerField(choices=IMPORTANCE, verbose_name='Важность')
    pub_date = models.DateTimeField(verbose_name='Дата')
    performers = models.ManyToManyField(User, verbose_name='Исполнители')

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        if self.parent is None:
            return '%s' % self.title
        else:
            return '%s - %s' % (self.parent.title, self.title)