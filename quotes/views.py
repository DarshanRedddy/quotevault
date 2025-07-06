from django.shortcuts import render, redirect
from .models import Quote, Tag
# Import models to get data from DB

def home(request):
    quotes = Quote.objects.all()    # Fetch all quotes
    tags = Tag.objects.all()        # Fetch all tags
    return render(request, 'home.html', {'quotes': quotes, 'tags': tags})
from django.shortcuts import render, redirect
from .models import Quote, Tag

def add_quote(request):
    tags = Tag.objects.all()

    if request.method == 'POST':
        text = request.POST['text']
        author = request.POST['author']
        tag_id = request.POST['tag']
        tag = Tag.objects.get(id=tag_id)

        # Save the new quote
        Quote.objects.create(text=text, author=author, tag=tag)

        return redirect('home')  # Redirect to homepage after saving

    return render(request, 'add_quote.html', {'tags': tags})
