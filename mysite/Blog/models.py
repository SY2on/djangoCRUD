from django.db import models


class Page(models.Model):
  title = models.CharField(max_length= 50)
  content = models.TextField()
  dt_created = models.DateField(auto_now=True)

  def __str__(self):
    return self.title