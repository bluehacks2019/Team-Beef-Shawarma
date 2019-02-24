from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Day, Plans,Tips
from .forms import DayForm,PlanForm,DayModelForm,PlanModelForm
# Create your views here.
def index(request):
    if request.method == 'POST':
        # day_made = request.session['day_made']
        if 'submit' in request.POST:
            day_form = DayModelForm(request.POST)
            if day_form.is_valid():
                print ("VALID DAY FORM YAY")
                day_form.save()
                return redirect(index)
    day_list = Day.objects.order_by('day_made')[0:]
    
    day_form = DayModelForm(request.POST)
    context = {'day_list': day_list, 'day_form':day_form }
    return render(request, 'homePage.html', context)
def day_page(request,day_made):
    if request.method == 'POST':
        day = Day.objects.get(day_made = day_made)
       
        if 'submit_plan' in request.POST:
            plan_form = PlanModelForm(request.POST)
            if plan_form.is_valid():
                print (day)
                print("PLAN FORM IS VALID FUCK YEAH")
                time_start = plan_form.cleaned_data['time_start']
                time_end = plan_form.cleaned_data['time_end']
                plan_title = plan_form.cleaned_data['plan_title']
                plan_description = plan_form.cleaned_data['plan_description']
                plan_tag = plan_form.cleaned_data['plan_tag']
                plan_obj = Plans(day = day, time_start = time_start, time_end = time_end, plan_title = plan_title, plan_description = plan_description, plan_tag = plan_tag)
                plan_obj.save()
                return redirect('./')
        if 'delete_plan' in request.POST:
            latest_plan_time = Plans.objects.all()[0].time_start
            print("DELET DIS")
            Plans.objects.filter(time_start = latest_plan_time).delete()
            return redirect('./')
    
    plan_list = Plans.objects.order_by('time_start')[0:]
    latest_plan_time = 0
    if(len(plan_list) != 0):
        latest_plan_time = plan_list[0].time_start
    tip_list = ''
    if (len(plan_list) == 0):
        True
    else:
        tip_list = Tips.objects.order_by('?').filter(response_for_tag = plan_list[0].plan_tag)[0]   
    # print(tip_list.tip_title +"  Tip Given")
    day_made = day_made
    form = PlanModelForm()
    context = {'plan_list': plan_list, 'day_made':day_made, 'form':form, 'tip_list':tip_list, 'latest_plan_time': latest_plan_time}
    return render(request, 'dayPage.html', context)
def day_form(request):
    if request.method == "POST":
        form = DayModelForm(request.POST)
        if form.is_valid():
            print("VALID DAY FORM")
            form.save()
    form = DayModelForm()
    context = {'form':form}        
    return render(request,'day_form.html', context)

def plan_form(request):
    if request.method == "POST":
        form = PlanModelForm(request.POST)
        if form.is_valid():
            print("NANAY MO VALID")
            form.save()
    form = PlanModelForm()
    context = {'form':form}
    return render(request,'plan_form.html',context)