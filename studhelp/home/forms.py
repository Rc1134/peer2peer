from django import forms
from .models import ProfileId

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileId
        fields = ['bio', 'picture', 'git', 'leetcode', 'linkedin']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
        }