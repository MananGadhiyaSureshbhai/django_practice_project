from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterform,USerUpadeForm,ProfileUpadateForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def regster(request):
    if request.method == 'POST':
        form = UserRegisterform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your Account Has Been Created! You Are Now Able To Login !!!')
            return redirect('login')
    else:
        form = UserRegisterform()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form=USerUpadeForm(request.POST,instance=request.user)
        p_form=ProfileUpadateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request, f'Your Account Has Been Updated !!!')
            return redirect('profile')
    else:
        u_form=USerUpadeForm(instance=request.user)
        p_form=ProfileUpadateForm(instance=request.user.profile)
    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'users/profile.html',context)
