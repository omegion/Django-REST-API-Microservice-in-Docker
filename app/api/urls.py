from django.urls import path, include
from . import views

urlpatterns = [
    path('deploys', views.ListDeployer.as_view()),
    path('deploys/<int:pk>/', views.DetailDeployer.as_view()),
    path('view', views.SwaggerSchemaView.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
]