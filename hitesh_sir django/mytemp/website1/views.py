from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name= 'Home.html'

class AboutPage(TemplateView):
    template_name='about.html'
    
class ConatactPage(TemplateView):
    template_name='conatct.html'    
    