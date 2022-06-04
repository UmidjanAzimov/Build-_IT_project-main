from django.urls import path
from .views import AddUserSignUp, AddUserSignUp1, AddUserSignUp2

urlpatterns = [
    path('addsignup/', AddUserSignUp.as_view(), name='addsign'),
    path('addsignup1/', AddUserSignUp1.as_view(), name='addsign1'),
    path('addsignup2/', AddUserSignUp2.as_view(), name='addsign2'),
]
