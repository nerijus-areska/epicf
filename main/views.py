from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


from .models import Question, Player
from .model.Items import ALL_ITEMS, EQ_SLOT, ARMOR_SLOTS


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            player = Player()
            player.user = user
            player.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def items(request):
    context = {
        'ALL_ITEMS': ALL_ITEMS,
        'EQ_SLOT': EQ_SLOT,
        'ARMOR_SLOTS': ARMOR_SLOTS,
        'equiped_items': request.user.player.equiped_item_map()
    }
    return render(request, 'items.html', context)

def shop(request):
    context = {
        'ALL_ITEMS': ALL_ITEMS,
        'EQ_SLOT': EQ_SLOT,
        'equiped_items': request.user.player.equiped_item_map(),
    }
    return render(request, 'shop.html', context)

def base(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'main/first.html', context)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)