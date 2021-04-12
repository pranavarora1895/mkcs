from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact, Newsletter, CVerify
import requests
import json
# Create your views here.


def index(request):
    if request.method == 'POST':
        fullname = request.POST.get('full-name')
        email = request.POST.get('email')
        newsletter = Newsletter(fullname=fullname, email=email)

        first_name = ""
        for letter in fullname:
            if letter == " ":
                break
            else:
                first_name += letter
        naming = {"name": first_name}

        # Recaptcha
        client_key = request.POST.get('g-recaptcha-response')
        secret_key = '6Ldx-4kaAAAAAJ4BUoqktfzjmtePdRotTQ0yUubY'
        captchaData = {
            'secret': secret_key,
            'response': client_key
        }
        r = requests.post(
            'https://www.google.com/recaptcha/api/siteverify', data=captchaData)
        response = json.loads(r.text)
        verify = response['success']
        print('Your success is: ', verify)
        if verify:
            newsletter.save()
            return render(request, 'newsletter_signup.html', naming)
        else:
            return HttpResponse('<script> alert("Please fill in the captcha")</script>')

    return render(request, 'index.html')


def contact(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        services = request.POST.get('services')
        contact_us = Contact(name=name, email=email, phone=phone,
                             message=message, services=services, date=datetime.today(), comments="")
        first_name = ""
        for letter in name:
            if letter == " ":
                break
            else:
                first_name += letter
        naming = {"name": first_name}

        # Recaptcha
        client_key = request.POST.get('g-recaptcha-response')
        secret_key = '6Ldx-4kaAAAAAJ4BUoqktfzjmtePdRotTQ0yUubY'
        captchaData = {
            'secret': secret_key,
            'response': client_key
        }
        r = requests.post(
            'https://www.google.com/recaptcha/api/siteverify', data=captchaData)
        response = json.loads(r.text)
        verify = response['success']
        print('Your success is: ', verify)
        if verify:
            contact_us.save()
            return render(request, 'submit.html', naming)
        else:
            return HttpResponse('<script> alert("Please fill in the captcha")</script>')

        # messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')


def services(request):
    if request.method == "POST":
        cverify = request.POST.get('cverify')

        client_key = request.POST.get('g-recaptcha-response')
        secret_key = '6Ldx-4kaAAAAAJ4BUoqktfzjmtePdRotTQ0yUubY'
        captchaData = {
            'secret': secret_key,
            'response': client_key
        }
        r = requests.post(
            'https://www.google.com/recaptcha/api/siteverify', data=captchaData)
        response = json.loads(r.text)
        verify = response['success']
        print('Your success is: ', verify)
        if verify:

            db_verify = CVerify.objects.filter(verify_code=cverify)
            if not db_verify:
                print("Certificate not available.")
                return HttpResponse('<script> alert("Oops!! Certificate not Verified!")</script>')
            else:
                db_cert = CVerify.objects.get(verify_code=cverify)
                cert_name = db_cert.name
                cert_classwork = db_cert.classwork
                cert_course = db_cert.course
                cert_course_code = db_cert.coursecode
                cert_start_date = db_cert.start_date
                cert_issued_date = db_cert.c_issued_date
                cert_max_marks = db_cert.cert_max_marks
                cert_marks_gain = db_cert.cert_marks_gained
                cert_pass_fail = db_cert.cert_pass_fail

                # print(cert_name, cert_classwork, cert_course, cert_issued_date)
                cert_data = {
                    "cert_verify_no": cverify,
                    "cert_name": cert_name,
                    "cert_classwork": cert_classwork,
                    "cert_course": cert_course,
                    "cert_course_code": cert_course_code,
                    "cert_start_date": cert_start_date,
                    "cert_issued_date": cert_issued_date,
                    "cert_max_marks": cert_max_marks,
                    "cert_marks_gain": cert_marks_gain,
                    "cert_pass_fail": cert_pass_fail
                }
                # print(cert_data)
                return render(request, 'verify_info.html', cert_data)
        else:
            return HttpResponse('<script> alert("Please fill in the captcha")</script>')
    return render(request, 'services.html')


def about(request):
    return render(request, 'aboutus.html')


def projects(request):
    return render(request, 'projects.html')
