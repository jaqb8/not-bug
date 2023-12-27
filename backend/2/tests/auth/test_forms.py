import pytest
from auth.forms import CreateUserForm

pytestmark = pytest.mark.django_db


class TestUserForm:
    def test_form_has_fields(self):
        form = CreateUserForm()
        expected = ["username", "email", "password1", "password2"]
        actual = list(form.fields)
        assert expected == actual

    def test_create_user_form(self):
        form = CreateUserForm(
            data={
                "username": "testuser",
                "email": "test@test.com",
                "password1": "testpassword",
                "password2": "testpassword",
            }
        )
        assert form.is_valid()

    def test_create_user_form_no_data(self):
        form = CreateUserForm(data={})
        assert not form.is_valid()
        assert len(form.errors) == 4

    def test_create_user_form_invalid_data(self):
        form = CreateUserForm(
            data={
                "username": "testuser",
                "email": "test",
                "password1": "testpassword",
                "password2": "testpassword",
            }
        )
        assert not form.is_valid()
        assert len(form.errors) == 1
        assert "email" in form.errors

    def test_create_user_form_passwords_dont_match(self):
        form = CreateUserForm(
            data={
                "username": "testuser",
                "email": "test@test.com",
                "password1": "testpassword",
                "password2": "testpassword1",
            }
        )
        assert not form.is_valid()
        assert len(form.errors) == 1
        assert "password2" in form.errors
