
from django.contrib import admin
from django.urls import path, include
from appVeterinaria import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appVeterinaria.urls')),
    # 2. RUTA PERSONALIZADA PARA LA PÁGINA PRINCIPAL DE INFO
    path('principal/', views.principal_veterinaria, name='principal_veterinaria'),

    # 3. RUTAS DE AUTENTICACIÓN
    # Forzamos template_name para usar tu login.html
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    # Al cerrar sesión, redirigimos de vuelta al login
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),

    # ... (el resto de tus rutas de CRUDS de appVeterinaria)
    
    # Ruta vacía para forzar la redirección al login
    path('', LoginView.as_view(template_name='registration/login.html'), name='inicio'),
]


