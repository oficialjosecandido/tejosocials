from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db.models import Q
from EmployeeApp.models import Departments, Employees
from EmployeeApp.serializers import *
from django.core.files.storage import default_storage
from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage
from django.template.loader import get_template
from django.conf import settings


# Create your views here.
@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)

    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(
            DepartmentId=department_data['DepartmentId'])
        department_serializer = DepartmentSerializer(
            department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        department = Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        employees = Employees.objects.order_by('-DateOfJoining')
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)

    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = addEmployeeSerializer(data=employee_data)
        # print('cheugue aqui?', employee_data['EmployeeId'])
        rec_email = employee_data['Email']
        rec_name = employee_data['EmployeeName']
        # rec_id = employee_data['EmployeeId']
        if employee_serializer.is_valid():
            employee_serializer.save()
            # send email
            html_tpl_path = 'auctions/email_templates/profile_success.html'
            context_data = {'name': rec_name}
            email_html_template = get_template(
                html_tpl_path).render(context_data)
            receiver_email = rec_email
            email_msg = EmailMessage('TEJO IT JOBS | Your Profile was Published',
                                     email_html_template,
                                     settings.EMAIL_HOST_USER,
                                     [receiver_email],
                                     reply_to=[settings.EMAIL_HOST_USER]
                                     )
            email_msg.content_subtype = 'html'
            email_msg.send(fail_silently=False)

            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(
            EmployeeId=employee_data['EmployeeId'])
        employee_serializer = updateSerializer(employee, data=employee_data)
        rec_email = employee_data['Email']
        rec_name = employee_data['EmployeeName']
        rec_id = employee_data['EmployeeId']

        if employee_serializer.is_valid():
            employee_serializer.save()

            # send email
            html_tpl_path = 'auctions/email_templates/update_success.html'
            context_data = {'name': rec_name, 'id': rec_id}
            email_html_template = get_template(
                html_tpl_path).render(context_data)
            receiver_email = rec_email
            email_msg = EmailMessage('TEJO IT JOBS | Profile updated',
                                     email_html_template,
                                     settings.EMAIL_HOST_USER,
                                     [receiver_email],
                                     reply_to=[settings.EMAIL_HOST_USER]
                                     )
            email_msg.content_subtype = 'html'
            email_msg.send(fail_silently=False)

            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        print('qual é o meu id?', id)
        employee = Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)


@csrf_exempt
def detailEmployeeApi(request, id):
    if request.method == 'GET':
        employee = Employees.objects.filter(EmployeeId=id)
        for i in employee:
            i.Views = i.Views + 1
            i.save()
        employees_serializer = EmployeeSerializer(employee, many=True)
        return JsonResponse(employees_serializer.data, safe=False)


@csrf_exempt
def getThisEmployeeApi(request, id):
    if request.method == 'GET':
        employee = Employees.objects.filter(EmployeeId=id)
        employees_serializer = EmployeeSerializer(employee, many=True)
        return JsonResponse(employees_serializer.data, safe=False)


@csrf_exempt
def departmentEmployeeApi(request, id):
    department = Departments.objects.get(DepartmentId=id)
    if department:
        depName = department.DepartmentName
    else:
        return JsonResponse("Not Found", safe=False)

    if request.method == 'GET':
        employees = Employees.objects.filter(Department=depName)
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)


@csrf_exempt
def techsApi(request):
    techs = Tech.objects.all()
    tech_serializer = techSerializer(techs, many=True)
    return JsonResponse(tech_serializer.data, safe=False)


@csrf_exempt
def techEmployeeApi(request, id):
    tech = Tech.objects.get(TechId=id)
    if tech:
        techName = tech.TechName
    else:
        return JsonResponse("Not Found", safe=False)

    if request.method == 'GET':
        employees = Employees.objects.filter(Primary_Tech=techName)
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)


