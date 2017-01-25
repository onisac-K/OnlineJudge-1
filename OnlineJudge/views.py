from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
# from rest_framework.renderers import BrowsableAPIRenderer


@api_view(['GET'])
# @renderer_classes((BrowsableAPIRenderer,))
def api_root(request, format=None):
    return Response({
        'ranklist': reverse('ranklist', request=request, format=format),
        'register': reverse('sign-up', request=request, format=format),
    })
