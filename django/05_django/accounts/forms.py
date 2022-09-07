from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import User


class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        # 장고에서는 아래처럼 직점 참조를 권하지 않는다
        # model = User
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email',)


class CustomUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)
