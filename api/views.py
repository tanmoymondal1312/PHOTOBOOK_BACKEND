from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from twilio.rest import Client
from django.conf import settings
from Datas.models import Booking
from django.utils import timezone
import pytz
import environ
from twilio.rest import Client

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()


@api_view(['POST'])
def WhatsappBooking(request):
    name = request.data.get('name')
    service = request.data.get('service')
    number = request.data.get('number')

    if not name or not service or not number:
        return Response({'error': 'All fields are required'}, status=400)

   
    client = Client(env('TWILIO_ACCOUNT_SID'), env('TWILIO_AUTH_TOKEN'))
    tz = pytz.timezone('Asia/Dhaka')
    

    
    booking = Booking.objects.create(
            name=name,
            service=service,
            number=number,
            created_at=timezone.now().astimezone(tz) 
            

        )
    message_body = f"Id-:{booking.id}\n---Booking Details---\nName: {name}\nService: {service}\nNumber: {number}\n Booked At:{booking.created_at}"    
    try:
        message = client.messages.create(
           from_='whatsapp:+14155238886',
           body=message_body,
           to='whatsapp:+8801736008374'
          )
        booking.whatsapp_message_sent = True
        booking.save()

        return Response({'message': 'Booking successful'}, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=500)
