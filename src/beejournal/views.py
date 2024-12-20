from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
)
from beejournal.forms import (
    HiveForm,
    InspectionForm,
    PlaceForm,
    QueenForm,
)
from beejournal.models import (
    Inspection,
    Place,
    Hive,
    Queen,
)


class CustomCreateView(CreateView):
    """
    Custom CreateView that sets the user on the object before saving
    and passes the user to the form.
    """
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class CustomUpdateView(UpdateView):
    """
    Custom UpdateView that sets the user on the object before saving
    and passes the user to the form.
    """
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class PlaceListView(LoginRequiredMixin, ListView):
    model = Place
    template_name = "place_list.html"
    paginate_by = 20

    def get_queryset(self):
        return Place.objects.filter(user=self.request.user)

    def get_template_names(self, *args, **kwargs):
        if self.request.htmx:
            return 'htmx/place_list_row.html'
        return self.template_name

class PlaceCreateView(LoginRequiredMixin, CustomCreateView):
    model = Place
    form_class = PlaceForm
    template_name = "generic_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PlaceUpdateView(LoginRequiredMixin, CustomUpdateView):
    model = Place
    form_class = PlaceForm
    template_name = "generic_form.html"


class HiveListView(LoginRequiredMixin, ListView):
    model = Hive
    template_name = "hive_list.html"
    paginate_by = 20

    def get_queryset(self):
        return Hive.objects.filter(user=self.request.user)

    def get_template_names(self, *args, **kwargs):
        if self.request.htmx:
            return 'htmx/hive_list_row.html'
        return self.template_name

class HiveCreateView(LoginRequiredMixin, CustomCreateView):
    model = Hive
    form_class = HiveForm
    template_name = "generic_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        place_id = self.kwargs.get('place_id')
        if place_id:
            place = Place.objects.filter(pk=place_id).first()
            initial['place'] = place if place else None
        return initial

class HiveUpdateView(LoginRequiredMixin, CustomUpdateView):
    model = Hive
    form_class = HiveForm
    template_name = "generic_form.html"


class QueenListView(LoginRequiredMixin, ListView):
    model = Queen
    template_name = "queen_list.html"
    paginate_by = 20

    def get_queryset(self):
        return Queen.objects.filter(user=self.request.user)

    def get_template_names(self, *args, **kwargs):
        if self.request.htmx:
            return 'htmx/queen_list_row.html'
        return self.template_name

class QueenCreateView(LoginRequiredMixin, CustomCreateView):
    model = Queen
    form_class = QueenForm
    template_name = "generic_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        hive_id = self.kwargs.get('hive_id')
        if hive_id:
            hive = Hive.objects.filter(pk=hive_id).first()
            initial['hive'] = hive if hive else None
        return initial

class QueenUpdateView(LoginRequiredMixin, CustomUpdateView):
    model = Queen
    form_class = QueenForm
    template_name = "generic_form.html"


class InspectionListView(LoginRequiredMixin, ListView):
    model = Inspection
    template_name = "inspection_list.html"
    paginate_by = 20

    def get_queryset(self):
        return Inspection.objects.filter(user=self.request.user)

    def get_template_names(self, *args, **kwargs):
        if self.request.htmx:
            return 'htmx/inspection_list_row.html'
        return self.template_name

class InspectionCreateView(LoginRequiredMixin, CustomCreateView):
    model = Inspection
    form_class = InspectionForm
    template_name = "generic_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_initial(self):
        initial = super().get_initial()
        hive_id = self.kwargs.get('hive_id')
        if hive_id:
            hive = Hive.objects.filter(pk=hive_id).first()
            initial['hive'] = hive if hive else None
        return initial

class InspectionUpdateView(LoginRequiredMixin, CustomUpdateView):
    model = Inspection
    form_class = InspectionForm
    template_name = "generic_form.html"


class Overview(LoginRequiredMixin, ListView):
    model = Hive
    template_name = "overview.html"

    def get_queryset(self):
        return Hive.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        overview_data = []
        places = Place.objects.filter(user=self.request.user)
        for place in places:
            place_data = {
                'place': place,
                'hives': Hive.objects.filter(place=place),
            }
            overview_data.append(place_data)
        context['overview_data'] = overview_data
        return context
