from django.shortcuts import render
from reto.models import Sucursal, Evento, Participante
from datetime import datetime

def pantalla_view(request):
    # Obtener la fecha actual
    fecha_actual = datetime.now()

    # Obtener el mes actual
    mes_actual = fecha_actual.month

    # Obtener la sucursal con el ID 1
    sucursal = Sucursal.objects.get(id=1)

    # Obtener el evento activo del mes actual para la sucursal
    evento_activo = Evento.objects.filter(sucursal=sucursal, fecha_inicio__month=mes_actual).first()

    # Obtener los participantes con los puntajes más altos para cada categoría
    participantes = Participante.objects.filter(sucursal=sucursal, fecha__month=mes_actual, evento=evento_activo).order_by('-puntos')[:5]

    context = {
        'sucursal': sucursal,
        'evento_activo': evento_activo,
        'participantes': participantes
    }

    return render(request, 'pantalla.html', {
        'mes_actual': mes_actual,
        **context
    })