from django.shortcuts import render
from .models import TimeSlot

def timetable_view(request):

    records = TimeSlot.objects.all().order_by(
        'day', 'start_time'
    )

    return render(
        request,
        'timetable.html',
        {'records': records}
    )