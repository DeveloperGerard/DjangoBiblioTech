from django.urls import path
from .views import list_books,detalle_libro,categoria_libro

urlpatterns = [
    path('',list_books),
    path('<int:id>/',detalle_libro),
    path("<str:categoria>/",categoria_libro)
]
