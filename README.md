# Airport API Service (Hard) - Mate Academy Portfolio Project

A robust RESTful API system for tracking worldwide airport flights, managing fleets, crew, and ticket bookings, built with Django and Django REST Framework (DRF).

## Technologies Used
* Python & Django
* Django REST Framework (DRF)
* SQLite / PostgreSQL

##  Planned Features
* Complete management of Airports, Routes, and Cities.
* Fleet management (Airplane Types and Airplanes with row/seat controls).
* Flight Crew management.
* Flight scheduling with dynamic calculation of available tickets.
* Order and Ticket system with strict seat validation constraints.

## Database Structure / Models
The application is structured around the following relational entities:
* **Airport & Route**: Manages origins, destinations, and flight distances.
* **Airplane & AirplaneType**: Controls aircraft fleets, seating capacities, and row/seat constraints.
* **Crew**: Stores flight personnel details.
* **Flight**: Links routes, airplanes, departure/arrival times, and crew members.
* **Order & Ticket**: Handles user ticket purchases with strict database constraints and seat validation to prevent double-booking.

## Serializers & Business Logic
* **Nested Serializers**: Used in list and detail views to provide rich, descriptive JSON outputs (e.g., expanding airport details inside routes, or airplane types inside airplanes).
* **Atomic Transactions**: Orders containing multiple tickets are handled inside atomic blocks to guarantee data consistency.
* **Seat Validations**: Custom validations ensure tickets cannot exceed physical airplane boundaries.

### Prerequisites
* Python 3.10+
* Poetry or pip

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url> .