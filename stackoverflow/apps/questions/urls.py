from django.urls import path


from .views import (QuestionsView, SingleQuestionView)

urlpatterns = [path('', QuestionsView.as_view(), name="view-questions"),
               path('<int:id>/', SingleQuestionView.as_view(),
                    name="single-question")
               ]
