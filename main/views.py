from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from random import shuffle
import logging
from random import randint
from .forms import NumberForm, LevelForm

logger = logging.getLogger(__name__)

# Create your views here.

def home(request):
    if 'number' in request.session:
        del request.session['number']
    if 'guesses' in request.session:
        del request.session['guesses']
    form = LevelForm()
    if request.method == "POST":
        form = LevelForm(request.POST)
        if form.is_valid():
            level = int(form.cleaned_data['level'])
            request.session['level'] = level
            return redirect('/numbers-list')
    
    return render(request, 'index.html', {'form': form})

from random import randint
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def generate_number_with_digits(num_digits: int) -> int:
    if num_digits == 1:
        return randint(1, 9)
    else:
        return randint(10000000000000000000, 99999999999999999999)

def numbers_view(request: HttpRequest) -> HttpResponse:
    # Check if 'number' is already in the session
    if 'number' not in request.session:
        # Generate a random number with a random number of digits (from 2 to 20)
        num_digits = randint(2, 20)
        number = generate_number_with_digits(num_digits)
        
        # Store the generated number in the session
        request.session['number'] = number

    # Get the selected level from the session
    level = request.session.get('level', 1)
    nums_digits = level * 2

    # Retrieve the number from the session
    number = request.session['number']

    # Convert the number to a string to limit the number of digits
    number_str = str(number)[:nums_digits]

    # Convert back to an integer
    number_limited = int(number_str) if number_str else 0

    # Render the 'numbers-list.html' template with the 'number' context
    return render(request, 'numbers-list.html', {"number": number_limited, "level": level})

def guess_view(request: HttpRequest) -> HttpResponse:
    # Use session to store guesses across requests
    if 'guesses' not in request.session:
        request.session['guesses'] = []

    if request.method == "POST":
        form = NumberForm(request.POST)
        if form.is_valid():
            # Append the valid guess to the session list
            guess = form.cleaned_data['guess']
            request.session['guesses'].append(guess)
            request.session.modified = True  # Mark session as modified to save changes
            return redirect('/recall')
    else:
        form = NumberForm()

    # Get the selected level from the session
    level = request.session.get('level', 1)
    nums_digits = level * 2

    # Retrieve guesses from session
    guesses = request.session['guesses']
    
    return render(request, 'recall.html', {'form': form, 'guesses': guesses, 'nums_digits': nums_digits})

def delete_guess(request: HttpRequest) -> HttpResponse:
    # Check if guesses exist in session
    if 'guesses' in request.session and request.session['guesses']:
        # Remove the last guess from the session list
        request.session['guesses'].pop()
        request.session.modified = True  # Mark session as modified to save changes

    return redirect('/recall')

def results(request: HttpRequest) -> HttpResponse:
    # Retrieve the number from the session
    number = request.session['number']

    # Get the selected level from the session
    level = request.session.get('level', 1)
    nums_digits = level * 2

    # Convert the number to a string to limit the number of digits
    number_str = str(number)[:nums_digits]

    # Convert back to an integer
    number_limited = int(number_str) if number_str else 0

    # Check if guesses exist in session
    guesses = request.session.get('guesses', {})
    return render(request, 'results.html', {'guesses': guesses, 'number': number_limited})
