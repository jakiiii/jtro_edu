from django.shortcuts import render
from django.views.generic import TemplateView


class CourseListView(TemplateView):
    template_name = 'course/course_list.html'

    def get_context_data(self, **kwargs):
        context = super(CourseListView, self).get_context_data(**kwargs)
        context['title'] = 'Courses'
        return context


class CourseDetailView(TemplateView):
    template_name = 'course/course_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Course Preview'
        return context


class TakeCourseDetailView(TemplateView):
    template_name = 'course/course_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TakeCourseDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Course Preview'
        return context


