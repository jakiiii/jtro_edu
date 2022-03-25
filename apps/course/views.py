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


class CourseWatchTrailer(TemplateView):
    template_name = 'course/watch_trailer.html'

    def get_context_data(self, **kwargs):
        context = super(CourseWatchTrailer, self).get_context_data(**kwargs)
        context['title'] = 'Watch Trailer'
        return context


class TakeCourseDetailView(TemplateView):
    template_name = 'course/take_course_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TakeCourseDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Course'
        return context


class TakeCourseLessonDetailView(TemplateView):
    template_name = 'course/take_course_lesson.html'

    def get_context_data(self, **kwargs):
        context = super(TakeCourseLessonDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Course Lesson'
        return context


class TakeCourseLessonDiscussionView(TemplateView):
    template_name = 'course/discussions.html'

    def get_context_data(self, **kwargs):
        context = super(TakeCourseLessonDiscussionView, self).get_context_data(**kwargs)
        context['title'] = 'Discussion'
        return context


class TakeCourseAskQuestionView(TemplateView):
    template_name = 'course/ask_question.html'

    def get_context_data(self, **kwargs):
        context = super(TakeCourseAskQuestionView, self).get_context_data(**kwargs)
        context['title'] = 'Ask Question'
        return context


class TakeCourseLessonAnswerView(TemplateView):
    template_name = 'course/answer_question.html'

    def get_context_data(self, **kwargs):
        context = super(TakeCourseLessonAnswerView, self).get_context_data(**kwargs)
        context['title'] = 'Answer Question'
        return context
