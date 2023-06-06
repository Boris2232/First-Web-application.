from django.shortcuts import render, redirect
from regform.models import People


def regform(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']
        second_password = request.POST['second_pass']
        Logged_in = (password == second_password) and (len(username) != 0 and len(password) != 0 and len(
            second_password) != 0)
        if Logged_in:
            new_user = People(username=username, password=password)
            new_user.save()
            return redirect('login/')
        else:
            pass
    return render(request, 'regform.html')
