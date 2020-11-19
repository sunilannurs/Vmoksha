from django.shortcuts import render
from django.http import JsonResponse
from .models import *


def get_states(request):
    states = list(PState.objects.filter(country_id=request.GET['country_id']).values('state_id', 'state'))
    return JsonResponse({'states': states}, safe=False)


def get_cities(request):
    cities = list(PCity.objects.filter(state_id=request.GET['state_id']).values('city_id', 'city'))
    return JsonResponse({'cities': cities}, safe=False)


def get_locations(request):
    print("location")
    # print("loosdafasd",PLocation.object)
    location = list(PLocation.objects.filter(city_id=request.GET['city_id']).values('location_id', 'location'))
    return JsonResponse({'location': location}, safe=False)


from django.contrib import messages


def preferencee(request):
    if request.method == "POST":
        country_n = PCountry.objects.get(country_id=request.POST['country'])
        city_n = PCity.objects.get(city_id=request.POST['city'])
        location_n = PLocation.objects.get(location_id=request.POST['location'])
        preference_id = MyPreference.objects.all().last()
        preference = MyPreference()
        preference.id = int(preference_id.id + 1)
        preference.country = country_n.country
        preference.city = city_n.city
        preference.location = location_n.location
        messages.success(request, 'Thank you, Your Preference is Stored Successfully')

        preference.save()

    country = PCountry.objects.all()

    context = {
        'country': country,

    }
    return render(request, 'vmoksha/vmoksha.html', context)
