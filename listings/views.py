from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import LostRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def register_lost(request):
    """
    Django’s login form is returned using the POST method, in which the browser bundles up the
    form data, encodes it for transmission, sends it to the server, and then receives back its response.
    :param request:
    :return:
    """
    if request.method == "POST":
        form = LostRegisterForm(request.POST)  # if post request is received, then a form will be made with that data.
        if form.is_valid():
            form.save()  # ensures that we save the user info to our db.
            return redirect('FRONTEND.html')
    else:
        form = LostRegisterForm()  # Create an instance of the user registration form. blank form.

    return render(request, 'FRONTEND.html', {'form': form})
