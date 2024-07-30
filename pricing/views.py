from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from pricing_system.forms import OfferForm
from xhtml2pdf import pisa
import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.utils.datastructures import MultiValueDictKeyError

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('create_offer')
            else:
                return render(request, 'pricing/login.html', {'error': 'اسم المستخدم أو كلمة المرور غير صحيحة'})
        else:
            return render(request, 'pricing/login.html', {'error': 'يرجى إدخال اسم المستخدم وكلمة المرور'})
    else:
        return render(request, 'pricing/login.html')


# وظيفة تسجيل الدخول
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('create_offer')
        else:
            return render(request, 'pricing/login.html', {'error': 'اسم المستخدم أو كلمة المرور غير صحيحة'})
    else:
        return render(request, 'pricing/login.html')

# وظيفة الصفحة الرئيسية
@login_required
def home(request):
    return render(request, 'pricing/home.html')

# وظيفة إنشاء العرض المالي
@login_required
def create_offer(request):
    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            context = {
                'association_name': form.cleaned_data['association_name'],
                'customer_address': form.cleaned_data['customer_address'],
                'service_name': form.cleaned_data['service_name'],
                'service_price': form.cleaned_data['service_price'],
                'quantity': form.cleaned_data['quantity'],
                'total_price': form.cleaned_data['total_price'],
                'date': datetime.date.today(),
            }
            pdf = render_to_pdf('pricing/offer_pdf.html', context)
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = f"Offer_{datetime.date.today().strftime('%Y%m%d')}_{request.user.username}.pdf"
                content = f"inline; filename='{filename}'"
                response['Content-Disposition'] = content
                return response
            else:
                return HttpResponse("خطأ في توليد ملف PDF")
    else:
        form = OfferForm()
    return render(request, 'pricing/create_offer.html', {'form': form})

# وظيفة توليد PDF
def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = HttpResponse(content_type='application/pdf')
    pisa_status = pisa.CreatePDF(html, dest=result)
    if pisa_status.err:
        return HttpResponse('حدث خطأ أثناء توليد ملف PDF <pre>' + html + '</pre>')
    return result
