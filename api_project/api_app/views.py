from django.shortcuts import get_object_or_404, render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from datetime import datetime
from .models import Persona, Tarea
from .serializers import PersonaSerializer, TareaSerializer


# ====================== VISTAS DE PERSONA ======================

# Listar personas
class PersonaList(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

    def get(self, request):
        personas = Persona.objects.all()
        serializer = PersonaSerializer(personas, many=True)
        if not personas:
            raise NotFound('No se encontraron personas.')
        return Response(
            {
                'success': True,
                'detail': 'Listado de personas.',
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )


# Crear personas
class CrearPersona(generics.CreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

    def post(self, request):
        serializer = PersonaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                'success': True,
                'detail': 'Persona creada correctamente.',
                'data': serializer.data
            },
            status=status.HTTP_201_CREATED
        )

# Actualizar personas
class ActualizarPersona(generics.UpdateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

    def put(self, request, pk):
        persona = get_object_or_404(Persona, pk=pk)
        email = request.data.get('email', None)

        # Verificar si el email ha cambiado
        if email and email != persona.email:
            # Verificar si ya existe otra persona con el mismo email
            if Persona.objects.filter(email=email).exclude(pk=pk).exists():
                return Response(
                    {'email': ['Persona con este email ya existe.']},
                    status=status.HTTP_400_BAD_REQUEST
                )

        serializer = PersonaSerializer(persona, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                'success': True,
                'detail': 'Persona actualizada correctamente.',
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )


# Buscar persona por documento
class PersonaByDocumento(generics.ListAPIView):
    serializer_class = PersonaSerializer

    def get(self, request, documento):
        persona = Persona.objects.filter(documento=documento).first()
        if not persona:
            raise NotFound('No se encontró una persona con ese documento.')

        serializer = PersonaSerializer(persona)
        return Response(
            {
                'success': True,
                'detail': 'Persona encontrada.',
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )


# ====================== VISTAS DE TAREA ======================

# Listar tareas
class TareaList(generics.ListCreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    def get(self, request):
        tareas = Tarea.objects.all()
        serializer = TareaSerializer(tareas, many=True)
        if not tareas:
            raise NotFound('No se encontraron tareas.')
        return Response(
            {
                'success': True,
                'detail': 'Listado de tareas.',
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )


# Buscar tareas por fecha específica
class TareaByFecha(generics.ListAPIView):
    serializer_class = TareaSerializer

    def get(self, request, fecha):
        try:
            fecha_obj = datetime.strptime(fecha, '%Y-%m-%d').date()
        except ValueError:
            return Response(
                {
                    'success': False,
                    'detail': 'Formato de fecha inválido. Use YYYY-MM-DD.',
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        tareas = Tarea.objects.filter(fecha_limite=fecha_obj)
        if not tareas.exists():
            raise NotFound('No se encontraron tareas para esa fecha.')

        serializer = TareaSerializer(tareas, many=True)
        return Response(
            {
                'success': True,
                'detail': f'Tareas encontradas para la fecha {fecha}.',
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )


# Buscar tareas por rango de fechas
class TareaByRangoFechas(generics.ListAPIView):
    serializer_class = TareaSerializer

    def get(self, request, fecha_inicio, fecha_fin):
        try:
            fecha_inicio_obj = datetime.strptime(fecha_inicio, '%Y-%m-%d').date()
            fecha_fin_obj = datetime.strptime(fecha_fin, '%Y-%m-%d').date()
        except ValueError:
            return Response(
                {
                    'success': False,
                    'detail': 'Formato de fecha inválido. Use YYYY-MM-DD.',
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if fecha_inicio_obj > fecha_fin_obj:
            return Response(
                {
                    'success': False,
                    'detail': 'La fecha de inicio no puede ser mayor que la fecha de fin.',
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        tareas = Tarea.objects.filter(
            fecha_limite__gte=fecha_inicio_obj,
            fecha_limite__lte=fecha_fin_obj
        )
        
        if not tareas.exists():
            raise NotFound('No se encontraron tareas en ese rango de fechas.')

        serializer = TareaSerializer(tareas, many=True)
        return Response(
            {
                'success': True,
                'detail': f'Tareas encontradas entre {fecha_inicio} y {fecha_fin}.',
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )


# Buscar tareas por persona
class TareaByPersona(generics.ListAPIView):
    serializer_class = TareaSerializer

    def get(self, request, persona_id):
        # Verificar que la persona existe
        persona = get_object_or_404(Persona, pk=persona_id)
        
        tareas = Tarea.objects.filter(persona=persona)
        if not tareas.exists():
            raise NotFound('No se encontraron tareas para esta persona.')

        serializer = TareaSerializer(tareas, many=True)
        return Response(
            {
                'success': True,
                'detail': f'Tareas encontradas para {persona.nombre} {persona.apellido}.',
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )