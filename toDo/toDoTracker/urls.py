from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    #url(r'^$', views.IndexView.as_view()),
    url(r'^$', views.index, name='index'),
    url(r'^.*Edit-Task.html', views.EditTaskView.as_view()),
    #url(r'^.*New-Task.html', views.NewTaskView.as_view()),
    url(r'^Impressum.html', views.ImpressumView.as_view()),
    url(r'^New-Task.html',
        'toDoTracker.views.newTask', name='newTask'),
    )

#urlpatterns = [
#    url(r'^$', views.index, name='index'),
#]
