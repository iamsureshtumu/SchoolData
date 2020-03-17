from django.shortcuts import render
from django.http import HttpResponse
#importing for class based views
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from . import forms

from cbv_app.models import School,Student
from django.urls import reverse_lazy,reverse
# Create your views here.

def index(request): #Function based views
    return HttpResponse("Function Based Views")

class indexview(View): #Class based views with VIEW
    def get(self,request):
        return HttpResponse("Class Based Views")

def temp1(request): # FBV Template
    return render(request,'temp1.html',context={'data':"Function Based Views"})

class TemplateDemoView(TemplateView): #CBV Template
    template_name='temp1.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['data']="Class Based Views"
        return context

def FBV_Backend(request): #FBV forms Backend O/P
    form=forms.Form_name()
    if request.method=="POST":
        form=forms.Form_name(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        return HttpResponse("Form submission Successful") #it will show that submission in next page
            # return render(request,'temp2.html',context={'form':forms.Form_name()}) #it will stay in same page under PRINT

    return render(request,'temp2.html',context={'form':form})

##################################################################################
#def FBV_Frontend_Display(request): checkout P7 updated project, sample5-->display.
###################################################################################

class Form_Demo(View): #CBV forms Backend o/p
    def get(self,request):
        return render(request,'temp2.html',context={'form':forms.Form_name()})

    def post(self,request):
        form=forms.Form_name(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        return HttpResponse("Form submission Successful")

class TempView(TemplateView):
    template_name='cbv_app/base.html'
##########################################################################################
class SchoolListView(ListView):
    model=School
    context_object_name="schools"

class SchoolDetailView(DetailView):
    model=School
    template_name='cbv_app/school_detail.html'
    context_object_name='school_detail'
                                             
class SchoolCreateView(CreateView):
    model=School
    fields=('name','principal','location')

class SchoolUpdateView(UpdateView):
    model=School
    fields=('name','principal','location')

class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy("cbv_app:list")
###########################################################################################
class StudentListView(ListView):
    model=Student
    context_object_name="students"
class StudentDetailView(DetailView):
    model=Student
    template_name='cbv_app/student_detail.html'
    context_object_name='student_detail'
                                             
class StudentCreateView(CreateView):
    model=Student
    fields=('name','age','school')

class StudentUpdateView(UpdateView):
    model=Student
    fields=('name','age','school')

class StudentDeleteView(DeleteView):
    model=Student
    success_url = reverse_lazy("cbv_app:studentlist")
