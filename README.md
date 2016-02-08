# simpleconfig #

## About ##

simpleconfig is a tool to facilitate loading configuration files when using multiple environments (like development, production, test, etc.).

## Usage ##

Your configuration files may be placed in a "config" directory at the root of your project. Files should be named using the following format:

    <name>.<environment>.json

For example, you might place development database credentials in `config/database.development.json`.

When you run you app, specify the environment using the `APP_ENV` environment variable. Multiple environments may be specified, separated by commas. In the case of multiple environments, the configuration will be built in the order specified, i.e., environments to the right will override configurations from environments listed earlier. This feature can be used to create a default configuration, with specific environments defining a more limited set of configurations.

To load configurations, instantiate a `ConfigLoader` with the path to the root of your app. If you are running a script from the root, the following would work:

    import os

    from simpleconfig import ConfigLoader

    config_loader = ConfigLoader('.')
    db_config = config_loader.load_config('database')

## License ##

This software is released under the MIT license. See [LICENSE](LICENSE) for terms.
