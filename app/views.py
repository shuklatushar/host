from django.shortcuts import render
from django.http import HttpResponse
import joblib
# Create your views here.
def index(request):
    return render(request,'index.html') 

def result(request):
    inputlist=list()
    inputlist.append(request.GET['bidsPortfolioManager'])
    inputlist.append(request.GET['languageCode'])
    inputlist.append(request.GET['Age'])
    inputlist.append(request.GET['country'])
    inputlist.append(request.GET['appliedAmount'])
    inputlist.append(request.GET['Amount'])
    inputlist.append(request.GET['interest'])
    inputlist.append(request.GET['monthlyPayment'])
    
    inputlist.append(request.GET['Monthlypaymentday'])
    inputlist.append(request.GET['rating'])
    inputlist.append(request.GET['principalPaymentMode'])
    inputlist.append(request.GET['interestPenaltyPaymentMode'])
    inputlist.append(request.GET['PrincipalBalance'])
    inputlist.append(request.GET['interestAndPenaltyBalance'])
    inputlist.append(request.GET['previousPrepyamentBeforeLoan'])
    
    cls=joblib.load('technocolab_bondora_model_deployment.sav')
    ans=cls.predict([inputlist])
    ans=ans[0]
    v='will Not default'
    if ans==0:
       v='will default'
    return render(request,'result.html',{'ans':v}) 

def contact(request):
     return render(request,'contact.html') 

def home(request):
    inputlist=list()
    inputlist.append(request.GET['name'])
    inputlist.append(request.GET['email'])
    inputlist.append(request.GET['message'])
    return render(request,'index.html') 

def aboutus(request):
    return render(request,'aboutus.html') 