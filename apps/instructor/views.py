from django.shortcuts import render
from django.views.generic import TemplateView


class TeacherProfileView(TemplateView):
    template_name = 'instructor/teacher_profile.html'

    def get_context_data(self, **kwargs):
        context = super(TeacherProfileView, self).get_context_data(**kwargs)
        context['title'] = 'Profile'
        return context
