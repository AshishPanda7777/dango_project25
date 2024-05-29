from django.shortcuts import render

# Create your views here.
import datetime
def filters(request):
    da=datetime.datetime.now()
    d={'data':'Python iS eAsY  tO lEaRn','da':da}
    return render(request,'filters.html')



def userfilters(request):
    d={'data':'hai PyTHon How aRe yOU'}
    return render(request,'userfilters.html',d)