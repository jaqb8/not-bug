from pytest_factoryboy import register
from tests.factories import PostFactory, UserFactory

register(UserFactory)
register(PostFactory)
