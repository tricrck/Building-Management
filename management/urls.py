from django.urls import path

from . import views
from .views import (
    BuildingCreateView,
    BuildingDeleteView,
    BuildingListView,
    BuildingUpdateView,
    ApartmentCreateView,
    ApartmentDeleteView,
    ApartmentListView,
    ApartmentUpdateView,
    TenantCreateView,
    TenantDeleteView,
    TenantListView,
    TenantUpdateView,

)

app_name = 'management'
urlpatterns = [
  path('', views.home),
  path('building/list', BuildingListView.as_view(), name ='building_list'),
  path('tenant/list', TenantListView.as_view(), name ='tenant_list'),
  path('apartment/list', ApartmentListView.as_view(), name ='apartment_list'),
  path('apartment/create', ApartmentCreateView.as_view(), name ='apartment_create'),
  path('apartment/update/<int:id>', ApartmentUpdateView.as_view(), name ='apartment_update'),
  path('apartment/delete/<int:id>', ApartmentDeleteView.as_view(), name ='apartment_delete'),
  path('tenant/create', TenantCreateView.as_view(), name ='tenant_create'),
  path('tenant/update/<int:id>', TenantUpdateView.as_view(), name ='tenant_update'),
  path('tenant/delete/<int:id>', TenantDeleteView.as_view(), name ='tenant_delete'),
  path('building/create', BuildingCreateView.as_view(), name ='building_create'),
  path('building/update/<int:id>', BuildingUpdateView.as_view(), name ='building_update'),
  path('building/delete/<int:id>', BuildingDeleteView.as_view(), name ='building_delete'),
]