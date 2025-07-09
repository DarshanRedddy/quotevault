from django.shortcuts import render, redirect, get_object_or_404
from .models import Quote, Tag
from django.contrib.auth.decorators import login_required


def home(request):
    quotes = Quote.objects.all()
    tags = Tag.objects.all()
    return render(request, 'home.html', {'quotes': quotes, 'tags': tags})


def quotes_by_tag(request, tag_id):
    quotes = Quote.objects.filter(tag_id=tag_id)
    tags = Tag.objects.all()
    return render(request, 'home.html', {'quotes': quotes, 'tags': tags})


@login_required
def add_quote(request):
    if request.method == 'POST':
        text = request.POST['text']
        author = request.POST['author']
        tag_id = request.POST['tag']
        Quote.objects.create(text=text, author=author, tag_id=tag_id)
        return redirect('home')
    tags = Tag.objects.all()
    return render(request, 'add.html', {'tags': tags})


@login_required
def edit_quote(request, quote_id):
    quote = get_object_or_404(Quote, id=quote_id)
    if request.method == 'POST':
        quote.text = request.POST['text']
        quote.author = request.POST['author']
        quote.tag_id = request.POST['tag']
        quote.save()
        return redirect('home')
    tags = Tag.objects.all()
    return render(request, 'edit.html', {'quote': quote, 'tags': tags})


@login_required
def delete_quote(request, quote_id):
    quote = get_object_or_404(Quote, id=quote_id)
    quote.delete()
    return redirect('home')
from django.shortcuts import render, get_object_or_404, redirect
from .models import Quote, Tag

# Other functions ...

def edit_quote(request, quote_id):
    quote = get_object_or_404(Quote, id=quote_id)
    if request.method == 'POST':
        quote.text = request.POST['text']
        quote.author = request.POST['author']
        quote.tag_id = request.POST['tag']
        quote.save()
        return redirect('home')
    tags = Tag.objects.all()
    return render(request, 'edit.html', {'quote': quote, 'tags': tags})
