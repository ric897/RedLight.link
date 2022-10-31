
from django.shortcuts import redirect, render
from twilio.rest import Client

from AIupload.forms import Registration
from .models import NewUser

from django.views.generic.list import ListView

from django.views.generic.edit import FormView

from django.urls import reverse_lazy


from django.contrib.auth.decorators import login_required




from django.contrib.auth import login



from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from django.contrib.auth.views import LoginView


from django.http import HttpResponse, HttpResponseRedirect





# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'AIupload/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard')

class RegisterPage(FormView):
    redirect_authenticated_user = True
    template_name = 'AIupload/register.html'
    form_class = Registration
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        
        return super(RegisterPage, self).form_valid(form)


def dashboard(request):
    context = {}
    
    if request.user.is_authenticated:
        context['help_phone'] = request.user.help_phone

        if request.method == 'POST':
             
            
            
            account_sid = '' 
            auth_token = '' 
            client = Client(account_sid, auth_token) 
 
            ##Send to school or dak as well
            message = client.messages.create(messaging_service_sid='', body='EMERGENCY ' + str(request.user.first_name) + ' HAS REQUESTED HELP FOR A MENTAL HEALTH CRISIS AT BU CALL THEM AT +1' + str(request.user.phone) + ' OR REACH OUT TO EMERGENCY SERVICES ASAP', to='+16308081663')

            return redirect('call')
 
            


    return render(request, 'dashboard.html', context)

def call(request):
    #Things to help in this moment
    return render(request, 'call.html', {})



        




































