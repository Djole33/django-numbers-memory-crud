from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from random import shuffle
import logging
from random import randint

logger = logging.getLogger(__name__)

# Create your views here.

def home(request):
    if 'number' in request.session:
        del request.session['number']
    return render(request, 'index.html')

def generate_number_with_digits(num_digits: int) -> int:
    if num_digits == 1:
        return randint(1, 9)
    else:
        return randint(10**(num_digits - 1), 10**num_digits - 1)

def numbers_view(request: HttpRequest) -> HttpResponse:
    # Check if 'number' is already in the session
    if 'number' not in request.session:
        # Generate a random number with a random number of digits (from 1 to 30)
        num_digits = randint(1, 30)
        number = generate_number_with_digits(num_digits)
        
        # Store the generated number in the session
        request.session['number'] = number

    # Retrieve the number from the session
    number = request.session['number']
    
    # Render the 'numbers-list.html' template with the 'number' context
    return render(request, 'numbers-list.html', {"number": number})
