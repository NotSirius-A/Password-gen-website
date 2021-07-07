from django.urls import path

from .views import passwordgenAPIViewSet

urlpatterns = [
    path('get/', passwordgenAPIViewSet.as_view({'get':'retrieve'}), name="passwordgenAPI_output"),
]
