from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from products import views


urlpatterns = [
    url(r'^category/$', views.CategoryList.as_view()),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view()),
    url(r'^product/$', views.ProductList.as_view()),
    url(r'^product/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)