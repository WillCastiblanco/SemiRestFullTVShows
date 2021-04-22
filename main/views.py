from django.shortcuts import render,redirect
from.models import Show 

def index(request):
    allShows=Show.objects.all()
    context={
        "allShows":allShows
    }
    return render(request,'index.html',context)

def addShow(request):     
    return render(request,'addShow.html')
    # return redirect('/shows/new')

def createShow(request):
    if request.method == 'POST':
        Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'], 
            releaseDate=request.POST['releaseDate'], 
            description=request.POST['description']
            )
        return redirect("/shows")
    return redirect("/shows")

def editShow(request,showId):
    thisShow=Show.objects.get(id=showId)
    context={
        'thisShow':thisShow
    }
    return render(request,'editShow.html',context)

def updateShow(request,showId): 
    c=Show.objects.get(id=showId)
    c.title=request.POST['title']
    c.network=request.POST['network']
    c.releaseDate=request.POST['releaseDate']
    c.description=request.POST['description']
    c.save()        
    return redirect("/shows")
    
def displayShow(request,showId):
    thisShow=Show.objects.get(id=showId)
    context={
        'show':thisShow
    }
    return render (request,'displayShow.html',context)


def destroyShow(request,showId):
    c_destroy = Show.objects.get(id=showId)
    c_destroy.delete()
    return redirect('/shows')


def catch_all(request,url):
    return redirect('/shows')