@csrf_exempt
def getSoftReportApi(request):
    employee_data = JSONParser().parse(request)
    employee_serializer = employeeSoftSerializer(data=employee_data)
    rec_email = employee_data['softEmail']
    rec_name = employee_data['softName']
    if employee_serializer.is_valid():
        employee_serializer.save()
        # send email
        html_tpl_path = 'auctions/email_templates/profile_success.html'
        context_data = {'name': rec_name}
        email_html_template = get_template(html_tpl_path).render(context_data)
        receiver_email = rec_email
        email_msg = EmailMessage('TEJO IT JOBS | Your Profile was Published',
                                 email_html_template,
                                 settings.EMAIL_HOST_USER,
                                 [receiver_email],
                                 reply_to=[settings.EMAIL_HOST_USER]
                                 )
        email_msg.content_subtype = 'html'
        email_msg.send(fail_silently=False)

        return JsonResponse("Requested Successfully!!", safe=False)
    return JsonResponse("Failed to Request.", safe=False)


@csrf_exempt
def getTechReportApi(request):
    employee_data = JSONParser().parse(request)
    employee_serializer = employeeTechSerializer(data=employee_data)
    print('cheugue aqui?', employee_data['EmployeeId'])
    rec_email = employee_data['techEmail']
    rec_name = employee_data['techName']
    if employee_serializer.is_valid():
        employee_serializer.save()
        # send email
        html_tpl_path = 'auctions/email_templates/profile_success.html'
        context_data = {'name': rec_name}
        email_html_template = get_template(html_tpl_path).render(context_data)
        receiver_email = rec_email
        email_msg = EmailMessage('TEJO IT JOBS | Your Profile was Published',
                                 email_html_template,
                                 settings.EMAIL_HOST_USER,
                                 [receiver_email],
                                 reply_to=[settings.EMAIL_HOST_USER]
                                 )
        email_msg.content_subtype = 'html'
        email_msg.send(fail_silently=False)

        return JsonResponse("Requested Successfully!!", safe=False)
    return JsonResponse("Failed to Request.", safe=False)


@csrf_exempt
def getChatsApi(request):

    if request.method == 'GET':
        chats = Message.objects.all().order_by('-sendDate')
        chat_serializer = chatSerializer(chats, many=True)
        return JsonResponse(chat_serializer.data, safe=False)


@csrf_exempt
def markReadAPI(request):
    message_data = JSONParser().parse(request)
    message = Message.objects.get(messageId=message_data['messageId'])
    conversation_serializer = messageStatusSerializer(
        message, data=message_data)
    if conversation_serializer.is_valid():
        conversation_serializer.save()
        return JsonResponse("Updated", safe=False)
    return JsonResponse("Failed to Update.", safe=False)


@csrf_exempt
def replyMessageAPI(request):

    reply_data = JSONParser().parse(request)
    reply_serializer = chatSerializer(data=reply_data)

    rec_email = reply_data['receiverEmail']
    rec_name = reply_data['receiverName']
    if reply_serializer.is_valid():
        reply_serializer.save()
        # send email
        """
        html_tpl_path = 'auctions/email_templates/profile_success.html'
        context_data =  {'name': rec_name}
        email_html_template = get_template(html_tpl_path).render(context_data)
        receiver_email = rec_email
        email_msg = EmailMessage('TEJO IT JOBS | Your Profile was Published', 
                                    email_html_template, 
                                    settings.EMAIL_HOST_USER,
                                    [receiver_email],
                                    reply_to=[settings.EMAIL_HOST_USER]
                                    )
        email_msg.content_subtype = 'html'
        email_msg.send(fail_silently=False)
        """
        return JsonResponse("Replied Successfully!!", safe=False)
    return JsonResponse("Failed to Reply.", safe=False)


