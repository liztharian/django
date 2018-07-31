
from django.conf.urls import url,include
from home.views import HomeView

urlpatterns=[


    url(r'^$',HomeView.as_view(),name='home'),
]
