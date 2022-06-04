from django.urls import path
from .views import *
from pages import views

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('mutaxasissignup/', MutaxasisSignup.as_view(),name='mutaxasissignup'),
    path('firmasignup/',FirmaSignup.as_view(),name="firmasignup"),
    path('buyurtmachisignup/',BuyurmachiSignup.as_view(),name="buyurtmachisignup"),
    path('about/', Xizmatlar.as_view(), name="about"),
    path('mutaxasis/', Mutaxasiss.as_view(), name="mutaxasis"),
    path('buyurtmalar/',Buyurtmalarss.as_view(),name="buyurtmalar"),
    path('firmalar/', Firma.as_view(), name="firmalar"),
    path('news/', Posts.as_view(), name='news'),
    path('<int:pk>/',ArticleDetailView.as_view(),name='post_detail'),

    path('<int:pk>/firma',FirmaDetail.as_view(), name='firma_detail'),

    path('<int:pk>/m',Mutaxasislar_Detail.as_view(),name='mutaxasis_detail'),
    
    path('<int:pk>/list',ListDetailView.as_view(),name='list_detail'),
    path('list/bajarish',ListPageDetailView.as_view(),name='buyurtma_detail'),
    path('login/', LoginPage.as_view(), name='login'),
    path('profile/', Profile.as_view(), name='profile'),
    
    path('addbuyurtma/', views.add_buyurtma, name='addbuyurtma'),
    path('addmutaxasis/', views.add_mutaxasis, name='addmutaxasis'),
    path('addfirma/',views.add_firma, name='addfirma'),

    path('elon', SignUpMenu.as_view(), name='chooseone'),
    #chat url
    path('chat/', views.chat, name="chat"),
    path('<str:room>/', views.room, name="room"),
    path('list/checkview', views.checkview, name="checkview"),
    path('send', views.send, name="send"),
    path('getMessages/<str:room>/', views.getMessages, name="getMessages")
]