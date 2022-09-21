from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        # 기본 저장 필드: first_name, last_name, username, email
        user = super().save_user(request, user, form, False)
        print(request, user, form, sep='\n')
        
        # 추가 저장 필드
        nickname = data.get("nickname")
        name = data.get("name")
        gender = data.get("gender")
        
        if nickname:
            user.nickname = nickname
        
        if name:
            user.name = name
        
        if gender:
            user.gender = gender

        user.save()
        return user