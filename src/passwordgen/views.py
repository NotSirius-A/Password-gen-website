from django.shortcuts import render

from pathlib import Path
from my_core.settings import BASE_DIR

from .utils import PasswordGen, str_to_bool
from .forms import PassGenSettingsForm

def homepage_view(request, *args, **kwargs):
    """
    docstring
    """
    
    DEFAULT_WORDS = 4
    MAX_WORDS = PassGenSettingsForm.MAX
    MIN_WORDS = PassGenSettingsForm.MIN
    DEFAULT_SYMBOLS = True

    form = PassGenSettingsForm(request.GET or None)

    password = None
    gen = PasswordGen(Path(BASE_DIR.parent, 'word_list', 'word_list_prod.csv'))

    # put relevant url params into a dict, for later processing
    traits = {
        'words': request.GET.get('words', default=DEFAULT_WORDS),
        'symbols': request.GET.get('symbols', default=DEFAULT_SYMBOLS)
        }
    
    # url params are str's and user can manipulate the request, 
    # therefore values have be cleaned/converted
    try:
        traits['words'] = int(traits['words'])
        if traits['words'] > MAX_WORDS or traits['words'] < MIN_WORDS:
            raise ValueError
    except ValueError:
        traits['words'] = DEFAULT_WORDS
    
    try:
        traits['symbols'] = str_to_bool(traits['symbols'])
    except:
        traits['symbols'] = True

    try:
        gen.set_password_traits(**traits)
        password=gen.get_password()
    except Exception:
        pass

    context = {
        'password': password,
        'form': form,
    }
    return render(request, 'passwordgen/gen.html', context)
