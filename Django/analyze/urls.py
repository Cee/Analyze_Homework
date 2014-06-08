from django.conf.urls import patterns, include, url

import django
import os
import views

static_dir = os.path.join(os.path.dirname(__file__), 'static').replace('\\', '/')
statics = os.listdir(static_dir)

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'analyze.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^product$', views.product_info),
                       url(r'^product_d$', views.product_d),

                       url(r'^index(\.html)*$', views.index_html),
                       url(r'^category', views.category),
                       url(r'^$', views.jump_index),

                       url(r'^category$',views.category),


                       #sources
                       url(r'^(' + '|'.join(statics) + ')/(.+)$', views.source),
)
