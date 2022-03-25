from django.urls import path
from apps.course.views import (
    CourseListView, CourseDetailView, TakeCourseDetailView, CourseWatchTrailer, TakeCourseLessonDetailView,
    TakeCourseLessonDiscussionView, TakeCourseAskQuestionView, TakeCourseLessonAnswerView
)

app_name = 'course'

urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),
    path('preview/', CourseDetailView.as_view(), name='course-preview'),
    path('preview/trailer/', CourseWatchTrailer.as_view(), name='course-trailer'),
    path('yours/', TakeCourseDetailView.as_view(), name='course-yours'),
    path('yours/lesson/', TakeCourseLessonDetailView.as_view(), name='course-lesson'),
    path('yours/lesson/discussion/', TakeCourseLessonDiscussionView.as_view(), name='course-discussion'),
    path('yours/lesson/question/', TakeCourseAskQuestionView.as_view(), name='course-question'),
    path('yours/lesson/question-answer/', TakeCourseLessonAnswerView.as_view(), name='course-question-answer'),
]
