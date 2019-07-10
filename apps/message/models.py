# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class UserMessage(models.Model):
    ob_id = models.CharField(max_length=10,default="",primary_key=True, verbose_name=u'主键')
    Name = models.CharField(max_length=20,verbose_name=u'用户名')
    Email = models.EmailField(verbose_name=u'邮箱名')
    Adress = models.CharField(max_length=50,verbose_name=u'联系地址')
    Message = models.CharField(max_length=200,verbose_name=u'留言信息')

    class Meta:
        verbose_name = u'用户留言信息'
        verbose_name_plural=verbose_name