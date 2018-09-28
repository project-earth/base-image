import os
import yaml


def get_configuration(config_path=None):
    """ Parses a YAML formatted configuration file and adds the standard service wide information.

    Args:
        config_path <str>: A path to the config file to parse. Defaults to the following path:
            <base_path>/<service_name>/resources/config.yml
    """
    if config_path is None:
        config_path = os.path.join(os.environ['BASE_PATH'], os.environ['SERVICE_NAME'], 'resources', 'config.yml')

    with open(config_path, 'r') as file:
        configuration = yaml.load(file)
    configuration['service_name'] = os.environ['SERVICE_NAME']
    configuration['base_path'] = os.environ['BASE_PATH']

    return configuration


CONFIG = get_configuration()
