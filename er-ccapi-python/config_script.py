import yaml
from er_ccapi_python.client import GraphqlClient

# Load the configuration from the config.yml file
config = yaml.safe_load(open("config.yml"))

# Initialize the ER CCAPI client
er_client = GraphqlClient(config)
