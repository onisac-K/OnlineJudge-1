from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
# from rest_framework.renderers import BrowsableAPIRenderer
from . import urls


@api_view(['GET'])
# @renderer_classes((BrowsableAPIRenderer,))
def api_root(request, format=None):
    def dfs(urlpatterns):
        res = {}
        for u in urlpatterns:
            try:
                if hasattr(u, 'name'):
                    res[u.name] = reverse(u.name, request=request, format=format)
                else:
                    res[u.urlconf_name.__name__] = dfs(u.url_patterns)
            except Exception as e:
                pass
        return res or None
    # return Response({
    #     'ranklist': reverse('ranklist', request=request, format=format),
    #     'register': reverse('sign-up', request=request, format=format),
    #     'test': reverse('contest-list', request=request, format=format),
    # })
    return Response(dfs(urls.urlpatterns))