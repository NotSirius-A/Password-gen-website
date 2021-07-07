from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import NumberInput

# this worked fine as a widget for integer field,
# but i dont know how to display current value of the slider
# class CustomRangeInput(NumberInput):
#     input_type = 'range'

#     def __init__(self):
#         self.attrs = {'min':'2', 'max':'6', 'value':'4'}

class PassGenSettingsForm(forms.Form):
    MIN = 2
    MAX = 10

    words = forms.IntegerField(
        min_value=MIN, 
        max_value=MAX, 
        widget=NumberInput(attrs={
            'value':'4'
        }),
        error_messages={'invalid': '<2;10>',
                        'max_value': '<2;10>',
                        'min_value': '<2;10>',
                        }
    )

    symbols = forms.ChoiceField(choices=[
        (True, 'Yes'),
        (False, 'No'),
    ])

