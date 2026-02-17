from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from .models import RequestCall
from .forms import RequestCallForm
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string



# Create your views here.
def home(request):
    if request.method == 'POST':
        try:
            fullname = request.POST['fullname']
            email = request.POST['email']
            phone_number = request.POST['phone_number']
            subject = request.POST['subject']
            msg = request.POST['message']
            data = RequestCall(fullname=fullname, email=email, phone_number=phone_number, subject=subject, message=msg)
            data.save()

            html_content = f"""
            <html>
            <body>
                <h2>New Request Call</h2>
                <table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse;">
                    <tr>
                        <th align="left">Full Name</th>
                        <td>{fullname}</td>
                    </tr>
                    <tr>
                        <th align="left">Email</th>
                        <td>{email}</td>
                    </tr>
                    <tr>
                        <th align="left">Phone Number</th>
                        <td>{phone_number}</td>
                    </tr>
                    <tr>
                        <th align="left">Message</th>
                        <td>{msg}</td>
                    </tr>
                </table>
            </body>
            </html>
            """

            # Send Email to Admin
            send_mail(
                subject=f"New Request Call: {subject}",
                message=f"""
                Name: {fullname}
                Email: {email}
                Phone: {phone_number}
                Message: {msg}
                """,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['chintu81400@gmail.com'],  # Admin email
                fail_silently=False,
            )
            send_mail(
            subject=f"New Request Call: {subject}",
            message=f"""
            New Request Call Details

            Full Name : {fullname}
            Email     : {email}
            Phone     : {phone_number}
            Subject   : {subject}

            Message:
            {msg}
            """,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['yourgmail@gmail.com'],
                fail_silently=False,
            )

            messages.success(request, 'Your application has been submitted successfully.')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    return render(request, 'Fontend_Playa/index.html')

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