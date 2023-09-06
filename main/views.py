from django.shortcuts import render, redirect
from .forms import OrderForm, FeedbackForm
from .models import Feedback

# Create your views here.

def index(request):
    return render(request,"main/index.html")

def about(request):
    return render(request,'main/my-site/about.html')

def contact_us(request):
    print(f"\ncontact_us \n {request}")
    form = OrderForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {
        'form':form
    }

    return render(request,"main/my-site/contact_us.html",context)

def reviews(request):
    print(f"\nreviews \n {request}")
    form = FeedbackForm(request.POST)
    last_three_feedback = Feedback.objects.all().order_by('-id')[:3]
    if request.method == "POST":
        #print(form.data)
        if form.is_valid():
            form.save()
            last_three_feedback = Feedback.objects.all().order_by('-id')[:3]
            return redirect("home")
    
    context = {
        'form':form,
        'feedback1':last_three_feedback[2],
        'feedback2':last_three_feedback[1],
        'feedback3':last_three_feedback[0]
    }
    return render(request,"main/my-site/reviews.html",context)

