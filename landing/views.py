from django.shortcuts import render, redirect
from .forms import SignupForm  # import your form class

def soon(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('success')  # Redirect after successful POST
    return render(request, 'landing/soon.html', {'form': form})

def success(request):
    return render(request, 'landing/success.html')
