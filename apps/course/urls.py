from django.urls import path
from apps.course.views import CourseListView, CourseDetailView, TakeCourseDetailView

app_name = 'course'

urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),
    path('preview/', CourseDetailView.as_view(), name='course-preview'),
    path('yours/', TakeCourseDetailView.as_view(), name='course-yours'),
]
