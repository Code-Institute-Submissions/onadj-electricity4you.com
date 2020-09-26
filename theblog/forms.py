from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'author', 'category', 'body')
		widgets = {
		'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name of Post'}),
		'author': forms.Select(attrs={'class': 'form-control'}),
        'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
		'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Body"}),
		}


class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','body')
		widgets = {
		'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name Of Post'}),
		'author': forms.Select(attrs={'class': 'form-control','placeholder':'choices'}),
		'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Body"}),
		}