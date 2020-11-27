from django import forms
from .models import PostDetails

class newCommentForm(forms.ModelForm):

	class Meta:
		model = PostDetails
		fields = ['comment']