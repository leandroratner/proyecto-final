from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from turismo_arg.models import Post, Mensaje, Avatar
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from turismo_arg.forms import UsuarioForm
from django.contrib.auth.admin import User
from django.contrib.messages.views import SuccessMessageMixin


def index(request):
    posts = Post.objects.order_by('-publicado_el').all()
    return render(request, "turismo_arg/index.html", {"posts":posts})

class PostDetalle(DetailView):
    model = Post

class PostList(ListView):
    model = Post
    
class PostCrear(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("turismo-arg-listar")
    fields = '__all__'

class PostBorrar(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("turismo-arg-listar")

class PostActualizar(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("turismo-arg-listar")
    fields = '__all__'

class UserSignUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('turismo-arg-listar')

class UserLogin(LoginView):
    next_page = reverse_lazy('turismo-arg-listar')

class UserLogout(LogoutView):
    next_page = reverse_lazy('turismo-arg-listar')


class MensajeDetalle(DetailView):
    model = Mensaje

class MensajeListar(LoginRequiredMixin, ListView):
    model = Mensaje  

class MensajeCrear(SuccessMessageMixin, CreateView):
    model = Mensaje
    success_url = reverse_lazy("turismo-arg-mensajes-crear")
    fields = ['nombre', 'email', 'texto']
    success_message = "Mensaje enviado!"

class MensajeBorrar(LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy("turismo-arg-mensajes-listar")

class UserActualizar(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('turismo-arg-listar')

class AvatarActualizar(UpdateView):
    model = Avatar
    fields = ['imagen']
    success_url = reverse_lazy('turismo-arg-listar')

