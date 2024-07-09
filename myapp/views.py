from django.http import HttpResponse
from django.shortcuts import render
import datetime
import random
from .models import User
from .forms import UserForm
from django.contrib import messages


def home(request):
    # Generate dynamic data
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%B %d, %Y")

    quotes = [
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "It does not matter how slowly you go as long as you do not stop. - Confucius",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln"
    ]
    random_quote = random.choice(quotes)

    # Retrieve user data from database
    users = User.objects.all()
    


    # Handle form submission
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            user = User(name=name, email=email)
            user.save()
            messages.success(request, f'Thank you, {name}! Your email {email} has been submitted.')
            form = UserForm()
    else:
        form = UserForm()


    # Pass dynamic data to template
    context = {
        'current_time': current_time,
        'current_date': current_date,
        'random_quote': random_quote,
        'form': form,
        'users': users,
    }

    return render(request, 'index.html', context)

