from django.urls import path
from apps.posts.views import IndexView, AboutView, CousersView, FrontView, BakcView, Ux_uiView, AndroidView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path('about/', AboutView.as_view(), name='about'),
    path('cousers/', CousersView.as_view(), name='cousers'),
    path('front/', FrontView.as_view(), name='front'),
    path('back/', BakcView.as_view(), name='back'),
    path('ux_ui/', Ux_uiView.as_view(), name='ux_ui'),
    path('android/', AndroidView.as_view(), name='android'),

]
