from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.





class UserAdminConfig(admin.ModelAdmin):
    exclude = ['last_name', 'date_joined', 'first_name']
    search_fields = ('email', 'user_name')
    list_filter = ('email', 'user_name', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'user_name','is_active', 'is_staff')
    
    

    
    
    



admin.site.register(NewUser, UserAdminConfig)