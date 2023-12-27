import factory
from django.contrib.auth.models import User
from posts.models import Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    email = factory.Faker("text")
    password = factory.Faker("text")


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("text")
    content = factory.Faker("text")
    author = factory.SubFactory(UserFactory)
    date_posted = factory.Faker("date_time")
