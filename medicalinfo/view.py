from django.http import JsonResponse
from .models import Doctor
from .models import Medicine


def doctor_list(request):
    doctor=list(Doctor.objects.values())
    return JsonResponse({'doctor':doctor},safe=False)

def medicine_list(request):
    medicine=list(Medicine.objects.values())
    return JsonResponse({'medicine':medicine},safe=False)
