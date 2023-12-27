import pytest
from posts.forms import CreatePostForm

pytestmark = pytest.mark.django_db


class TestCreatePostForm:
    def test_form_has_fields(self):
        form = CreatePostForm()
        expected = ["title", "content"]
        actual = list(form.fields)
        assert expected == actual

    def test_post_form(self):
        form = CreatePostForm(
            data={
                "title": "test title",
                "content": "test content",
            }
        )
        assert form.is_valid()

    def test_post_form_no_data(self):
        form = CreatePostForm(data={})
        assert not form.is_valid()
        assert len(form.errors) == 2
