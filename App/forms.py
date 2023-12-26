from django import forms
from .models import Direction, Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date', 'direction']
        
    title = forms.CharField(label='Название события', widget=forms.TextInput(attrs={'placeholder': 'Введите название события'}))
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'Выберите дату'}),
    )

    direction = forms.ModelChoiceField(queryset=Direction.objects.none(), empty_label='Выберите направление')
    

    def __init__(self, user, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['direction'].queryset = Direction.objects.filter(creator = user)
