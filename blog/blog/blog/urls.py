from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.decorators import login_required
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'myblog.views.showBlog', name='showBlog'),
    url(r'^login/$', 'myblog.views.login', name = 'login1'),
    url(r'^logout/$', 'myblog.views.logout', name = 'logout'),
    url(r'^signup/$', 'myblog.views.signup', name = 'signup'),
    url(r'^accounts/login/$','django.contrib.auth.views.login',name='login'),                   
    url(r'^admin/', include(admin.site.urls)),
    #(r'^tinymce/',include('tinymce.urls')),
                       
)
urlpatterns += staticfiles_urlpatterns()