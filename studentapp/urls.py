from django.urls import path,include
from.import views

urlpatterns = [
    path('',views.show_student,name='show_student'),
    path('add_student',views.add_student,name='add_student'),
    path('show_student_details',views.show_student_details,name='show_student_details'),
    path('editpage/<int:pk>',views.editpage,name='editpage'),
    path('edit_student_details/<int:pk>',views.edit_student_details,name='edit_student_details'),
    path('deletepage/<int:pk>',views.deletepage,name='deletepage'),
    path('details/<int:pk>',views.details,name='details'),
    path('details',views.details,name='details'),






]