from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.template.response import TemplateResponse
from django.contrib.admin import helpers
from .models import (
        User,
        Employee,
        Patient,
        Responsible,
        Health_Team
    )


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserCreationForm(UserCreationForm):

    error_message = UserCreationForm.error_messages.update({
        'duplicate_username': 'This username has already been taken.'
    })

    class Meta(UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


@admin.register(User)
class MyUserAdmin(AuthUserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    fieldsets = (
            ('User Profile', {'fields': (('name'), ('gender'),
             ('telephone'), ('birthday'), ('photo'))}),
    ) + AuthUserAdmin.fieldsets
    list_display = ('username', 'has_specialization', 'name', 'is_superuser')
    search_fields = ['name']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj=None):
        fields = super().get_readonly_fields(request, obj)

        # This is the case when obj is already created i.e. it's an edit
        if obj:
            fields += ("user",)

        return fields


@admin.register(Responsible)
class ResponsibleAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj=None):
        fields = super().get_readonly_fields(request, obj)

        # This is the case when obj is already created i.e. it's an edit
        if obj:
            fields += ("user",)

        return fields


@admin.register(Health_Team)
class Health_TeamAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj=None):
        fields = super().get_readonly_fields(request, obj)

        # This is the case when obj is already created i.e. it's an edit
        if obj:
            fields += ("user",)

        return fields


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj=None):
        fields = super().get_readonly_fields(request, obj)

        # This is the case when obj is already created i.e. it's an edit
        if obj:
            fields += ("user",)

        return fields
