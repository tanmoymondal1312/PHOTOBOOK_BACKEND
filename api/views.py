from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from twilio.rest import Client
from django.conf import settings
from Datas.models import Booking
from django.utils import timezone
import pytz


@api_view(['POST'])
def WhatsappBooking(request):
    name = request.data.get('name')
    service = request.data.get('service')
    number = request.data.get('number')
#Added Extra Thing
    if not name :
        return Response({'error': 'Name are required ha ha'}, status=400)
    if not service:
        return Response({'error': 'Service are required ha ha'}, status=400)
    if not number:
        return Response({'error': 'Number are required ha ha'}, status=400)

    account_sid = 'AC1fe2ee83b43856d902b415a9273b8c31'
    auth_token = '4140346b75cf194759719a5a245c6cf3'
    client = Client(account_sid, auth_token)
    tz = pytz.timezone('Asia/Dhaka')
    

    
    booking = Booking.objects.create(
            name=name,
            service=service,
            number=number,
            created_at=timezone.now().astimezone(tz) 
            

        )
    print("Record Created")
    message_body = f"Id-:{booking.id}\n---Booking Details---\nName: {name}\nMessage: {service}\nNumber: {number}\n Booked At:{booking.created_at}"    
    try:
        message = client.messages.create(
           from_='whatsapp:+14155238886',
           body=message_body,
           to='whatsapp:+8801736008374'
          
          )
        print("Not Try Error")
        booking.whatsapp_message_sent = True
        booking.save()

        return Response({'message': 'Booking successful'}, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=500)
