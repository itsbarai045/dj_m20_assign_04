from django.shortcuts import redirect, render
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from . import forms, models


# Create your views here.
def home_view(request):
    query = request.GET.get('search')
    print(request.user.is_superuser)
   
    if query:
        events =models.Event.objects.filter(name__icontains=query) | models.Event.objects.filter(date__icontains=query) | models.Event.objects.filter(location__icontains=query) 
        events = events.distinct()
    else:
        events = models.Event.objects.all()
        
    for x in events:
       
        x.date=f"{x.date.day}/{x.date.month}/{x.date.year}"
        attend = models.Participant.objects.filter(event=x).count()
        if attend == x.limit:
            x.status = "Fully Booked"
        elif attend < x.limit and attend > 0 :
            x.status = "Partially Booked"
        elif attend == 0:
            x.status = "No One Booked Yet"

        if request.user.is_authenticated:
            is_booked = models.Participant.objects.filter(event=x, member=request.user)
            if is_booked:
                x.booked = True
            else:
                x.booked = False

    context = {
        'events': events
    }
    template_name = "event/home.html"
    return render(request, template_name, context)


@login_required
def booked_event_view(request):
    booked_events = []
    
    participants = models.Participant.objects.filter(member=request.user)
    for x in participants:
        booked_events.append(x.event)

    for x in booked_events:
       
        x.date=f"{x.date.day}/{x.date.month}/{x.date.year}"
        attend = models.Participant.objects.filter(event=x).count()
        if attend == x.limit:
            x.status = "Fully Booked"
        elif attend < x.limit and attend > 0 :
            x.status = "Partially Booked"
        elif attend == 0:
            x.status = "No One Booked Yet"

        if request.user.is_authenticated:
            is_booked = models.Participant.objects.filter(event=x, member=request.user)
            if is_booked:
                x.booked = True
            else:
                x.booked = False

    context = {
        'events': booked_events
    }
    template_name = "event/booked_event.html"
    return render(request, template_name, context)


@login_required
def add_event_view(request):

    if request.method =="POST":
        form = forms.EventForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return redirect('home')
    else:
        form = forms.EventForm()

    context = {
        "form": form,
        'text' : "Add"
    }
    template_name = "event/event_form.html"
    
    return render(request, template_name, context)



def view_event_view(request, pk):
    event = models.Event.objects.get(pk=pk)
    participants = models.Participant.objects.filter(event=event)
    
    
    attend = models.Participant.objects.filter(event=event).count()
    if attend == event.limit:
        event.status = "Fully Booked"
    elif attend < event.limit and attend > 0 :
        event.status = "Partially Booked"
    elif attend == 0:
        event.status = "No One Booked Yet"
    booked = False
    if request.user.is_authenticated:
        is_participant = models.Participant.objects.filter(event=event, member=request.user)
        if is_participant:
            booked = True
        else:
            booked = False

    context = {
        "event": event,
        "participants": participants,
        'booked': booked
    }
    template_name = "event/event_view.html"
    
    return render(request, template_name, context)


@login_required
def delete_event_view(request, pk):
    event = models.Event.objects.get(pk=pk)
    if request.method == "POST":
        event.delete() 
        return redirect('home')   

    context = {
        "event": event
    }
    template_name = "event/event_delete.html"
    
    return render(request, template_name, context)


@login_required
def book_event_view(request, pk):
    template_name = "event/event_book.html"
    event = models.Event.objects.get(pk=pk)
    
    # booked = models.Participant.objects.filter(member=request.user)
    # if booked is not None:
    #     template_name = "event/event_booked.html"

    if request.method == "POST":
        models.Participant.objects.create(event=event, member=request.user)
        return redirect('home')   

    context = {
        "event": event
    }
        
    return render(request, template_name, context)


@login_required
def update_event_view(request, pk):
    event = models.Event.objects.get(pk=pk)
    if request.method =="POST":
        form = forms.EventForm(request.POST, instance=event)
        if form.is_valid():
            form = form.save(commit=False)
            form.owner = request.user
            form.save()
            return redirect('view_event', pk)
    else:
        form = forms.EventForm(instance=event)

    context = {
        "form": form,
        'text' : "Update"
    }
    template_name = "event/event_form.html"
    
    return render(request, template_name, context)


@login_required
def category_view(request):
    categories = models.Category.objects.all()
    context = {
        'categories':categories
    }
    template_name = "event/category.html"
    return render(request, template_name, context)



@login_required
def add_category_view(request):

    if request.method =="POST":
        form = forms.CategoryForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('category')
    else:
        form = forms.CategoryForm()

    context = {
        "form": form
    }
    template_name = "event/category_form.html"
    return render(request, template_name, context)



@login_required
def update_category_view(request, pk):

    category = models.Category.objects.get(pk=pk)
    if request.method =="POST":
        form = forms.CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('category')
    else:
        form = forms.CategoryForm(instance=category)

    context = {
        "form": form
    }
    template_name = "event/category_form.html"
    return render(request, template_name, context)





