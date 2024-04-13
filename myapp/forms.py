from django import forms
from .models import Trn_entry
from .models import Unsd_entry
from .models import Sop_master
from .models import atteninfo
from .models import device_logs
from .models import devicelist



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

class atteninfoForm(forms.ModelForm):




	# create meta class
	class Meta:
	
		# specify model to be used
		# model = Rgp_entry
		model = atteninfo

		# specify fields to be used
		fields = '__all__'

class device_logsForm(forms.ModelForm):




	# create meta class
	class Meta:
	
		# specify model to be used
		# model = Rgp_entry
		model = device_logs

		# specify fields to be used
		fields = '__all__'

class devicelistForm(forms.ModelForm):




	# create meta class
	class Meta:
	
		# specify model to be used
		# model = Rgp_entry
		model = devicelist

		# specify fields to be used
		fields = '__all__'