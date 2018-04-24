from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from drdown.medicalrecords.views import view_medical_record
from drdown.users.views import view_user

app_name = 'medicalrecords'
urlpatterns = [
    url(
        regex=r'^(?P<username>[\w.@+-]+)$',
        view=view_medical_record.MedicalRecordsListView.as_view(),
        name='list_medicalrecords'
    ),
    url(
        regex=r'^$',
        view=view_medical_record.MedicalRecordsUserListView.as_view(template_name='medicalrecords/medicalrecord_list_user.html'),
        name='list_medicalrecords_user'
    ),
    url(
        regex=r'^new/$',
        view=view_medical_record.MedicalRecordsCreateView.as_view(),
        name='create_medicalrecords'
    ),

    url(
        regex=r'^(?P<pk>\d+)/delete/$',
        view=view_medical_record.MedicalRecordsDeleteView.as_view(),
        name='delete_medicalrecords'
    ),

    url(
        regex=r'^(?P<pk>\d+)/update/$',
        view=view_medical_record.MedicalRecordsUpdateView.as_view(),
        name='update_medicalrecords'
    ),
]
