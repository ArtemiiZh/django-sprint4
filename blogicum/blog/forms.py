from django import forms
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class PostForm(forms.ModelForm):
    """Форма для создания и редактирования публикаций с картинкой."""
    class Meta:
        model = Post
        exclude = ('author',)
        widgets = {
            'pub_date': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
        }


class CommentForm(forms.ModelForm):
    """Форма для добавления комментариев."""
    class Meta:
        model = Comment
        fields = ('text',)
