from django.urls import path

from . import views

urlpatterns = [
    path('autos/', views.autos),
    path('autos/<int:auto_id>', views.auto),
    path('owners/', views.owners),
    path('owners/<int:owner_id>', views.owner),
    path('auto_passports/', views.auto_passports),
    path('auto_passports/<int:auto_passport_id>', views.auto_passport),
]