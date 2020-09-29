from django import forms
from .models import Post, Category, Comment

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

        'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder', 'type': 'hidden'}),

		# 'author': forms.Select(attrs={'class': 'form-control'}),
        'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
		'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Enter Your Post Here"}),
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


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name','body')
		widgets = {
		'name': forms.TextInput(attrs={'class': 'form-control'}),
		'body': forms.Textarea(attrs={'class': 'form-control'}),
		}