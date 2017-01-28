from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
# from rest_framework.renderers import BrowsableAPIRenderer
from . import urls
from django.urls.resolvers import RegexURLPattern, RegexURLResolver
from django.urls.exceptions import NoReverseMatch
from django.shortcuts import render


@api_view(['GET'])
# @renderer_classes((BrowsableAPIRenderer,))
def api_root(request, format=None):
    def dfs(urlpatterns):
        res = {}
        for u in urlpatterns:
            try:
                if isinstance(u, RegexURLPattern):
                    res[u.name] = reverse(u.name, request=request, format=format)
                elif isinstance(u, RegexURLResolver):
                    res[u.urlconf_module.__name__] = dfs(u.url_patterns)
            except Exception:
                pass
        return res or None
    # return Response({
    #     'ranklist': reverse('ranklist', request=request, format=format),
    #     'register': reverse('sign-up', request=request, format=format),
    #     'test': reverse('contest-list', request=request, format=format),
    # })
    return Response(dfs(urls.urlpatterns))


def index(request):
    return render(request, 'index.html')
