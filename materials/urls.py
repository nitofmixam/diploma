from django.urls import path
from rest_framework.routers import DefaultRouter
from materials.apps import MaterialsConfig
from materials.views import CourseViewSet, TopicViewSet, LectureCreateAPIView, LectureUpdateAPIView, \
    LectureDestroyAPIView, LectureListAPIView, LectureRetrieveAPIView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, 'course')
router.register(r'topic', TopicViewSet, 'topic')

urlpatterns = [
                  path('lecture/create/', LectureCreateAPIView.as_view(), name="lecture_create"),
                  path('lecture/update/<int:pk>/', LectureUpdateAPIView.as_view(), name="lecture_update"),
                  path('lecture/destroy/<int:pk>/', LectureDestroyAPIView.as_view(), name="lecture_destroy"),
                  path('lectures_list/', LectureListAPIView.as_view(), name="lectures_list"),
                  path('lecture/retrieve/<int:pk>/', LectureRetrieveAPIView.as_view(), name="lecture_retrieve"),
              ] + router.urls
