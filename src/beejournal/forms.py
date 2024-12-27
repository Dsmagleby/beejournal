from django import forms
from django.forms.widgets import Widget
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Field
from beejournal.models import Place, Hive, Queen, Inspection


class BaseModelForm(forms.ModelForm):
    """
    Adds a submit button to the forms if no layout is defined.
    If a layout is defined, submit button has to be added manually 
    within the formhelper layout.
    """
    def __init__(self, *args, **kwargs):
        super(BaseModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        if not self.helper.layout:
            self.helper.layout = Layout(*self.fields.keys())
        self.helper.layout.append(Submit('submit', 'Gem', css_class='btn btn-secondary my-2'))


class RangeSliderWidget(Widget):
    def render(self, name, value, attrs=None, renderer=None):
        # Render the HTML for the range slider
        return mark_safe(render_to_string(
                'widgets/range_slider.html',
                {
                    'name': name,
                    'value': value,
                    'min': 0,
                    'max': 10,
                },
            )
        )

    def value_from_datadict(self, data, files, name):
        # Extract the value from the submitted data
        return int(data.get(name))


class PlaceForm(BaseModelForm):
    class Meta:
        model = Place
        fields = ['name']
        labels = {
            'name': 'Navn',
        }

    def __init__(self, *args, **kwargs):
        _ = kwargs.pop('user')
        super().__init__(*args, **kwargs)


class HiveForm(BaseModelForm):
    class Meta:
        model = Hive
        fields = ['number', 'frames', 'place']
        labels = {
            'number': 'Nummer',
            'frames': 'Rammer',
            'place': 'Sted',
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['place'].queryset = Place.objects.filter(user=user)


class QueenForm(BaseModelForm):
    color = forms.ChoiceField(
        choices=Queen.CHOICES,
        widget=forms.RadioSelect(),
    )
    class Meta:
        model = Queen
        fields = ['hive', 'date', 'comment', 'color', 'marked']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'hive': 'Stade',
            'date': 'Dato',
            'comment': 'Kommentar',
            'color': 'Farve',
            'marked': 'Markeret',
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['hive'].queryset = Hive.objects.filter(user=user)
        self.helper.layout = Layout(
            'hive',
            'date',
            'comment',
            Field('color', template='layouts/inline_radio_select.html'),
            'marked',
            Submit('submit', 'Gem', css_class='btn btn-secondary my-2'),
        )


class InspectionForm(BaseModelForm):
    class Meta:
        model = Inspection
        fields = ['hive', 'date', 'comment', 'larva', 'egg', 'queen', 'mood', 'size', 'varroa']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'mood': RangeSliderWidget(),
            'size': RangeSliderWidget(),
            'varroa': RangeSliderWidget(),
        }
        labels = {
            'hive': 'Stade',
            'date': 'Dato',
            'comment': 'Kommentar',
            'larva': 'Larver',
            'egg': 'Æg',
            'queen': 'Dronning',
            'mood': 'Humør',
            'size': 'Størrelse',
            'varroa': 'Varroa',
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['hive'].queryset = Hive.objects.filter(user=user)
        self.helper.layout = Layout(
            Div(
                Div('hive', css_class='md:w-[50%] md:mr-2'),
                Div('date', css_class='md:w-[50%] md:ml-2'),
                css_class='md:flex md:justify-between'
            ),
            'comment',
            Div(
                Div('larva', css_class='md:w-[33%]'),
                Div('egg', css_class='md:w-[33%]'),
                Div('queen', css_class='md:w-[33%]'),
                css_class='md:flex md:justify-between'
            ),
            'mood',
            'size',
            'varroa',
            Submit('submit', 'Gem', css_class='btn btn-secondary my-2'),
        )   