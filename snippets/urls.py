from django.urls import path
from snippets import views

urlpatterns = [
    path('', views.home),
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('albums/', views.AlbumList.as_view(), name='album-detail'),
    path('albums/<int:pk>/', views.AlbumDetail.as_view()),
    path('tracks/', views.TrackList.as_view()),
    path('tracks/<int:pk>/', views.TrackDetail.as_view(), name='track-detail'),
    
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('collections/', views.CollectionList.as_view()),
    path('collections/<int:pk>/', views.CollectionDetail.as_view()),
    path('pdcollections/', views.ProductCollectionList.as_view()),
    path('pdcollections/<int:pk>/', views.ProductCollectionDetail.as_view()),
]
