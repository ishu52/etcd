from dependency_injector import providers, containers
from Config.Configuration import Configuration

class Configs(containers.DeclarativeContainer):
    config = providers.Configuration('config')

class SetConfiguration(containers.DeclarativeContainer):
    configuration = providers.Singleton(Configuration, Configs.config)
 