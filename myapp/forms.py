from django import forms
from .models import Trn_entry
from .models import Unsd_entry
from .models import Sop_master



# creating a form
class Trn_entryForm(forms.ModelForm):




	# create meta class
	class Meta:
	
		# specify model to be used
		model = Trn_entry
		# model = Unsd_entry

		# specify fields to be used
		fields = '__all__'

class Unsd_entryForm(forms.ModelForm):




	# create meta class
	class Meta:
	
		# specify model to be used
		# model = Rgp_entry
		model = Unsd_entry

		# specify fields to be used
		fields = '__all__'

class Sop_masterForm(forms.ModelForm):




	# create meta class
	class Meta:
	
		# specify model to be used
		# model = Rgp_entry
		model = Sop_master

		# specify fields to be used
		fields = '__all__'