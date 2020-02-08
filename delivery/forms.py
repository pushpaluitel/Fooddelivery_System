from django import forms
from delivery.models import Customer

class customerform(forms.ModelForm):
	class Meta:
		model = Customer
		fields = "__all__"
		
class menuform(forms.ModelForm):
	Image = forms.ImageField()
	class Meta:
		model = Customer
		fields = "__all__"