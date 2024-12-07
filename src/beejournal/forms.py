from django import forms

from beejournal.models import Place, Hive, Queen, Inspection


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name']
        labels = {
            'name': 'Navn',
        }

    def __init__(self, *args, **kwargs):
        _ = kwargs.pop('user')
        super().__init__(*args, **kwargs)

class HiveForm(forms.ModelForm):
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


class QueenForm(forms.ModelForm):
    class Meta:
        model = Queen
        fields = ['hive', 'date', 'comment', 'color', 'marked']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
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


class InspectionForm(forms.ModelForm):
    class Meta:
        model = Inspection
        fields = ['hive', 'date', 'comment', 'larva', 'egg', 'mood', 'size', 'varroa']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'hive': 'Stade',
            'date': 'Dato',
            'comment': 'Kommentar',
            'larva': 'Larver',
            'egg': 'Æg',
            'mood': 'Humør',
            'size': 'Størrelse',
            'varroa': 'Varroa',
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['hive'].queryset = Hive.objects.filter(user=user)