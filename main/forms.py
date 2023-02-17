from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = [
#             'text',
#         ]
#
#     def clean(self):
#         cleaned_data = super().clean()
#         return cleaned_data
