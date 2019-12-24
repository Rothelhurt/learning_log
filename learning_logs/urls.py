"""Определяет схемы URL для learning_logs."""

from django.conf.urls import url
from . import views

urlpatterns = [
    # Домашняя страница.
    url(r'^$', views.index, name='index'),
    # Просмотр тем.
    url(r'^topics/$', views.topics, name='topics'),
    # Просмотр отдельной темы.
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # Страница создания новой темы.
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # Страница добавления новой записи.
    url(r'^new_enrty/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # Страница для редактирования записи.
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
    # Страница для удаления записи.
    url(r'^delete_entry/(?P<entry_id>\d+)/$', views.delete_entry, name='delete_entry'),
]
