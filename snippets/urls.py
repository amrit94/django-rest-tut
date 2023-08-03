from django.urls import path, include
from snippets.views import home, SnippetViewSet
from rest_framework import routers


# # # 1. ViewSets
# If using ViewSet in views --> use action a/c to actions def in views
snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    # 'patch': 'partial_update',
    'delete': 'destroy'
})
urlpatterns = [
    path('', home),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
]

# SnippetViewSet --> using routers

# Define and Register SimpleRouter
simple_router = routers.SimpleRouter()
simple_router.register(r'snippets', SnippetViewSet, basename="snippet")

# Define and Register DefaultRouter
default_router = routers.DefaultRouter()
default_router.register(r'snippets', SnippetViewSet, basename="snippet1")

# The API URLs are now determined automatically by the router
urlpatterns += [
    path('simple/', include(simple_router.urls)),
    path('default/', include(default_router.urls)),
]


# # # 2. ModelViewSets
from snippets.views import SnippetModelViewSet
modelviewset_router = routers.DefaultRouter()
modelviewset_router.register(r'snippets', SnippetModelViewSet, basename="snippet2")

urlpatterns += [
    path('modelviewset/', include(modelviewset_router.urls)),
]


# # # 2. ModelViewSets
from snippets.views import SnippetReadOnlyModelViewSet
ro_viewset_router = routers.DefaultRouter()
ro_viewset_router.register(r'snippets', SnippetReadOnlyModelViewSet, basename="snippet3")

urlpatterns += [
    path('ro_viewset/', include(ro_viewset_router.urls)),
]