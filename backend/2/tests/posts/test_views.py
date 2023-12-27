from unittest.mock import patch
from django.test import Client
import pytest


pytestmark = pytest.mark.django_db


class TestPostViews:
    client = Client()

    def test_post_list_view(self, post_factory, user_factory):
        post_factory.create_batch(10)
        user = user_factory()
        self.client.force_login(user)

        response = self.client.get("/")

        assert response.status_code == 200
        assert "posts" in response.context
        assert len(response.context["posts"]) == 10
        assert "create_post_form" in response.context

    def test_post_list_view_unauthenticated(self, post_factory):
        post_factory.create_batch(10)

        response = self.client.get("/")

        assert response.status_code == 200
        assert "posts" in response.context
        assert len(response.context["posts"]) == 10
        assert "create_post_form" not in response.context

    def test_create_post_view(self, user_factory):
        user = user_factory()
        self.client.force_login(user)

        with patch("posts.views.CreatePostForm") as mock_create_post_form:
            mock_create_post_form.is_valid.return_value = True
            response = self.client.post(
                "/create",
            )

        assert response.status_code == 302
        assert response.url == "/"

    def test_create_post_view_invalid_form(self, user_factory):
        user = user_factory()
        self.client.force_login(user)

        with patch("posts.views.CreatePostForm.is_valid") as mock_create_post_form:
            mock_create_post_form.return_value = False
            response = self.client.post(
                "/create",
            )

        assert response.status_code == 400
        assert "create_post_form" in response.context

    def test_create_post_view_unauthenticated(self):
        response = self.client.post(
            "/create",
        )

        assert response.status_code == 302
        assert response.url == "/login?next=/create"

    def test_post_detail_view(self, post_factory, user_factory):
        user = user_factory()
        post_factory(title="test post", author=user)
        self.client.force_login(user)

        response = self.client.get("/post/1")

        assert response.status_code == 200
        assert "post" in response.context
        assert response.context["post"].title == "test post"
        assert response.context["can_edit"] is True

    def test_post_detail_view_unauthenticated(self, post_factory):
        post_factory(title="test post")
        response = self.client.get("/post/1")

        assert response.status_code == 200
        assert "post" in response.context
        assert response.context["post"].title == "test post"
        assert response.context["can_edit"] is False

    def test_post_detail_view_not_author(self, post_factory, user_factory):
        user = user_factory()
        post_factory(title="test post")
        self.client.force_login(user)

        response = self.client.get("/post/1")

        assert response.status_code == 200
        assert "post" in response.context
        assert response.context["post"].title == "test post"
        assert response.context["can_edit"] is False

    def test_post_edit_view(self, post_factory, user_factory):
        user = user_factory()
        post_factory(title="test post", author=user)
        self.client.force_login(user)

        with patch("posts.views.CreatePostForm") as mock_create_post_form:
            mock_create_post_form.is_valid.return_value = True
            response = self.client.post(
                "/post/1/edit",
            )

        assert response.status_code == 302
        assert response.url == "/post/1"

    def test_post_edit_view_invalid_form(self, post_factory, user_factory):
        user = user_factory()
        post_factory(title="test post", author=user)
        self.client.force_login(user)

        with patch("posts.views.CreatePostForm.is_valid") as mock_create_post_form:
            mock_create_post_form.return_value = False
            response = self.client.post(
                "/post/1/edit",
            )

        assert response.status_code == 400
        assert "edit_post_form" in response.context

    def test_post_edit_view_unauthenticated(self, post_factory):
        post_factory(title="test post")
        response = self.client.post(
            "/post/1/edit",
        )

        assert response.status_code == 302
        assert response.url == "/login?next=/post/1/edit"

    def test_post_edit_view_not_author(self, post_factory, user_factory):
        user = user_factory()
        post_factory(title="test post")
        self.client.force_login(user)

        response = self.client.post(
            "/post/1/edit",
        )

        assert response.status_code == 302
        assert response.url == "/post/1"

    def test_post_edit_view_get(self, post_factory, user_factory):
        user = user_factory()
        post = post_factory(title="test post", author=user)
        self.client.force_login(user)

        response = self.client.get("/post/1/edit")

        assert response.status_code == 200
        assert "edit_post_form" in response.context
        assert "test post" == response.context["post"].title
