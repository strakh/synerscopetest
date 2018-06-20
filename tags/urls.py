from django.urls import path
from . import views

app_name='tags'
urlpatterns = [
    path('', views.list_tags, name='root'),
    path('page<int:page_num>', views.list_tags, name='page'),
    path('add/', views.TagCreate.as_view(), name='add'),
    path('<int:pk>/', views.TagUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.TagDelete.as_view(), name='delete'),
]
