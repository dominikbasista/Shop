from django.test import TestCase
from accounts.forms import SignUpForm

class SignUpFormTest(TestCase):

    def test_sign_up_form_rednders_email_input(self):
        form = SignUpForm()
        self.fail(form.as_p)

