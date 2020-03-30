from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm
from django.views import generic
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView,UpdateView,DeleteView


class UserFormView(View):
    form_class=UserForm
    template_name='user/registration_form.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            email=form.cleaned_data['email']
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            if not email.endswith('@iitd.ac.in'):
                return redirect('/User/register/')
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user=authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('/professor/')

        return render(request,self.template_name,{'form':form})



'''
class UserUpdate(UpdateView):
    model=User
    fiels=['first_name','last_name','username']
    template_name_suffix = '_update_form'
'''
