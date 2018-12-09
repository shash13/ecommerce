from django.conf.urls import include, url
from django.contrib import admin
from shop import views as shop_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'ecommerce.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', shop_views.index, name='index'),
    url(r'^homepage/', shop_views.homepage, name='homepage'),
    url(r'^list/', shop_views.product_list_view, name='list'),
    url(r'^listclass/', shop_views.ProductListView.as_view(), name='list2'),
    url(r'^listdetail/(?P<pk>\d+)/$', shop_views.product_detail_view, name='list'),
   # url(r'^listdetailclass/(?P<pk>\d+)/$', shop_views.ProductDetailView.as_view(), name='list2'),
    url(r'^contact/', shop_views.contact, name='contact'),
 ]
