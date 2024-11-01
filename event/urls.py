from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name="home"),
    path('add_event', views.add_event_view, name="add_event"),
    path('view_event/<int:pk>', views.view_event_view, name="view_event"),
    path('update_event/<int:pk>', views.update_event_view, name="update_event"),
    path('delete_event/<int:pk>', views.delete_event_view, name="delete_event"),
    path('book_event/<int:pk>', views.book_event_view, name="book_event"),

    path('booked_event', views.booked_event_view, name="booked_event"),

    path('category', views.category_view, name="category"),
    path('add_category', views.add_category_view, name="add_category"),
    path('update_category/<int:pk>', views.update_category_view, name="update_category"),
    
]
