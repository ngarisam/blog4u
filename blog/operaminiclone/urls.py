from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from . import views
from django.contrib.auth import views as auth_view
from . forms import ReaderLoginForm



urlpatterns = [
    path("", views.home, name="home"),
    path("<int:year>/<int:month>/<slug:val>/", views.viewpost, name="viewpost"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("sendmessage/", views.sendmessage, name="sendmessage"),
    path("category/<str:val>/", views.home, name="category"),
    path("addcomment/", views.addcomment, name="addcomment"),
    path('accounts/login/', auth_view.LoginView.as_view(template_name="operaminiclone/login.html",authentication_form=ReaderLoginForm), name='login'),
      path("register/", views.ReaderRegistrationView.as_view(), name="register"),


] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
