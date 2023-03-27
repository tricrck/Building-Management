from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import (
    CreateView,
    ListView,
    DeleteView,
    UpdateView
)
from .models import Building, Apartment, Tenant
from .forms import BuildingModelForm, ApartmentModelForm, TenantModelForm
# Create your views here.

def home(request):
    return render(request, 'management/home.html')



class BuildingListView(ListView):
    template_name = 'management/building_list.html.html'
    queryset = Building.objects.all()
     # Variable definition 
    variable = ["Stores",["San Diego",["Downtown","Uptown","Midtown"]]]

    # Template definition with linenumbers filt
class TenantListView(ListView):
    template_name = 'management/tenant_list.html.html'
    queryset = Tenant.objects.all()

class ApartmentListView(ListView):
    template_name = 'management/apartment_list.html.html'
    queryset = Apartment.objects.all()

class ApartmentCreateView(CreateView):
    template_name = 'management/apartment_create_form.html'
    form_class = ApartmentModelForm
    model = Apartment
    queryset = Apartment.objects.all() 

    def form_valid(self, form):
        return super(ApartmentCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('management:apartment_create')


class ApartmentUpdateView(UpdateView):
    template_name = 'management/apartment_update_form.html'
    form_class = ApartmentModelForm
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Apartment, id=id_)
        
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    

class ApartmentDeleteView(DeleteView):
    template_name = 'management/apartment_delete_form.html'
    model = Apartment
    def get_object(self):
        new = self.kwargs.get("id")
        id_ = int(new)
        return get_object_or_404(Apartment, id=id_)
        
    def get_success_url(self):
        return reverse('management:apartment_list')

class TenantCreateView(CreateView):
    template_name = 'management/tenant_create_form.html'
    model = Tenant
    form_class = TenantModelForm
    queryset = Tenant.objects.all() 

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('management:tenant_create')


class TenantUpdateView(UpdateView):
    template_name = 'management/tenant_update_form.html'
    form_class = TenantModelForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Tenant, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class TenantDeleteView(DeleteView):
    template_name = 'management/tenant_delete_form.html'
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Tenant, id=id_)

    def get_success_url(self):
        return reverse('management:tenant_list')

class BuildingCreateView(CreateView):
    template_name = 'management/building_create_form.html'
    form_class = BuildingModelForm
    queryset = Building.objects.all() 

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('management:building_create')

class BuildingUpdateView(UpdateView):
    template_name = 'management/building_update_form.html'
    form_class = BuildingModelForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Building, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class BuildingDeleteView(DeleteView):
    template_name = 'management/building_delete_form.html'
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Building, id=id_)

    def get_success_url(self):
        return reverse('management:building_list')