from django.db import models

# Create your models here.
class Register(models.Model):

	user = models.CharField(max_length=50)
	mail = models.CharField(max_length = 50)
	phonenumber = models.IntegerField()
	password = models.CharField(max_length = 50)
	picture = models.FileField(upload_to='/static/pictures')
	
	class Meta:
		db_table = "register"

