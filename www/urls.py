from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^([0-9]+)/$', views.detail, name = 'detail'),
    url(r'^elim-directorio/post_url/$', views.post_person, name = 'post_person'),
    url(r'^predicas/$', views.predicas_elim, name = 'predicas'),
    url(r'^quienes-somos/$', views.quienes_somos, name = 'quienes_somos'),
    url(r'^elim-tv/$', views.elim_tv, name = 'elim_tv'),
    url(r'^elim-radio/$', views.elim_radio, name = 'elim_radio'),
    url(r'^elim-directorio/$', views.elim_directorio, name = 'elim_directorio'),
]

