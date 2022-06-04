from django import forms
from django.forms import ModelForm
from .models import Buyurtmachi, Mutaxasis, Firmalar, Buyurtma

class BuyurtmachiForm(forms.ModelForm):
    class Meta:
        model = Buyurtmachi
        fields = "__all__"
        
class MutaxassisForm(forms.ModelForm):
    class Meta:
        model = Mutaxasis
        fields = "__all__"
        
class FirmaForm(forms.ModelForm):
    class Meta:
        model = Firmalar
        fields = "__all__"

class BuyurtmaBerish(forms.ModelForm):
    class Meta:
        model = Buyurtma
        fields = ('title_buyurtma', 'body_buyurtma', 'price_buyurtma', 'muddat', 'telefon_raqam', 'aloqa_uchun_email_manzil','room_name','username','telegram')

class Mutaxasis_Elon(forms.ModelForm):
    class Meta:
        model = Mutaxasis
        fields = '__all__'
        
class Firma_Elon(forms.ModelForm):
    class Meta:
        model = Firmalar
        # fields = "__all__"
        fields = ('nomi', 'yonalish', 'litsenzya', 'ishchi_soni', 'portfolio', 'logotip', 'mobile_number', 'email_address', 'telegram_address')
        