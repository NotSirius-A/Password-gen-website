from typing import Type
from django.shortcuts import render

from rest_framework import serializers, viewsets
from rest_framework.response import Response

from .serializers import CustomSerializer

from .utils import is_valid_APIrequest_custom
from passwordgen.utils import PasswordGen

from my_core.settings import BASE_DIR
from pathlib import Path


# from rest_framework import renderers


class passwordgenAPIViewSet(viewsets.ViewSet):
    """
    rest_framework view set,
    handles API calls
    """
    # renderer_classes = [renderers.JSONRenderer]

    def retrieve(self, request):

        traits = {
            'words': request.GET.get('words'),
            'symbols': request.GET.get('symbols'),
        }

        quantity = request.GET.get('quantity')

        # values need to be validated BEFORE the passwords are generated,
        # therefore i cant use the preffered serializer validation with
        # default ValidationErrors from rest_framework
        # i implemented my own data validation
        traits['symbols'], traits['words'], quantity, errors = is_valid_APIrequest_custom(traits, quantity)

        if len(errors['errors']) > 0:
            # return errors
            return Response(errors)

        # APIrequest should be valid now

        # initalizing passwordgen
        gen = PasswordGen(Path(BASE_DIR.parent, 'word_list', 'word_list_prod.csv'))
        gen.set_password_traits(**traits)

        # generating passwords 'quantity' times
        passwords = [gen.get_password() for i in range(quantity)]

        data = {
            'words': traits['words'],
            'symbols': traits['symbols'],
            'quantity': quantity,
            'passwords': passwords,
        }

        serializer = CustomSerializer(data=data)
        serializer.is_valid()

        return Response(serializer.data)

    def get_view_name(self):
        return "Password Generator API"
