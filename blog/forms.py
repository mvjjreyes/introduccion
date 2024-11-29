from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'border-2 border-gray-300 rounded-md p-2 w-full', 'placeholder': 'Introduce el título'}),
            'content': forms.Textarea(attrs={'class': 'border-2 border-gray-300 rounded-md p-2 w-full h-32', 'placeholder': 'Introduce el contenido'}),
        }