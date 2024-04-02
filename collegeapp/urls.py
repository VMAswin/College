from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.ho,name='ho'),
    path('hlog',views.hlog,name='hlog'),
    path('ad',views.ad,name='ad'),
    path('addcourse',views.addcourse,name='addcourse'),
    path('adco',views.adco,name='adco'),
    path('adst',views.adst,name='adst'),
    path('addstud',views.addstud,name='addstud'),
    path('showstud',views.showstud,name='showstud'),
    path('shte',views.shte,name='shte'),
    path('teacherregist',views.teacherregist,name='teacherregist'),
    path('add_teacher',views.add_teacher,name='add_teacher'),
    path('test',views.test,name='test'),
    path('teacher',views.teacher,name='teacher'),
    path('profile',views.profile,name='profile'),
    path('ed',views.ed,name='ed'),
    path('edi/<int:k>',views.edi,name='edi'),
    path('logout',views.logout,name='logout'),
    path('deletestud/<int:k>',views.deletestud,name='deletestud'),
    path('edits/<int:k>',views.edits,name='edits'),
    path('editstud/<int:k>',views.editstud,name='editstud'),
    path('delete/<int:k>',views.delete,name='delete'),

]