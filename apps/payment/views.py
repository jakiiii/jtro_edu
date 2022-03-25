from django.shortcuts import render
from django.views.generic import TemplateView


class PricingView(TemplateView):
    template_name = 'payment/pricing.html'

    def get_context_data(self, **kwargs):
        context = super(PricingView, self).get_context_data(**kwargs)
        context['title'] = 'Pricing'
        return context
