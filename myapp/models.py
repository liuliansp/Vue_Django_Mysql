from __future__ import unicode_literals
from django.db import models

#SyntaxError: from __future__ imports must occur at the beginning of the file 将from __future__ import unicode_literals放到最前面

# Create your models here.
class Book(models.Model):
    book_name=models.CharField(max_length=64)
    add_time=models.DateField(auto_now_add=True)
    def __unicode__(self):
        return self.book_name