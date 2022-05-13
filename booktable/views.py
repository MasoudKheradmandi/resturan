from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import BookTableModel
from booktable.forms import BookTableForm
from django.contrib.auth import get_user
# Create your views here.
@login_required
def Book_A_Table(request):
    
    if get_user == NULL:
        return redirect('account:signup')


    else:
        if request.method == 'POST':
            form = BookTableForm(request.POST)
            if form.is_valid():
                date = form.cleaned_data['date']
                time = form.cleaned_data['time']
                month = form.cleaned_data['month']
                tedad = form.cleaned_data['tedad']
                fullname = form.cleaned_data['fullname']
                Note = form.cleaned_data['Note']
                form = BookTableModel.objects.create(date=date,time=time,month=month,tedad=tedad,fullname=fullname,Note=Note)
                form.save()
            return HttpResponse("DONE!")
        else:
            form= BookTableForm()
    
        date = range(1,31)
        time = range(9,24)
        month=range(1,13)
        tedad = range(1,6)
    

        context = {
        'form':form,
        'date':date,
        'time':time,
        'month':month,
        'tedad':tedad,
           }

    return render(request,'book-table.html',context)