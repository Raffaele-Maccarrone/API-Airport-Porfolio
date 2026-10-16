# Airport API Service (Hard) - Mate Academy Portfolio Project

A robust RESTful API system for tracking worldwide airport flights, managing fleets, crew, and ticket bookings, built with Django and Django REST Framework (DRF).

## 🚀 Technologies Used
- Python & Django (4.2+)
- Django REST Framework (DRF)
- PostgreSQL & Docker / Docker Compose
- DRF Spectacular (Swagger/OpenAPI documentation)
- SimpleJWT (Authentication)

## ✨ Features & Business Logic
- **Complete management**: Airports, Routes, and Cities.
- **Fleet management**: Airplane Types and Airplanes with row/seat controls.
- **Flight Crew management**: Assigning pilots and staff to flights.
- **Flight scheduling**: Dynamic calculation of available tickets.
- **Order and Ticket system**: Strict seat validation constraints and atomic transactions to prevent double-booking.
- **Optimized Queries**: Uses `select_related` and `prefetch_related` across viewsets to prevent N+1 performance issues.
- **Filtering & Security**: Advanced query parameters for flights and secure ownership restrictions for orders.

---

## 🗄️ Database Structure / Models
The application is structured around the following relational entities:
- **Airport & Route**: Manages origins, destinations, and flight distances.
- **Airplane & AirplaneType**: Controls aircraft fleets, seating capacities, and row/seat constraints.
- **Crew**: Stores flight personnel details.
- **Flight**: Links routes, airplanes, departure/arrival times, and crew members.
- **Order & Ticket**: Handles user ticket purchases with strict database constraints and seat validation.

---

## 🔌 API Endpoints
Once the server is running, you can access the following endpoints under `/api/airport/`:
- `GET / POST /api/airport/airports/` - Manage airports
- `GET / POST /api/airport/routes/` - Manage routes
- `GET / POST /api/airport/airplane-types/` - Manage airplane types
- `GET / POST /api/airport/airplanes/` - Manage airplanes
- `GET / POST /api/airport/crew/` - Manage flight crew
- `GET / POST /api/airport/flights/` - View/manage flights (supports filtering by `date`, `route`, `airplane`)
- `GET / POST /api/airport/orders/` - View/create authenticated user orders and tickets

---

## 🐳 Running with Docker
You can run the entire application (Django + PostgreSQL) easily using Docker Compose:

1. **Clone the repository**:
   ```bash
git clone [https://github.com/Raffaele-Maccarrone/API-Airport-Porfolio.git](https://github.com/Raffaele-Maccarrone/API-Airport-Porfolio.git)
cd API-Airport-Porfolio