@csrf_exempt
def sendMessageAPI(request):

    send_data = JSONParser().parse(request)
    send_serializer = chatSerializer(data=send_data)

    sender = send_data['senderName']
    rec_name = send_data['receiverName']
    rec_email = send_data['receiverEmail']
    message = send_data['message']

    if send_serializer.is_valid():
        send_serializer.save()

        html_tpl_path = 'auctions/email_templates/new_message.html'
        context_data = {'name': rec_name, 'sender': sender, 'message': message}
        email_html_template = get_template(html_tpl_path).render(context_data)
        receiver_email = rec_email
        email_msg = EmailMessage('TEJO IT JOBS | You received a Message ',
                                 email_html_template,
                                 settings.EMAIL_HOST_USER,
                                 [receiver_email],
                                 reply_to=[settings.EMAIL_HOST_USER]
                                 )
        email_msg.content_subtype = 'html'
        email_msg.send(fail_silently=False)

        return JsonResponse("Message Sent!!", safe=False)
    return JsonResponse("Failed to Reply.", safe=False)


@csrf_exempt
def getMessagesAPI(request, id):

    if request.method == 'GET':
        conversation = Message.objects.get(messageId=id)
        conversation_serializer = conversationSerializer(chats, many=True)
        return JsonResponse(conversation_serializer.data, safe=False)

    elif request.method == 'PUT':
        chat_data = JSONParser().parse(request)
        chat = Chat.objects.get(messageId=chat_data['messageId'])
        conversation_serializer = conversationSerializer(
            employee, data=chat_data)
        email = employee_data['receiverEmail']
        name = employee_data['senderEmail']
        id = employee_data['messageId']

        if conversationSerializer.is_valid():
            conversationSerializer.save()

            # send email
            html_tpl_path = 'auctions/email_templates/update_success.html'
            context_data = {'name': name, 'id': id}
            email_html_template = get_template(
                html_tpl_path).render(context_data)
            receiver_email = rec_email
            email_msg = EmailMessage('TEJO IT JOBS | New Message',
                                     email_html_template,
                                     settings.EMAIL_HOST_USER,
                                     [receiver_email],
                                     reply_to=[settings.EMAIL_HOST_USER]
                                     )
            email_msg.content_subtype = 'html'
            email_msg.send(fail_silently=False)

            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)


@csrf_exempt
def contactApi(request, id=0):

    if request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = addContactSerializer(data=employee_data)
        rec_email = employee_data['senderEmail']
        rec_name = employee_data['senderName']
        rec_message = employee_data['senderMessage']
        rec_sku = employee_data['senderSKU']

        print(rec_email, rec_name, rec_sku)

        if rec_sku:
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

        else:
            if employee_serializer.is_valid():
                employee_serializer.save()
            # send email
            html_tpl_path = 'auctions/email_templates/profile_success.html'
            context_data = {'name': rec_name, 'message': rec_message}
            email_html_template = get_template(
                html_tpl_path).render(context_data)
            receiver_email = rec_email
            email_msg = EmailMessage('TEJO IT JOBS | Your Contact was sent',
                                     email_html_template,
                                     settings.EMAIL_HOST_USER,
                                     [receiver_email],
                                     reply_to=[settings.EMAIL_HOST_USER]
                                     )
            email_msg.content_subtype = 'html'
            email_msg.send(fail_silently=False)

            return JsonResponse("Contact request sent successfully!!", safe=False)
        return JsonResponse("Failed to send request.", safe=False)


@csrf_exempt
def newsletterApi(request, id=0):

    if request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = addNewsletterSerializer(data=employee_data)
        rec_email = employee_data['senderEmail']
        print(rec_email)

        if employee_serializer.is_valid():
            employee_serializer.save()
        # send email
        html_tpl_path = 'auctions/email_templates/newsletter.html'
        context_data = {'name': 'Anonymous Guest'}
        email_html_template = get_template(html_tpl_path).render(context_data)
        receiver_email = rec_email
        email_msg = EmailMessage('TEJO IT JOBS | Added to the Newsletter List',
                                 email_html_template,
                                 settings.EMAIL_HOST_USER,
                                 [receiver_email],
                                 reply_to=[settings.EMAIL_HOST_USER]
                                 )
        email_msg.content_subtype = 'html'
        email_msg.send(fail_silently=False)
        return JsonResponse("Added to our Newslettter!!", safe=False)
