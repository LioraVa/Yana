from django.shortcuts import HttpResponse, render
from django.views.generic import DetailView

from appointments.forms import appointmentForm
from appointments.models import appointments


# after updating it will redirect to detail_View 
def detail_view(request, id):
    context = {}
    context["data"] = appointments.objects.get(id=id)
    return render(request, "detail_view.html", context)


class appointmentsdetail(DetailView):
    template_name = 'appointment_files/view_appointment.html'
    model = appointments


def index(request):
    if request.user.is_authenticated:
        # If a user is logged in, redirect them to a page informing them of such
        return render(request, 'appointment_files/index.html')
    else:
        return render(request, 'base.html')


def viewAppointments(request):
    query_results = appointments.objects.all()
    return render(request, 'appointment_files/view_appointment.html', {'query_results': query_results})


def add(request):
    if request.method == "POST":
        form = appointmentForm(request.POST)
        if form.is_valid():
            add = form.cleaned_data
            add = form.save()

            return HttpResponse("appointment added!!!")

    else:
        form = appointmentForm()

    return render(request, "appointment_files/add.html", {"form": form})


def delete_app(request, app_id):
    app = appointments.objects.get(id=app_id)

    if request.method == 'POST':
        app.delete()

    return HttpResponse("appointment Deleted!!!")


def edit(request, app_id):
    app = appointments.objects.get(id=app_id)
    f_name = app.first_name
    l_name = app.last_name
    t = app.time_field
    d = app.date_field
    cent = app.center_id
    d_name = app.doctor_name
    p_id = app.pat_id
    if request.method != 'POST':
        form = appointmentForm(instance=app)
    else:
        form = appointmentForm(instance=app, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("appointment edited!!!")
    context = {'first_name': f_name, 'last_name': l_name, 'pat_id': p_id, 'center': cent,
               'time_field': t, 'date_field': d, 'doctor_name': d_name, 'form': form}
    return render(request, 'appointment_files/edit.html', context)
