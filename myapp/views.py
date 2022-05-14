from django.shortcuts import render
import datetime

  
# Create your views here.  
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods
#importing loading from django template  
from django.template import loader
from myapp.forms import StuForm

from django.shortcuts import render 
from myapp.functions.functions import handle_uploaded_file  
from myapp.forms import StudentForm

from reportlab.pdfgen import canvas  

def getpdf(request):  
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'  
    p = canvas.Canvas(response)  
    p.setFont("Times-Roman", 55)  
    p.drawString(100,700, "Hello, Django.")  
    p.showPage()  
    p.save()  
    return response  

def setcookie(request):  
    response = HttpResponse("Cookie Set")  
    response.set_cookie('django-tutorial', 'data store in browser')  
    return response

def getcookie(request):  
    tutorial  = request.COOKIES['django-tutorial']  
    return HttpResponse("django tutorials @: "+  tutorial);


def upload(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file_test'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        student = StudentForm()  
        return render(request,"upload-file.html",{'form':student})  

from myapp.forms import EmployeeForm

def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                return redirect('/')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'emp-form.html',{'form':form}) 
  
def stu(request):  
    student = StudentForm()  
    return render(request,"stu-form.html",{'form':student})  

def formModel(request):  
    stu = StuForm()  
    return render(request,"form-model.html",{'form':stu})

def hello(request):  
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")

def index(request):  
    # now = datetime.datetime.now()  
    # html = "<html><body><h3>Now time is %s.</h3></body></html>" % now  
    # return HttpResponse(html)    # rendering the template in HttpResponse

    # a = 1  
    # if a:  
    #     return HttpResponseNotFound('<h1>Page not found</h1>')  
    # else:  
    #     return HttpResponse('<h1>Page was found</h1>') # rendering the template in HttpResponse
    name = {  
        'student':'rahul'  
    }

    template = loader.get_template('index.html') # getting our template  
    return HttpResponse(template.render(name))   # rendering the template in HttpResponse 

@require_http_methods(["GET"])  
def show(request):  
    return HttpResponse('<h1>This is Http GET request.</h1>')     
