from django.urls import path

from .views import passwordgenAPIViewSet

urlpatterns = [
    path('', passwordgenAPIViewSet.as_view({'get':'retrieve'}), name="passwordgenAPI_output"),
]
