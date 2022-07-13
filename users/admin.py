# # https://swarf00.github.io/2018/12/07/registration.html

# # from django.contrib import admin
# # from .models import User

# from django.contrib.auth import get_user_model
# from django.contrib import admin

# @admin.register(get_user_model())
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['email','nickname','joined_at']
#     list_display_links = ('nickname', 'email')
#     exclue = ('password',)


#     def joined_at(self, obj):
#         return obj.created_at.strftime("%Y-%m-%d")
#     joined_at.admin_order_field = '-joined_at'      # 가장 최근에 가입한 사람부터 리스팅
#     joined_at.short_description = '가입일'
