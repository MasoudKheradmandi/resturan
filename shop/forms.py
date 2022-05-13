from django import forms


class ShopForm(forms.Form):
	Fullname = forms.CharField(max_length=300)
	# locations = forms.