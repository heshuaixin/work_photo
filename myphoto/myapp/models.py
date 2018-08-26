from django.db import models
from datetime import datetime
# Create your models here.
# model配置，链接数据库
class Myphotos(models.Model):
	# id = models.AutoField()    自增主键可以省略不写
	title = models.CharField(max_length=32)
	name = models.CharField(max_length=32)
	addtime=models.DateTimeField(default=datetime.now)

	class Meta(object):
		"""指定真实表名"""
		db_table = "myphotos"

			