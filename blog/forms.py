from django import forms

from .models import Blog


class BlogForm(forms.ModelForm):
    def clean_title(self):
        title = self.cleaned_data.get('title')
        
        if len(title) < 4:
            raise forms.ValidationError('Title must be at least 4 characters long')
        
        return title
    
    class Meta:
        model = Blog
        fields = ('title', 'body')