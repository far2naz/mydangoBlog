from django import forms
from . import models

class CreaterArticle(forms.ModelForm):
    class Meta:
        model=models.Article
        fields=['title','slug','body','imagwe','body2','imagwe2']
