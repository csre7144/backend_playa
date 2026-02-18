from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from .models import RequestCall
from .forms import RequestCallForm
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags



# Create your views here.
def home(request):

    if request.method == "POST":
        try:     
            fullname = request.POST.get("fullname")
            email = request.POST.get("email")
            phone_number = request.POST.get("phone_number")
            subject = request.POST.get("subject")
            msg = request.POST.get("message")
            # Save to database
            data = RequestCall.objects.create(
                fullname=fullname,
                email=email,
                phone_number=phone_number,
                subject=subject,
                message=msg
            )

            # ================= HTML EMAIL =================
            html_content = f"""
            <!DOCTYPE html>
            <html>
            <body style="font-family: Arial; font-size:16px; background:#f4f4f4; padding:20px;">
                <div style="background:#ffffff; padding:20px; border-radius:8px;">
                    
                    <div style="text-align:center;">
                        <h2 style="color:#2c3e50;">New Request Call</h2>
                    </div>

                    <table width="100%" cellpadding="10" cellspacing="0" border="1" style="border-collapse:collapse;">
                        <tr><th align="left">Full Name</th><td>{fullname}</td></tr>
                        <tr><th align="left">Email</th><td>{email}</td></tr>
                        <tr><th align="left">Phone</th><td>{phone_number}</td></tr>
                        <tr><th align="left">Subject</th><td>{subject}</td></tr>
                        <tr><th align="left">Message</th><td>{msg}</td></tr>
                    </table>

                    <div style="margin-top:20px; font-size:14px; color:#777; text-align:center;">
                        © 2026 Playa Pharmacy<br>
                        Email: info@playapharmacy.com<br>
                        Phone: +1 (310) 823-4500 | Fax: +1 (310) 823-5700
                    </div>

                </div>
            </body>
            </html>
            """

            text_content = strip_tags(html_content)

            email_message = EmailMultiAlternatives(
                subject=f"New Request Call: {subject}",
                body=text_content,
                from_email=settings.EMAIL_HOST_USER,
                to=['chintu81400@gmail.com'],
            )

            email_message.attach_alternative(html_content, "text/html")
            email_message.send()

            # Store data in session (for redirect)
            request.session['submitted_data'] = {
                'fullname': fullname,
                'email': email,
                'phone_number': phone_number,
                'subject': subject,
                'message': msg
            }

            messages.success(request, "Your application has been submitted successfully!")
            

            return redirect('home')

        except Exception as e:
            messages.error(request, f"Error: {e}")
            return redirect('home')

    # GET request
    submitted_data = request.session.pop('submitted_data', None)

    return render(request, 'Fontend_Playa/index.html', {
        'submitted_data': submitted_data
    })

def about(request):
    return render(request, 'Fontend_Playa/about.html')

def compounding(request):
    return render(request, 'Fontend_Playa/compounding.html')

def provider(requset):
    return render(requset, 'Fontend_Playa/provider.html')

def transfer(request):
    return render(request, 'Fontend_Playa/transfer.html')

def contact(request):
    return render(request, 'Fontend_Playa/contact2.html')

def methylene(request):
    return render(request, 'Fontend_Playa/methylene.html')

def pain_management(request):
    return render(request, 'Fontend_Playa/Pain_Management.html')

def hormone(request):
    return render(request, 'Fontend_Playa/hormone.html')

def sleep_aids(request):
    return render(request, 'Fontend_Playa/sleep_aids.html')

def weight_management(request):
    return render(request, 'Fontend_Playa/weight_management.html')


def pet_medicine(request):
    return render(request, 'Fontend_Playa/pet_medicine.html')


def nutriceuticals(request):
    return render(request, 'Fontend_Playa/nutriceuticals.html')


def adrenal_fatigue(request):
    return render(request, 'Fontend_Playa/adrenal_fatigue.html')

def dermatology(request):
    return render(request, 'Fontend_Playa/dermatology.html')


def additional_expertise(request):
    return render(request, 'Fontend_Playa/additional_expertise.html')



# Dashboard Backend
def dashboard(request):
    return render(request, 'Dashboard_Playa/dashboard.html')

def request_call(request):
    data = RequestCall.objects.all()
    return render(request, 'Dashboard_Playa/Request_Call_Patient.html', {'data':data})

def add_request_call(request):
    if request.method == 'POST':    
        form = RequestCallForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('request_call')  # your table page name
    else:
        form = RequestCallForm()

    return render(request, 'Dashboard_Playa/add_request_call.html', {'form': form})

def edit_request_call(request, pk):
    request_call = get_object_or_404(RequestCall, pk=pk)

    if request.method == 'POST':
        # Get form data
        request_call.fullname = request.POST.get('fullname')
        request_call.email = request.POST.get('email')
        request_call.phone_number = request.POST.get('phone_number')
        request_call.subject = request.POST.get('subject')
        request_call.message = request.POST.get('message')

        request_call.save()
        messages.success(request, 'Request call updated successfully.')
        return redirect('request_call')  # Redirect to your list/dashboard page

    # GET request - show form pre-filled
    return render(request, 'Dashboard_Playa/edit_request_call.html', {'request_call': request_call})

# Delete 

def delete_request_call(request, pk):
    obj = get_object_or_404(RequestCall, pk=pk)
    if request.method == "POST":
        obj.delete()
        messages.success(request, 'Request call deleted successfully.')
        return redirect('request_call')
    return redirect('request_call')



def task_management(request):
    return render(request, 'Dashboard_Playa/Task_Mangement.html')

def contact_information(request):
    return render(request, 'Dashboard_Playa/contact_information.html')

def contact_form(request):
    return render(request, 'Dashboard_Playa/contact_form.html')

def transfer_rx(request):
    return render(request, 'Dashboard_Playa/transfer_rx.html')
