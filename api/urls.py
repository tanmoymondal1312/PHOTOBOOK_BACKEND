from django.urls import path
from.import views


urlpatterns = [
    #path('',views.GetData)
    path('api/book', views.WhatsappBooking, name='whatsapp-booking'),
]

