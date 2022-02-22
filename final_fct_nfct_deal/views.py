from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import *
from .models import *

def final_deal(request):
    form = FinalFctNfctDealDetails(request.POST or None)
    