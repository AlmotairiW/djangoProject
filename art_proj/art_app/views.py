from django.shortcuts import render, redirect
import bcrypt
from .models import *

# Create your views here.


def index(request):
    return render(request, "index.html")


def login_reg(request):
    return render(request, "login_page.html")


def process_reg(request):

    fname = request.POST['first_name']
    lname = request.POST['last_name']
    email = request.POST['email']
    new_pass = bcrypt.hashpw(
        request.POST['password'].encode(), bcrypt.gensalt()).decode()
    if(request.POST['account_type'] == 'customer'):
        new_user = Account.objects.create(
            first_name=fname, last_name=lname, email=email, password=new_pass, is_customer=True)
        this_user = Customer.objects.create(account=new_user)

    else:
        new_user = Account.objects.create(
            first_name=fname, last_name=lname, email=email, password=new_pass, is_artist=True)
        this_user = Artist.objects.create(account=new_user)
    request.session['uid'] = this_user.account_id
    return redirect('/sucsess')


def sucsess(request):
    this_account = Account.objects.get(id=request.session['uid'])
    if this_account.is_artist:
        this_account = Artist.objects.get(account_id=request.session['uid'])
        context = {
            "this_user": Artist.objects.get(account_id=request.session['uid']),
        }
        return render(request, "artist_dashboard.html", context)
    else:  # Customer
        pass


def login(request):

    logged_user = Account.objects.get(email=request.POST['email'])
    if bcrypt.checkpw(request.POST['pass'].encode(), logged_user.password.encode()):
        request.session['uid'] = logged_user.id
        return redirect('/sucsess')


def add_item(request):
    context = {
        "this_user": Artist.objects.get(account_id=request.session['uid']),
    }
    return render(request, "add_item_1.html", context)

def create_art(request):
    art_titel = request.POST['title']
    art_desc = request.POST['Description']
    art_q = request.POST['quantity']
    art_size = request.POST['size']
    art_price = request.POST['price']

    this_art = Artwork.objects.create(title = art_titel, description = art_desc, quantity = art_q,
        size = art_size, price = art_price)
    
    this_artist = Artist.objects.get ( account_id = request.session['uid'])

    art_img_name = f'{this_art.title} image'
    art_img_alt_text = f'this image added by {this_artist.account.first_name} for {this_art.title}'

    # ArtworkImage.objects.create()
    
    

