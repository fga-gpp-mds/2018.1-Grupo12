from test_plus.test import TestCase
from django.test.client import Client
from django.shortcuts import reverse

from drdown.careline.models import Procedure
from drdown.users.models import Patient, Responsible, Employee

from drdown.careline.views import ChecklistDetailView

class TestViewChecklistDetailView(TestCase):
    """
        Test if the List View of Checklist is working correctly
    """

    def setUp(self):
        """
            Runs before every test
        """

        self.user_responsible = self.make_user(username='resp')

        Responsible.objects.create(
            user=self.user_responsible,
            cpf="974.220.200-16"
        )

        self.user_patient1 = self.make_user(username='pat1')

        Patient.objects.create(
            ses="1234567",
            user=self.user_patient1,
            priority=1,
            mother_name="Mae",
            father_name="Pai",
            ethnicity=3,
            sus_number="12345678911",
            civil_registry_of_birth="12345678911",
            declaration_of_live_birth="12345678911",
            responsible=self.user_responsible.responsible
        )

        self.user_patient1.refresh_from_db()

        self.user_patient2 = self.make_user(username='pat2')

        Patient.objects.create(
            ses="1234213",
            user=self.user_patient2,
            priority=1,
            mother_name="Mae",
            father_name="Pai",
            ethnicity=3,
            sus_number="12345633912",
            civil_registry_of_birth="12345123911",
            declaration_of_live_birth="1212338911",
            responsible=self.user_responsible.responsible
        )

        self.client = Client()
        self.view = ChecklistDetailView()

    def test_has_permission_for_responsible(self):
        """
            Test if a responsible have access to its patients
        """

        self.assertEquals(
            self.view.has_permission(current_user=self.user_responsible, target_user=self.user_patient1),
            True
        )

        self.assertEquals(
            self.view.has_permission(current_user=self.user_responsible, target_user=self.user_patient2),
            True
        )

    def test_has_permission_for_not_responsible(self):
        """
            Test if a user that is not a responsible for a patient cannot access a patient data
        """

        user = self.make_user(username='hacker')

        self.assertEquals(
            self.view.has_permission(current_user=user, target_user=self.user_patient1),
            False
        )

        self.assertEquals(
            self.view.has_permission(current_user=user, target_user=self.user_patient2),
            False
        )

        Responsible.objects.create(cpf="427.465.580-68", user=user)
        user.refresh_from_db()

        self.assertEquals(
            self.view.has_permission(current_user=user, target_user=self.user_patient1),
            False
        )

        self.assertEquals(
            self.view.has_permission(current_user=user, target_user=self.user_patient2),
            False
        )

    def test_get_page_when_responsible(self):
        """
            Test if the page loads when a responsible is the current user and is trying to see his patient
        """

        self.client.force_login(self.user_responsible)

        response = self.client.get(
            path=reverse(
                viewname='careline:checklist_detail',
                kwargs={'username': self.user_patient1.username}
            ),
            follow=True
        )

        self.assertEquals(response.status_code, 200)

    def test_get_page_when_patient(self):
        """
            Test if the page loads when a patient is the current user
        """

        self.client.force_login(self.user_patient1)

        response = self.client.get(
            path=reverse(
                viewname='careline:checklist_detail',
                kwargs={'username': self.user_patient1.username}
            ),
            follow=True
        )

        self.assertEquals(response.status_code, 200)

    def test_get_page_when_different_patient(self):
        """
            Test if the page wont load when a patient is trying to access other patient
        """

        self.client.force_login(self.user_patient2)

        response = self.client.get(
            path=reverse(
                viewname='careline:checklist_detail',
                kwargs={'username': self.user_patient1.username}
            ),
            follow=True
        )

        self.assertEquals(response.status_code, 200)
