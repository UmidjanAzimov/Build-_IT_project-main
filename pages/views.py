from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView,DetailView, CreateView
from .models import Buyurtmachi, Mutaxasis,Firmalar,Post, Buyurtma,Buyurtmabajarish,Room, Message
from .forms import BuyurtmaBerish,Mutaxasis_Elon,Firma_Elon
from django.http import HttpResponse, JsonResponse


from .forms import BuyurtmachiForm, MutaxassisForm, FirmaForm

# Create your views here.
class Profile(TemplateView):
    template_name = 'profile.html'

class Home(TemplateView):
    template_name = 'home.html'

class LoginPage(TemplateView):
    template_name = 'login.html'

class MutaxasisSignup(ListView):
    model = Mutaxasis
    template_name = 'mutaxasissignup.html'

class FirmaSignup(ListView):
    model = Firmalar
    template_name = 'firmasignup.html'

class BuyurmachiSignup(ListView):
    model = Buyurtmachi
    template_name = 'buyurtmachisignup.html'

class Xizmatlar(TemplateView):
    template_name = 'xizmatlar.html'



class Buyurtmalar(TemplateView):
    
    template_name = 'buyurtmalar.html'

class Firma(ListView):
    paginate_by = 5
    model = Firmalar
    template_name = 'firmalar.html'
    
class Posts(ListView):
    paginate_by = 5
    model = Post
    template_name = 'yangiliklar.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class FirmaDetail(DetailView):
    model =Firmalar
    template_name = 'firma_detail.html'


class ListDetailView(DetailView):
    model = Buyurtma
    template_name = 'list_detail.html'

class SignUpMenu(TemplateView):
    template_name = "elon.html"


class Buyurtmalarss(ListView):
    paginate_by = 5
    model = Buyurtma
    template_name = 'buyurtmalar.html'

class ListPageDetailView(ListView):
    model = Buyurtmabajarish
    template_name= 'chat.html'



class Mutaxasiss(ListView):
    paginate_by = 5
    model = Mutaxasis
    template_name = "mutaxasislar.html"

class Mutaxasislar_Detail(DetailView):
    model = Mutaxasis
    template_name = 'mutaxasis_detail.html'


# Buyurtma berish uchun>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def add_buyurtma(request):
    submitted = False
    if request.method == "POST":
        form = BuyurtmaBerish(request.POST)
        if form.is_valid():
            form.save()
            return redirect('buyurtmalar')
            # return HttpResponseRedirect('/add_buyurtma?submitted=True')
    else:
        form = BuyurtmaBerish
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'buyurtma_joylashtirish.html', {'buyurtma': form, 'submitted': submitted})

class AddBuyurtma(ListView):
    model = Buyurtma
    template_name = 'buyurtma_joylashtirish.html'

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Mutaxasis elon
def add_mutaxasis(request):
    submitted = False
    if request.method == "POST":
        form = Mutaxasis_Elon(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mutaxasis')
    else:
        form = Mutaxasis_Elon
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'mutaxasis_elon.html', {'mutaxasis': form, 'submitted': submitted})


#Firma Eloni

def add_firma(request):
    submitted = False
    if request.method == "POST":
        form = Firma_Elon(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('firmalar')
    else:
        form = Firma_Elon
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'firma_elon.html', {'firma': form, 'submitted': submitted})




#chat view

def chat(request):
    return render(request, 'chat.html')


def room(request, room):
    username = request.GET.get('username') # henry
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {

        'username': username,
        'room': room,
        'room_details': room_details,
    })


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    # return HttpResponse("Hi, Message Sent Successfully!!")

def getMessages(request,  room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})
