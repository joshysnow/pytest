class Config:
  def __init__(self, env):
    SUPPORTED_ENVS = ['dev', 'qa']

    if not isinstance(env, str) or (env.lower() not in SUPPORTED_ENVS):
      raise Exception(f'{env} is not a supported environment (supported envs: {SUPPORTED_ENVS})')

    self.base_url = {
      'dev': 'https://mydev-env.com',
      'qa': 'https://myqa_env.com'
    }[env]

    self.app_port = {
      'dev': 8080,
      'qa': 80
    }[env]
