import pytest
from ..models import User


@pytest.mark.django_db
class TestUser:

    @pytest.fixture
    def create_user(self):
        return User.objects.create_user(
            username='Markinho',
            password='vv'
        )

    def test_should_create_user(self, create_user):
        user = create_user

        assert isinstance(user, User)
        assert user.username == 'Markinho'