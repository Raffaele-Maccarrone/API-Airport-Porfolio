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

## API Endpoints & ViewSets
* **Optimized Queries**: Uses `select_related` and `prefetch_related` across viewsets to prevent N+1 query performance issues.
* **Dynamic Annotations**: Calculates available tickets dynamically for flights.
* **Filtering**: Supports query parameters for filtering flights by date, route, or airplane.
* **Security**: Orders are restricted securely to the authenticated owner.

## API Endpoints
Once the server is running, you can access the following endpoints under `/api/airport/`:
* `GET /POST /api/airport/airports/` - Manage airports
* `GET /POST /api/airport/routes/` - Manage routes
* `GET /POST /api/airport/airplane-types/` - Manage airplane types
* `GET /POST /api/airport/airplanes/` - Manage airplanes
* `GET /POST /api/airport/crew/` - Manage flight crew
* `GET /POST /api/airport/flights/` - View/manage flights (supports filtering by `date`, `route`, `airplane`)
* `GET /POST /api/airport/orders/` - View/create authenticated user orders and tickets

### Prerequisites
* Python 3.10+
* Poetry or pip

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url> .