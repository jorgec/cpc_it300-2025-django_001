"""
URL configuration for django_01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path

from quotes import views as quote_views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", quote_views.QuotesListView.as_view(), name="quotes"),
    path("quotes/<int:pk>/", quote_views.QuoteDetailView.as_view(), name="quote-detail"),
    path("quotes/create/", quote_views.QuoteCreateView.as_view(), name="quote-create"),
    path("quotes/update/<int:pk>/", quote_views.QuoteUpdateView.as_view(), name="quote-update"),
    path("quotes/delete/<int:pk>/", quote_views.QuoteDeleteView.as_view(), name="quote-delete"),
    path("quotes/random", quote_views.QuoteRandomView.as_view(), name="quote-random"),
]
