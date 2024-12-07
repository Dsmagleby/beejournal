"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

import beejournal.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', beejournal.views.Overview.as_view(), name='overview'),
    # place views
    path(
        'places/create/',
        beejournal.views.PlaceCreateView.as_view(),
        name='place_create',
    ),
    path(
        'places/<int:pk>/update/',
        beejournal.views.PlaceUpdateView.as_view(),
        name='place_update',
    ),
    path(
        'places/',
        beejournal.views.PlaceListView.as_view(),
        name='place_list',
    ),
    # hive views
    re_path(
        r'^hives/create(?:/(?P<place_id>\d+))?/$',
        beejournal.views.HiveCreateView.as_view(),
        name='hive_create',
    ),
    path(
        'hives/<int:pk>/update/',
        beejournal.views.HiveUpdateView.as_view(),
        name='hive_update',
    ),
    path(
        'hives/',
        beejournal.views.HiveListView.as_view(),
        name='hive_list',
    ),
    # queen views
    re_path(
        r'^queens/create(?:/(?P<hive_id>\d+))?/$',
        beejournal.views.QueenCreateView.as_view(),
        name='queen_create',
    ),
    path(
        'queens/<int:pk>/update/',
        beejournal.views.QueenUpdateView.as_view(),
        name='queen_update',
    ),
    path(
        'queens/',
        beejournal.views.QueenListView.as_view(),
        name='queen_list',
    ),
    # inspection views
    re_path(
        r'inspections/create(?:/(?P<hive_id>\d+))?/$',
        beejournal.views.InspectionCreateView.as_view(),
        name='inspection_create',
    ),
    path(
        'inspections/<int:pk>/update/',
        beejournal.views.InspectionUpdateView.as_view(),
        name='inspection_update',
    ),
    path(
        'inspections/',
        beejournal.views.InspectionListView.as_view(),
        name='inspection_list',
    ),
    # browser
    path("__reload__/", include("django_browser_reload.urls")),
]
