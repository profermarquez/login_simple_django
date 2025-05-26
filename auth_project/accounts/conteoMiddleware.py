
from django.utils.deprecation import MiddlewareMixin
from django.utils.timezone import now


class LastSeenMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            request.session['last_seen'] = now().isoformat()

"""
MiddlewareMixin, podés implementar varios métodos especiales, entre ellos:

Método	Cuándo se ejecuta
-------------------------------------------------------------------------
process_request(self, request)	→  Antes de que se llame a la vista
process_view(self, request, view_func, view_args, view_kwargs)	→  Justo antes de ejecutar la vista
process_response(self, request, response) → 	Después de ejecutar la vista
process_exception(self, request, exception)	→  Si ocurre una excepción en la vista
"""
