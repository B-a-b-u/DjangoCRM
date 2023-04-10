from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class NewUserForm(UserCreationForm):
    
    fname = forms.CharField(label="",widget = forms.TextInput(attrs={"class":"form-fname","placeholder":"first name"}), max_length=30 ,required=True) 
    lname = forms.CharField(label="",widget = forms.TextInput(attrs={"class":"form-lname","placeholder":"last name"}), max_length=30, required=True)
    email = forms.EmailField(label="",widget = forms.TextInput(attrs={"class":"form-email","placeholder":"Email"}), required=True)

    class Meta:
        model = User
        fields = ("username","fname","lname","email","password1","password2")

    def __init__(self,*args,**kwargs):
        super(NewUserForm,self).__init__(*args,**kwargs)

        # Username 
        self.fields["username"].widget.attrs["class"] = "form-uname"     # setting class name
        self.fields["username"].widget.attrs["placeholder"] = "UserName"      # setting placeholder
        self.fields["username"].label = "UserName"              # setting label
        self.fields["username"].help_text = "<p>Username should be unique</p>"     # setting help-txt

        #   password
        self.fields["password1"].widget.attrs["class"] = "form-pswd1"     # setting class name
        self.fields["password1"].widget.attrs["placeholder"] = "Password"      # setting placeholder
        self.fields["password1"].label = ""              # setting label
        self.fields["password1"].help_text = "<p>Password should have atleast 8 characters</p>"     # setting help-txt

        #     Confirm password
        self.fields["password2"].widget.attrs["class"] = "form-pswd2"     # setting class name
        self.fields["password2"].widget.attrs["placeholder"] = "Password"      # setting placeholder
        self.fields["password2"].label = ""              # setting label
        self.fields["password2"].help_text = "<p>Password should have atleast 8 characters</p>"     # setting help-txt