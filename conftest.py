import pytest
from fixture.application import Application

#@pytest.fixture(scope = "session")
@pytest.fixture
def app(request):
  fixture = Application()
  fixture.session.login(username="test0001push@gmail.com", password="plokijuh1")
  request.addfinalizer(fixture.destroy)
  return fixture