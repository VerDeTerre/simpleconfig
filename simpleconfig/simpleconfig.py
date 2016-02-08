# Copyright (c) 2016 John Tye Bennett
# See LICENSE for details

import os
from json import loads


class ConfigLoader(object):

    def __init__(self, app_root):
        self.app_root = app_root
        self.config_root = os.path.join(app_root, 'config')
        self.environments = os.environ.get(
            'APP_ENV',
            'development'
        ).split(',')

    def config_path(self, name, environment):
        filename = '.'.join([name, environment, 'json'])
        return os.path.join(self.config_root, filename)

    def load_config(self, name):
        config = {}
        success = False
        for environment in self.environments:
            try:
                with open(self.config_path(name, environment)) as file:
                    config.update(loads(file.read()))
                success = True
            except:
                pass
        if not success:
            raise Exception('Could not find config file for "{}"'.format(name))
        return config
