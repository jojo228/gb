from urllib.parse import urlencode
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView
from main.forms import SearchForm
from main.models import *
from django.views.generic import (
    TemplateView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    ListView,
    FormView,
)


# Create your views here.
def coming_soon(request):
    
    return render(request, "coming-soon.html")


def term_condition(request):
    
    return render(request, "term_&_condition.html")


def police_prive(request):
    
    return render(request, "police_prive.html")


def home(request):
    houses = House.objects.all().order_by("-date")[:9]
    cars = Voiture.objects.all().order_by("-date")[:9]
    clothes = Mode.objects.all().order_by("-date")[:9]
    
    return render(request, "index.html", locals())



def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            room_type = form.cleaned_data.get('room_type')
            guests = form.cleaned_data.get('guests')
            when = form.cleaned_data.get('main-input-search')

            # Perform search logic for Room model
            houses = House.objects.all()
            if room_type:
                houses = houses.filter(room_type__name__icontains=room_type)
            if guests:
                houses = houses.filter(guests=guests)
            # Add more filtering logic as needed (e.g., when, check_out)

            

            return render(request, 'search_results.html', {
                'room_type': room_type,
                'houses': houses,
            })

    # If form is invalid or method is not GET
    return render(request, 'search_results.html')



class AnnounceListView(ListView):
    model = House
    paginate_by = 30
    context_object_name = "houses"
    template_name = "house_listing.html"

    def get_queryset(self):
        return House.objects.all().order_by("-date")

    def get_context_data(self, **kwargs):
        context = super(AnnounceListView, self).get_context_data(**kwargs)
        return context
    

class CarListView(ListView):
    model = Voiture
    paginate_by = 30
    context_object_name = "cars"
    template_name = "car_listing.html"

    def get_queryset(self):
        return House.objects.all().order_by("-date")

    def get_context_data(self, **kwargs):
        context = super(CarListView, self).get_context_data(**kwargs)
        return context
    

class ModeListView(ListView):
    model = Mode
    paginate_by = 30
    context_object_name = "modes"
    template_name = "mode_listing.html"

    def get_queryset(self):
        return House.objects.all().order_by("-date")

    def get_context_data(self, **kwargs):
        context = super(ModeListView, self).get_context_data(**kwargs)
        return context


# DETAIL
class HouseDetailView(DetailView):
    model = House
    context_object_name = "house"
    template_name = "house_detail.html"


class CarDetailView(DetailView):
    model = Voiture
    context_object_name = "car"
    template_name = "car_detail.html"


class ModeDetailView(DetailView):
    model = Mode
    context_object_name = "mode"
    template_name = "mode_detail.html"

    

def book_room(request, pk):
    room_url = request.build_absolute_uri(reverse('house_detail', kwargs={'pk': pk}))
    message = f"Salut, je suis intéressé par cet appartement: {room_url}"
    
    # Define the recipient number
    recipient_number = '22879518099'  # Replace with the recipient's phone number
    
    # Construct the WhatsApp URL with recipient number and message
    whatsapp_params = {
        'text': message,
        'phone': recipient_number
    }
    whatsapp_url = f"https://api.whatsapp.com/send?{urlencode(whatsapp_params)}"
    
    return redirect(whatsapp_url)


def book_car(request, pk):
    room_url = request.build_absolute_uri(reverse('car_detail', kwargs={'pk': pk}))
    message = f"Salut, je suis intéressé par cette voiture: {room_url}"
    
    # Define the recipient number
    recipient_number = '22879518099'  # Replace with the recipient's phone number
    
    # Construct the WhatsApp URL with recipient number and message
    whatsapp_params = {
        'text': message,
        'phone': recipient_number
    }
    whatsapp_url = f"https://api.whatsapp.com/send?{urlencode(whatsapp_params)}"
    
    return redirect(whatsapp_url)


def book_mode(request, pk):
    room_url = request.build_absolute_uri(reverse('mode_detail', kwargs={'pk': pk}))
    message = f"Salut, je suis intéressé par cet article: {room_url}"
    
    # Define the recipient number
    recipient_number = '22879518099'  # Replace with the recipient's phone number
    
    # Construct the WhatsApp URL with recipient number and message
    whatsapp_params = {
        'text': message,
        'phone': recipient_number
    }
    whatsapp_url = f"https://api.whatsapp.com/send?{urlencode(whatsapp_params)}"
    
    return redirect(whatsapp_url)


def index2(request):
    
    return render(request, "index2.html")



def index3(request):
    
    return render(request, "index3.html")


def index4(request):
    
    return render(request, "index4.html")




def errorpage(request):
    
    return render(request, "404.html")


def about(request):
    
    return render(request, "about.html")


def contacts(request):
    
    return render(request, "contacts.html")


def invoice(request):
    
    return render(request, "invoice.html")


def authorsingle(request):
    
    return render(request, "author-single.html")


def help(request):
    
    return render(request, "help.html")


def pricingtables(request):
    
    return render(request, "pricing-tables.html")


def bookingsingle(request):
    
    return render(request, "booking-single.html")


def dashboard(request):
    
    return render(request, "dashboard.html")



def blog2(request):
    
    return render(request, "blog2.html")



def blogsingle(request):
    
    return render(request, "blog-single.html")


def dashboardaddlisting(request):
    
    return render(request, "dashboard-add-listing.html")



def blog(request):
    
    return render(request, "blog.html")


def listingsingle(request):
    
    return render(request, "listing-single.html")


def listingsingle2(request):
    
    return render(request, "listing-single2.html")


def listingsingle3(request):
    
    return render(request, "listing-single3.html")


def listingsingle4(request):
    
    return render(request, "listing-single4.html")


def listing(request):
    
    return render(request, "listing.html")


def listing2(request):
    
    return render(request, "listing2.html")


def listing3(request):
    
    return render(request, "listing3.html")


def listing4(request):
    
    return render(request, "listing4.html")


def listing5(request):
    
    return render(request, "listing5.html")


def listing6(request):
    
    return render(request, "listing6.html")


def room1(request):
    
    return render(request, "rooms/room1.html")


def room2(request):
    
    return render(request, "rooms/room2.html")


def room3(request):
    
    return render(request, "rooms/room3.html")

def dashboardaddlisting(request):
    
    return render(request, "dashboard-add-listing.html")


def dashboardlistingtable(request):
    
    return render(request, "dashboard-listing-table.html")


def dashboardpassword(request):
    
    return render(request, "dashboard-password.html")


def dashboardreview(request):
    
    return render(request, "dashboard-review.html")




