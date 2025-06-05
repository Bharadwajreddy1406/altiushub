from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # CRUD operations for Users
    path("api/users/", views.get_collection, name='get_all_urls'),  # GET - Read all
    path("api/users/create/", views.add_url, name='create_url'),     # POST - Create
    path("api/users/<str:user_id>/", views.get_url, name='get_url'), # GET - Read one
    path("api/users/<str:user_id>/update/", views.update_url, name='update_url'), # PUT/PATCH - Update
    path("api/users/<str:user_id>/delete/", views.delete_url, name='delete_url'), # DELETE - Delete
    
    
    
    
    # below are the ones i did as part of revising
    
    
    path('', views.home, name='home'),
    path('greet/', views.greet, name='greet'),
    path('dynamic/<str:name>/', views.dynamic, name='dynamic'),
    path("user/<int:user_id>/<str:name>", views.user, name='user'),
    
    # API endpoints
    path("api/", views.test_api, name='test_api'),
    
    # Legacy endpoints (keeping for backward compatibility)
    path("api/get_data/", views.get_collection, name='get_collection'),
    path("api/add_url/", views.add_url, name='add_url'),
    
    # jwt authentication
    # JWT authentication endpoints
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Cookie-based JWT authentication
    path('api/login/', views.login_with_cookies, name='login_with_cookies'),
    path('api/logout/', views.logout_cookies, name='logout_cookies'),
]
