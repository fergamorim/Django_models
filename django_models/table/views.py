from django.shortcuts import redirect, render
from .forms import User, Address, PhoneNumber, Profession, UserProfile
from .models import User

# Create your views here.
def FormView(request, FromObject):
    form = exec(FromObject + '()')
    if request.method == 'POST':
        form = FromObject(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'crudapp/order.html'
    context = {'form': form}
    return render(request, template_name, context)

def ShowView(request, modelObject):
    obj = exec(modelObject + '.objects.all()')
    template_name = 'crudapp/show.html'
    context = {'obj': obj}
    return render(request, template_name, context)

def ShowView(request, modelObject, FormObject, f_oid):
    obj = exec(modelObject + '.objects.get(oid=' + f_oid + ')')
    form = exec(FormObject + '(instance='+ obj + ')')
    if request.method == 'POST':
        form = FormObject(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'crudapp/order.html'
    context = {'form': form}
    return render(request, template_name, context)

def deleteView(request, modelObject ,f_oid):
    obj = exec(modelObject + '.objects.get(oid=' + f_oid + ')')
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    template_name = 'crudapp/confirmation.html'
    context = {'obj': obj}
    return render(request, template_name, context)