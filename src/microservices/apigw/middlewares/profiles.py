from django.http import HttpResponse
import logging

class ProfileMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def process_view(self, request, view_func, view_args, view_kwargs):

        return None

    def __call__(self, request):

        response = self.get_response(request)

        return response

