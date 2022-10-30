from django.shortcuts import render, redirect, get_object_or_404
from .models import Board
from .forms import BoardForm


def index(request):
    boards = Board.objects.all()
    context = {
        'boards': boards,
    }
    return render(request, 'boards/index.html', context)


def create(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.creator = request.user
            board.save()
            return redirect('boards:index')
    else:
        form = BoardForm()
    context = {
        'form': form,
    }
    return render(request, 'boards/create.html', context)


def detail(request, pk):
    board = get_object_or_404(Board, pk=pk)
    players = board.play_users.all()
    context = {
        'board': board,
        'players': players,
    }
    return render(request, 'boards/detail.html', context)


def play(request, pk):
    if request.user.is_authenticated:
        board = get_object_or_404(Board, pk=pk)
        if board.play_users.filter(pk=request.user.pk).exists():
            board.play_users.remove(request.user)
        else:
            board.play_users.add(request.user)
        return redirect('boards:index')
    return redirect('accounts:login')
