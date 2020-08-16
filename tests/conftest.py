from pytest import fixture
from config import Config


def pytest_addoption(parser):
  parser.addoption(
    '--env',
    action='store',
    help='Environment to execute tests'
  )

@fixture(scope='session')
def env(request):
  """
  request is part of pytest and holds all information entered on the
  command line.

  return the --env variable from the command line.
  """
  return request.config.getoption('--env')

@fixture(scope='session')
def app_config(env):
  config = Config(env)
  return config
