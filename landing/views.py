from django.shortcuts import render, redirect
from .forms import SignupForm

def soon(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('soon')
    return render(request, 'soon.html', {'form': form})
