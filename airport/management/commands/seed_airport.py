from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from django.utils import timezone
from airport.models import (
    Airport,
    Route,
    AirplaneType,
    Airplane,
    Crew,
    Flight,
)


class Command(BaseCommand):
    help = "Seed database with initial sample data for airport API"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")

        # 1. Airports
        jfk, _ = Airport.objects.get_or_create(
            name="JFK International Airport", closest_big_city="New York"
        )
        lhr, _ = Airport.objects.get_or_create(
            name="Heathrow Airport", closest_big_city="London"
        )
        cdg, _ = Airport.objects.get_or_create(
            name="Charles de Gaulle Airport", closest_big_city="Paris"
        )

        # 2. Routes
        Route.objects.get_or_create(
            source=jfk, destination=lhr, distance=5585
        )
        Route.objects.get_or_create(
            source=lhr, destination=cdg, distance=344
        )

        # 3. Airplane Types
        boeing_type, _ = AirplaneType.objects.get_or_create(name="Boeing 737")
        airbus_type, _ = AirplaneType.objects.get_or_create(name="Airbus A320")

        # 4. Airplanes
        airplane1, _ = Airplane.objects.get_or_create(
            name="Spirit of New York",
            rows=20,
            seats_in_row=6,
            airplane_type=boeing_type,
        )
        airplane2, _ = Airplane.objects.get_or_create(
            name="European Sky",
            rows=15,
            seats_in_row=4,
            airplane_type=airbus_type,
        )

        # 5. Crew
        crew1, _ = Crew.objects.get_or_create(
            first_name="John", last_name="Doe"
        )
        crew2, _ = Crew.objects.get_or_create(
            first_name="Jane", last_name="Smith"
        )

        # 6. Flights
        route_jfk_lhr = Route.objects.get(source=jfk, destination=lhr)
        route_lhr_cdg = Route.objects.get(source=lhr, destination=cdg)

        now = timezone.now()
        flight1, _ = Flight.objects.get_or_create(
            route=route_jfk_lhr,
            airplane=airplane1,
            departure_time=now + timedelta(days=1),
            arrival_time=now + timedelta(days=1, hours=7),
        )
        flight1.crew.set([crew1, crew2])

        flight2, _ = Flight.objects.get_or_create(
            route=route_lhr_cdg,
            airplane=airplane2,
            departure_time=now + timedelta(days=2),
            arrival_time=now + timedelta(days=2, hours=1, minutes=30),
        )
        flight2.crew.set([crew1])

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))