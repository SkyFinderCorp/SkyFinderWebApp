from django.shortcuts import render
from django.shortcuts import HttpResponse
import array as arr
from django.shortcuts import render
import requests


def home(request):
    return render(request, "index.html")


def track(request):
    global flight_data
    if request.method == "POST":
        form_data = request.POST

        air_line = form_data['airline']
        flight_number = form_data['flightnumber']

        params = {
            'access_key': 'a58ff3a85e378dc08d28d17d9d729ac0',
            'airline_name': air_line,
            'flight_iata': flight_number
        }

        results = requests.get('http://api.aviationstack.com/v1/flights', params=params)

        api_response = results.json()

        for flight in api_response['data']:
            flight_data = [
                flight['airline']['name'],
                flight['flight']['number'],
                flight['flight']['iata'],

                flight['departure']['airport'],
                flight['departure']['iata'],
                flight['departure']['estimated'],
                flight['departure']['gate'],
                flight['departure']['terminal'],

                flight['arrival']['airport'],
                flight['arrival']['iata'],
                flight['arrival']['estimated'],
                flight['arrival']['gate'],
                flight['arrival']['terminal']
            ]

        return render(request, 'track.html', {'flightData': flight_data})
    return render(request, "track.html")


def contact(request):
    return render(request, "contact.html")
