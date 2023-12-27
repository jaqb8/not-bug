import datetime
import pytest

pytestmark = pytest.mark.django_db


class TestPostModel:
    def test_post_str(self, post_factory):
        post = post_factory(title="test post")
        assert str(post) == "test post"

    def test_post_formatted_date(self, post_factory):
        post = post_factory()
        assert post.formatted_date() == datetime.datetime.now().strftime("%d %B %Y")
