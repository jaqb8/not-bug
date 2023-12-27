from unittest.mock import patch
from django.test import Client
import pytest


pytestmark = pytest.mark.django_db


class TestAuthViews:
    client = Client()

    def test_register_view_get(self):
        response = self.client.get("/register")

        assert response.status_code == 200
        assert "registerform" in response.context

    @patch("auth.views.CreateUserForm.save")
    @patch("auth.views.CreateUserForm.is_valid")
    def test_register_view(self, mock_is_valid, mock_save, user_factory):
        mock_is_valid.return_value = True
        mock_save.return_value = user_factory()
        response = self.client.post(
            "/register",
        )

        assert response.status_code == 302
        assert response.url == "/"

    @patch("auth.views.CreateUserForm.is_valid")
    def test_register_view_invalid_form(self, mock_is_valid):
        mock_is_valid.return_value = False
        response = self.client.post(
            "/register",
        )

        assert response.status_code == 400
        assert "registerform" in response.context

    def test_login_view_get(self):
        response = self.client.get("/login")

        assert response.status_code == 200
        assert "loginform" in response.context

    @patch("auth.views.LoginForm.is_valid")
    @patch("auth.views.authenticate")
    def test_login_view(self, mock_authenticate, mock_is_valid, user_factory):
        user = user_factory()
        mock_is_valid.return_value = True
        mock_authenticate.return_value = user

        response = self.client.post(
            "/login",
        )

        assert response.status_code == 302
        assert response.url == "/"

    @patch("auth.views.LoginForm.is_valid")
    @patch("auth.views.authenticate")
    def test_login_view(self, mock_authenticate, mock_is_valid):
        mock_is_valid.return_value = True
        mock_authenticate.return_value = None

        response = self.client.post(
            "/login",
        )

        assert response.status_code == 400
        assert "loginform" in response.context

    @patch("auth.views.LoginForm.is_valid")
    def test_login_view_invalid_form(self, mock_is_valid):
        mock_is_valid.return_value = False
        response = self.client.post(
            "/login",
        )

        assert response.status_code == 400
        assert "loginform" in response.context

    def test_logout_view(self, user_factory):
        user = user_factory()
        self.client.force_login(user)
        response = self.client.get("/logout")

        assert response.status_code == 302
        assert response.url == "/"

    def test_logout_view_unauthenticated(self):
        response = self.client.get("/logout")

        assert response.status_code == 302
        assert response.url == "/login?next=/logout"

    def test_profile_view(self, user_factory, post_factory):
        user = user_factory()
        post_factory(author=user)
        self.client.force_login(user)

        response = self.client.get("/profile")

        assert response.status_code == 200
        assert "posts" in response.context
        assert len(response.context["posts"]) == 1

    def test_profile_view_unauthenticated(self):
        response = self.client.get("/profile")

        assert response.status_code == 302
        assert response.url == "/login?next=/profile"
