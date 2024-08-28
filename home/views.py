from django.shortcuts import redirect, HttpResponse, render
from .forms import ContactForm , AffilateForm , BuilderForm , DetailsForm , CareerForm
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        form = AffilateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been submitted successfully!')
            # return redirect('contactus')  # Redirect to the same page or another page after successful submission
    else:
        form = AffilateForm()
    return render(request,"index.html")

def home(request):
   if request.method == 'POST':
        form = AffilateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been submitted successfully!')
            # return redirect('contactus')  # Redirect to the same page or another page after successful submission
   else:
        form = AffilateForm()
   return render(request,"index.html")

def about(request):
   return render(request,"about-us.html")

def whyus(request):
   return render(request,"whychooseus.html")

def Ourteam(request):
   return render(request,"our-team.html")

def Service(request):
   return render(request,"our-services.html")   

def carrers(request):
   if request.method == 'POST':
        form = CareerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your application was submitted successfully!')
            # return redirect('apply_for_job')  # Replace 'apply_for_job' with the correct URL name for your view
        else:
            messages.error(request, 'Something went wrong, please try again.')
   else:
        form = CareerForm()
   return render(request,"careers.html")   

# def contactus(request):
#    return render(request,"contact-us.html")



def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message was sent successfully! We will be in touch as soon as we can.')
            # return redirect('contactus')  # Redirect to the same page or another one
        else:
            messages.error(request, 'Something went wrong, please try again.')
    else:
        form = ContactForm()
    
    return render(request, "contact-us.html", {'form': form})

def builder(request):
    if request.method == 'POST':
        form = BuilderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message was sent successfully!')
        else:
            messages.error(request, 'Something went wrong, please try again.')
    else:
        form = BuilderForm()
    
    return render(request,"builder.html")

def buyer(request):
   return render(request,"buyer.html")

def broker(request):
   if request.method == 'POST':
        form = DetailsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message was sent successfully! We will be in touch as soon as we can.')
        else:
            messages.error(request, 'Something went wrong, please try again.')
        # return redirect('contact')  # Adjust the redirect as per your URL configuration
   else:
        form = DetailsForm()

   return render(request,"broker.html")   

def experia(request):
   return render(request,"experia.html")

def thebridge(request):
   return render(request,"the-bridge.html")
