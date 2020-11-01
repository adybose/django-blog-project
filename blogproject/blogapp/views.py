from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Article
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
class ArticleListView(ListView):
    queryset = Article.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'

class AboutView(TemplateView):
    template_name = 'about.html'

def contact_us(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender_email, ['enquiry@exampleco.com'])

            return HttpResponse('Thank you for contacting us')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
