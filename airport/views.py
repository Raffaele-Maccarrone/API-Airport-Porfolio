from datetime import datetime
from django.db.models import Count, F
from rest_framework import permissions, viewsets
from rest_framework.permissions import IsAuthenticated

from airport.models import (
    Airport,
    Route,
    AirplaneType,
    Airplane,
    Crew,
    Flight,
    Order,
)
from airport.serializers import (
    AirportSerializer,
    RouteSerializer,
    RouteListSerializer,
    AirplaneTypeSerializer,
    AirplaneSerializer,
    AirplaneListSerializer,
    CrewSerializer,
    FlightSerializer,
    FlightListSerializer,
    FlightDetailSerializer,
    OrderSerializer,
    OrderListSerializer,
)


class IsAdminOrIfAuthenticatedReadOnly(permissions.BasePermission):
    """
    Permite leitura apenas para usuários autenticados, mas apenas administradores
    podem criar, editar ou apagar (POST, PUT, PATCH, DELETE).
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        return bool(request.user and request.user.is_staff)


class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.select_related("source", "destination")
    serializer_class = RouteSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return RouteListSerializer
        return RouteSerializer


class AirplaneTypeViewSet(viewsets.ModelViewSet):
    queryset = AirplaneType.objects.all()
    serializer_class = AirplaneTypeSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class AirplaneViewSet(viewsets.ModelViewSet):
    queryset = Airplane.objects.select_related("airplane_type")
    serializer_class = AirplaneSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return AirplaneListSerializer
        return AirplaneSerializer


class CrewViewSet(viewsets.ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class FlightViewSet(viewsets.ModelViewSet):
    queryset = (
        Flight.objects.select_related(
            "route__source",
            "route__destination",
            "airplane__airplane_type",
        )
        .prefetch_related("crew")
        .annotate(
            tickets_available=F("airplane__rows")
            * F("airplane__seats_in_row")
            - Count("tickets")
        )
    )
    serializer_class = FlightSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def get_serializer_class(self):
        if self.action == "list":
            return FlightListSerializer
        if self.action == "retrieve":
            return FlightDetailSerializer
        return FlightSerializer

    def get_queryset(self):
        queryset = self.queryset

        date = self.request.query_params.get("date")
        route_id = self.request.query_params.get("route")
        airplane_id = self.request.query_params.get("airplane")

        if date:
            date_parsed = datetime.strptime(date, "%Y-%m-%d").date()
            queryset = queryset.filter(departure_time__date=date_parsed)
        if route_id:
            queryset = queryset.filter(route_id=route_id)
        if airplane_id:
            queryset = queryset.filter(airplane_id=airplane_id)

        return queryset.distinct()


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.prefetch_related(
        "tickets__flight__route__source",
        "tickets__flight__route__destination",
        "tickets__flight__airplane",
    )
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return OrderListSerializer
        return OrderSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
