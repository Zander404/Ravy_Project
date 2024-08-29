from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, SignUpForm
from .models import Post


# Create your views here.

## Rota de Registro
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redireciona para a página inicial ou outra URL após o registro
    else:
        form = SignUpForm()
    return render(request, 'registration/registrate.html', {'form': form})


# Rota inicial
def index(request):
    poems = Post.objects.all()
    return render(request, 'blog/index.html', context={'poemas': poems})


# Rota de Usuário visualizar o Poema
def read_more(request, pk):
    poetry = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/poems.html', context={'poema': poetry})


def contact(request):
    return render(request, 'blog/contact.html')


def about(request):
    return render(request, 'blog/about_me.html')


## Rota de Poemas
@login_required(login_url='/login')
def add_poetry(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'blog/crud/forms.html', {'form': form})


@login_required(login_url='/login')
def edit_poetry(request, pk):
    # Carrega o post a ser editado
    post = get_object_or_404(Post, id=pk)

    if request.method == 'POST':
        # Se o formulário for enviado, preencha-o com os dados do POST
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()  # Salva as alterações
            return redirect('post_detail', post_id=post.id)  # Redireciona para a página de detalhes do post
    else:
        # Se o formulário não foi enviado, exiba o formulário com os dados do post
        form = PostForm(instance=post)

    return render(request, 'blog/crud/forms.html', {'form': form, 'post': post})


@login_required(login_url='/login')
def delete_poetry(request, pk):
    post = get_object_or_404(Post, id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'blog/poems.html', {'post': post})
