from django.shortcuts import render, redirect
from .forms import TableForm  
from .models import Table 
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.
@login_required
def emp(request):  
    form = TableForm()
    if request.method == "POST":  
        #print('Print Table:' ,request.POST)
        form = TableForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass  
    else:  
        form = TableForm()  
    return render(request,'table/addt.html',{'form':form}) 

@user_passes_test(lambda u: u.is_superuser)
def show(request):  
    table = Table.objects.all()  
    return render(request,"table/showt.html",{'table':table})
@user_passes_test(lambda u: u.is_superuser) 
def edit(request, id):  
    table = Table.objects.get(id=id)  
    return render(request,'table/editt.html', {'table':table})


@user_passes_test(lambda u: u.is_superuser)  
def update(request, id):  
    table = Table.objects.get(id=id)  
    form = TableForm(request.POST, instance = table)  
    if form.is_valid():  
        form.save()  
        return redirect("/rent")  
    return render(request, 'table/editt.html', {'table': table})  

@user_passes_test(lambda u: u.is_superuser)
def destroy(request, id):  
    table = Table.objects.get(id=id)  
    table.delete()  
    return redirect("/rent")  