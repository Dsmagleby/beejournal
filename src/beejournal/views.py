from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    FormView,
)
from beejournal.forms import (
    HiveForm,
    InspectionBulkCreateForm,
    InspectionForm,
    PlaceForm,
    QueenForm,
    VarroaForm,
)
from beejournal.models import (
    Inspection,
    Place,
    Hive,
    Queen,
    Varroa,
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


class CustomFormView(FormView):
    """
    Custom FormView that sets the user on the object before saving
    and passes the user to the form.
    """
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
            return 'htmx/place_list_table.html'
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
            return 'htmx/hive_list_table.html'
        return self.template_name


class HiveCreateView(LoginRequiredMixin, CustomCreateView):
    model = Hive
    form_class = HiveForm
    template_name = "generic_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        frames_or_height = form.cleaned_data.get('frames_or_height')
        frames_or_height_value = form.cleaned_data.get('frames_or_height_value')
        if frames_or_height == 'frames':
            form.instance.frames = frames_or_height_value
        elif frames_or_height == 'height':
            form.instance.height = frames_or_height_value
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

    def form_valid(self, form):
        frames_or_height = form.cleaned_data.get('frames_or_height')
        frames_or_height_value = form.cleaned_data.get('frames_or_height_value')
        if frames_or_height == 'frames':
            form.instance.frames = frames_or_height_value
            form.instance.height = None
        elif frames_or_height == 'height':
            form.instance.height = frames_or_height_value
            form.instance.frames = None
        else:
            form.instance.frames = None
            form.instance.height = None
        return super().form_valid(form)


class QueenListView(LoginRequiredMixin, ListView):
    model = Queen
    template_name = "queen_list.html"
    paginate_by = 20

    def get_queryset(self):
        return Queen.objects.filter(user=self.request.user)

    def get_template_names(self, *args, **kwargs):
        if self.request.htmx:
            return 'htmx/queen_list_table.html'
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
            return 'htmx/inspection_list_table.html'
        return self.template_name


class InspectionCreateView(LoginRequiredMixin, CustomCreateView):
    model = Inspection
    form_class = InspectionForm
    template_name = "generic_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        if form.instance.hive:
            hive = form.instance.hive
            frames_or_height = form.cleaned_data.get('frames_or_height')
            frames_or_height_value = form.cleaned_data.get('frames_or_height_value')
            queen_color = form.cleaned_data.get('color')
            if queen_color:
                hive.color = queen_color
            if frames_or_height == 'frames':
                hive.frames = frames_or_height_value
                hive.height = None
            elif frames_or_height == 'height':
                hive.height = frames_or_height_value
                hive.frames = None
            hive.save()
        return super().form_valid(form)
    
    def get_initial(self):
        initial = super().get_initial()
        hive_id = self.kwargs.get('hive_id')
        if hive_id:
            hive = Hive.objects.filter(pk=hive_id).first()
            initial['hive'] = hive if hive else None
            initial['frames_or_height'] = 'height' if hive.height else 'frames'
            initial['frames_or_height_value'] = hive.frames or hive.height
        return initial


class InspectionUpdateView(LoginRequiredMixin, CustomUpdateView):
    model = Inspection
    form_class = InspectionForm
    template_name = "generic_form.html"

    def form_valid(self, form):
        if form.instance.hive:
            hive = form.instance.hive
            frames_or_height = form.cleaned_data.get('frames_or_height')
            frames_or_height_value = form.cleaned_data.get('frames_or_height_value')
            if frames_or_height == 'frames':
                hive.frames = frames_or_height_value
                hive.height = None
            elif frames_or_height == 'height':
                hive.height = frames_or_height_value
                hive.frames = None
            hive.save()
        return super().form_valid(form)


class InspectionBulkCreateView(LoginRequiredMixin, CustomFormView):
    template_name = "generic_form.html"
    form_class = InspectionBulkCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        place = get_object_or_404(Place, id=self.request.GET.get("id"))
        context["form_title"] = "Opret inspektioner på " + place.name
        return context

    def form_valid(self, form):
        place = get_object_or_404(Place, id=self.request.GET.get("id"))
        hives = Hive.objects.filter(place=place)
        for hive in hives:
            Inspection.objects.create(
                hive=hive,
                user=self.request.user,
                **form.cleaned_data
            )
        return super().form_valid(form)

    def get_success_url(self):
        place = get_object_or_404(Place, id=self.request.GET.get("id"))
        return reverse("overview") + f"?id={place.id}"


class VarroaListView(LoginRequiredMixin, ListView):
    model = Varroa
    template_name = "varroa_list.html"
    paginate_by = 20

    def get_queryset(self):
        return Varroa.objects.filter(user=self.request.user)

    def get_template_names(self, *args, **kwargs):
        if self.request.htmx:
            return 'htmx/varroa_list_table.html'
        return self.template_name


class VarroaCreateView(LoginRequiredMixin, CustomCreateView):
    model = Varroa
    form_class = VarroaForm
    template_name = "generic_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class VarroaUpdateView(LoginRequiredMixin, CustomUpdateView):
    model = Varroa
    form_class = VarroaForm
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
            hives = Hive.objects.filter(place=place)
            if not hives.exists():
                continue
            place_data = {
                'place': place,
                'hives': hives,
            }
            overview_data.append(place_data)
        context['overview_data'] = overview_data
        return context
