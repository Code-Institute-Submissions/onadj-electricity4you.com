from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'author', 'body')
		widgets = {
		'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Give Your Post Name'}),
        'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder', 'type': 'hidden'}),
		'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Write Your Post"}),
		}

class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'body')
		widgets = {
		'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name Of Post'}),
		# 'author': forms.Select(attrs={'class': 'form-control','placeholder':'choices'}),
		'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Body"}),
		}
