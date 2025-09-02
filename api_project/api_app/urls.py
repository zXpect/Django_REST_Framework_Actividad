from django.urls import path
from .views import (
    PersonaList, PersonaByDocumento, ActualizarPersona, CrearPersona,
    TareaList, TareaByFecha, TareaByRangoFechas, TareaByPersona
)

urlpatterns = [
    # Personas
    path('personas/', PersonaList.as_view(), name='persona-list'),
    path('personas/crear/', CrearPersona.as_view(), name='persona-crear'),
    path('personas/actualizar/<int:pk>/', ActualizarPersona.as_view(), name='persona-actualizar'),
    path('personas/documento/<str:documento>/', PersonaByDocumento.as_view(), name='persona-por-documento'),
    
    #Tareas
    path('tareas/', TareaList.as_view(), name='tarea-list'),
    path('tareas/fecha/<str:fecha>/', TareaByFecha.as_view(), name='tarea-por-fecha'),
    path('tareas/rango-fechas/<str:fecha_inicio>/<str:fecha_fin>/', TareaByRangoFechas.as_view(), name='tarea-por-rango-fechas'),
    path('tareas/persona/<int:persona_id>/', TareaByPersona.as_view(), name='tarea-por-persona'),
]

# Debug - eliminar después
print("URLs de api_app cargadas correctamente:")
for pattern in urlpatterns:
    print(f"  - {pattern.pattern}")