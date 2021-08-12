from django.db import models

# Create your models here.
class UserDetails(models.Model):

	title = models.CharField(max_length=100)
	gender = models.CharField(max_length=255)
	notes = models.CharField(max_length=255)

	def __str__(self):
		return self.title

# if __name__ == '__main__':
# 	user_details = UserDetails(title="this is a title", gender="male", notes="this is a note")
# 	print(user_details)