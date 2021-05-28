from rest_framework.viewsets import *
from .permissions import *
from .serializers import *


class BodyViewSet(ModelViewSet):
    queryset = Body.objects.all()
    serializer_class = BodySerializer
    search_fields = ['body_type', 'body_model']


class EngineViewSet(ModelViewSet):
    queryset = Engine.objects.all()
    serializer_class = EngineSerializer
    search_fields = ['engine_type', 'power', 'volume']


class CarModelViewSet(ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    search_fields = ['model', 'brand', 'producer', 'engine_id', 'body_id']


class LegalOwnerViewSet(ModelViewSet):
    queryset = LegalOwner.objects.all()
    serializer_class = LegalOwnerSerializer
    search_fields = ['owner_inn', 'owner_name', 'chief', 'phone']


class PhysicalOwnerViewSet(ModelViewSet):
    queryset = PhysicalOwner.objects.all()
    serializer_class = PhysicalOwnerSerializer
    search_fields = ['owner_id', 'owner_fullname', 'phone', 'address']


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    search_fields = [
        'car_number', 'helm', 'drive',
        'year', 'owner_type', 'district',
        'year_tax', 'comment', 'color',
        'model', 'owner_inn', 'owner_id'
    ]


class DriveAwayInfoViewSet(ModelViewSet):
    queryset = DriveAwayInfo.objects.all()
    serializer_class = DriveAwayInfoSerializer
    search_fields = ['driving_away', 'date_away', 'date_return', 'car_number']


class InspectorViewSet(ModelViewSet):
    queryset = Inspector.objects.all()
    serializer_class = InspectorSerializer
    search_fields = ['sign_number', 'fullname', 'post']


class WatchInfoViewSet(ModelViewSet):
    queryset = WatchInfo.objects.all()
    serializer_class = WatchInfoSerializer
    search_fields = [
        'watch_date', 'sign_cost', 'watch_cost', 'mileage',
        'okay', 'reasons', 'car_number', 'inspector'
    ]
