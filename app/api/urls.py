from django.urls import path, include
from . import views

urlpatterns = [
    path('deploys', views.ListDeployer.as_view(), name='api.v1.deploys'),
    path('deploys/<int:pk>', views.DetailDeployer.as_view(), name='api.v1.deploys.detail'),
    path('view', views.SwaggerSchemaView.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
]