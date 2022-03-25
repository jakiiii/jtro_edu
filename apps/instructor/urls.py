from django.urls import path
from apps.instructor.views import TeacherProfileView

app_name = 'instructor'


urlpatterns = [
    path('profile/', TeacherProfileView.as_view(), name='teacher-profile')
]
