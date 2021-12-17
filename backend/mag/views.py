from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db.models import Q
from mag.models import *
from mag.serializers import *
from django.core.files.storage import default_storage
from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage
from django.template.loader import get_template
from django.conf import settings
from . import forms


# Create your views here.
@csrf_exempt
def getPostsAPI(request, id=0):
    posts = Post.objects.order_by('-date')
    posts_serializer = PostsSerializer(posts, many=True)
    return JsonResponse(posts_serializer.data, safe=False)


@csrf_exempt
def getPostsThisAPI(request, key):
    posts = Post.objects.filter(tag=key).order_by('-date')
    posts_serializer = PostsSerializer(posts, many=True)
    return JsonResponse(posts_serializer.data, safe=False)


# Create your views here.
@csrf_exempt
def getThisPostAPI(slug):
    print('chegamos aqui')
    post = Post.objects.filter(slug=slug)
    print(slug)
    posts_serializer = PostsSerializer(post, many=True)
    return JsonResponse(posts_serializer.data, safe=False)


@csrf_exempt
def contactApi(request, id=0):

    if request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = addContactSerializer(data=employee_data)
        rec_email = employee_data['senderEmail']
        rec_name = employee_data['senderName']
        rec_message = employee_data['senderMessage']

        print(rec_email, rec_name)

        if employee_serializer.is_valid():
            employee_serializer.save()
        # send email
        """
        html_tpl_path = 'auctions/email_templates/delete.html'
        context_data = {'name': rec_name}
        email_html_template = get_template(
            html_tpl_path).render(context_data)
        receiver_email = rec_email
        email_msg = EmailMessage('TEJO IT JOBS | Your Delete was sent',
                                    email_html_template,
                                    settings.EMAIL_HOST_USER,
                                    [receiver_email],
                                    reply_to=[settings.EMAIL_HOST_USER]
                                    )
        email_msg.content_subtype = 'html'
        email_msg.send(fail_silently=False)
        """

        return JsonResponse("Delete request sent successfully!!", safe=False)

    return JsonResponse("Failed to send request.", safe=False)
