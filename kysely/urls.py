from django.urls import path
from . import views
from django.conf import  settings
from django.conf.urls.static import static

app_name = 'Kysely'

urlpatterns = [
#127.0.0.1/kysely/
path('', views.index, name="index"),
#esim. 127.0.0.1/kysely/1
path('<int:question_id>/', views.detail, name="detail"),
#esim. 127.0.0.1/kysely/1/results
path('<int:question_id>/results/', views.results, name="results"),
#esim. 127.0.0.1/kysely/1/vote
path('<int:question_id>/vote/', views.vote, name="vote"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

