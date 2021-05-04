from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, "index.html")




#customer
# -artwork info
# -write review
# -artist bio

def artwork_info(request ,artwork_id):
    if request.session['login']=True:
        this_customer=Customer.objects.get(id=request.session['logged_in_id'])
    else:
        this_customer=null #if login>true,use "this_cus"else:redirect to login if need

    context = {
        "this_customer" : this_customer,
        "reviews" : Artwork.objects.get(id=artwork_id).reviews,
        "this_artwork" : Artwork.objects.get(id=artwork_id)
    }
     return render(request, 'artwork_info.html', context)

# check quantity in html ,if not should be here
# assume 
def buy_artwork(request,artwork_id)
    this_customer=Customer.objects.get(id=request.session['logged_in_id'])
    this_artwork=Artwork.objects.get(id=artwork_id)
    if this_artwork.quantity >= request.POST['quantity']:
        this_artwork.quantity=this_artwork.quantity-request.POST['quantity']
        this_customer.purchases.add(this_artwork)
        return render(request, "completed_purchases.html")
    else:
        return redirect(f'/artwork_info/{artwork_id}')

# submit btn for review valid for logged-in +iscustomer+artwork in purchases
# could add rating with review
def add_review(request,artwork_id)
    this_customer=Customer.objects.get(id=request.session['logged_in_id'])
    this_artwork=Artwork.objects.get(id=artwork_id)
    the_review_txt=request.POST['review']
    this_review=Review.objects.create(review_txt=the_review_txt,artwork=this_artwork,customer=this_customer)
    this_artwork.reviews.add(this_review)

def show_artist_profile(request,artist_id):
    context = {
        "this_artist": Artist.objects.get(id=artist_id),
    }
    return render(request, "artist_profile.html", context)
    # #####