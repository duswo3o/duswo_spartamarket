from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ("nickname",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        # fields = "__all__"
        fields = ["nickname",
                  'first_name',
                  'last_name',
                  'email',
                  ]
        # exclude = ()