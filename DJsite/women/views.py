from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, FormView
from  django.urls import reverse_lazy
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login



#def index(request): # reference to http//request
 #   posts = Women.objects.all()
  #  context = {'menu': menu,
   #            'title': "Главная страница",
    #           'cat_selected': 0
     #          }
    #return render(request, 'women/index.html', context=context)

class WomenHome(DataMixin, ListView):
    model = Women # takes all entries from the table and displays it as a list
    template_name = 'women/index.html' # reference to tamplate
    context_object_name = 'posts' # creation of list of data
    #extra_context = {'title': 'Главная страница'} # static context

    def get_context_data(self, *, object_list=None, **kwargs): # dynamic context
        context = super().get_context_data(**kwargs) # to get whole shaped context from ListView
        c_def = self.get_user_context(title = 'Главная страница') # call of basic class method
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self): # only published entries are Displayed (defines the sample of returned data)
        return Women.objects.filter(is_published=True).select_related('cat') # Greedy Request that returns besides published data data from category table

class WomenCategory(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False #for 404 the page is not found

    def get_queryset(self): # our query
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(c.name),
                                      cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))

# def show_category(request, cat_id):
#     posts = Women.objects.filter(cat_id=cat_id)
#     if len(posts) == 0:
#         raise Http404()
#     context = {'posts': posts,
#                'menu': menu,
#                'title': "Отоброжение по рубрикам",
#                'cat_selected': cat_id
#                }
#     return render(request, 'women/index.html', context=context)

@login_required # for authtorized users
def about(request): # reference to http//request
    contact_list = Women.objects.all()
    paginator = Paginator(contact_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) # list of objects for current page
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте', 'page_obj': page_obj})

class AddPage(LoginRequiredMixin, DataMixin, CreateView): # This class works with forms
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home') #Redicrect to a special page after adding a new arcticle
    login_url = reverse_lazy('home') #a path for an unauthorized user

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def=self.get_user_context(title='Добавление статьи')
        return dict(list(c_def.items()) + list(context.items()))


# def addpage(request):
#     if request.method == 'POST': # if data are filled, we take them from POST
#         form = AddPostForm(request.POST, request.FILES) # for form display with filled data by user # Creating a form to add an article.
#         if form.is_valid(): # validation
#             #print(form.cleaned_data)
#             form.save() #This method creates and saves a database object from the data bound to the form.
#             return redirect('home')
#             '''alternative way:
#             try:
#                 Women.objects.create(**form.cleaned_data)
#                 return redirect('home')
#             except:
#                 form.add_error(None, "Ошибка добавления поста")'''
#
#     else:
#         form = AddPostForm()
#     return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


def contact(request):
    return HttpResponse("Обратная связь")

class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'women/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Обратная связь')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form): # If registration form is ok, then this method starts working
        print(form.cleaned_data)
        return redirect('home')

# def login(request):
#     return HttpResponse("Авторизация")

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'women/register.html'
    success_name = 'women/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form): # If registration form is ok, then this method starts working
        user = form.save() # add user in db by self
        login(self.request, user) # Autenticate user
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'women/login.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self): # if login and password are correct this function works
        return reverse_lazy('home') # redirect to home


class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug' #key for url
    context_object_name = 'post'
    #pk_utl_kwarg = 'post_pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(c_def.items()) + list(context.items()))

def logout_user(request):
    logout(request)
    return redirect('login')

# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug) #check if there are any woman in dictionary
#
#     context = {'post': post,
#                'menu': menu,
#                'title': "post.title",
#                'cat_selected': post.cat_id,
#                }
#     return render(request, 'women/post.html', context=context)

def pageNotFound(request, excpetion):
    return HttpResponseNotFound('<h1> The page is not found</h>')

