from django.forms import ModelForm
from .models import UserDetails


class UserModelForm(ModelForm):
	class Meta():
		model = UserDetails
		fields = "__all__" #['title', 'notes']