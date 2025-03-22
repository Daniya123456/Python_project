# Installation
To install the ER CCAPI Python Package, you can use pip3 or pip:

``` py
pip3 install git+ssh://git@gitlab.cicd.energy-robotics.com:8086/er_dev/er-ccapi-python.git
```
## Usage

If you want to use the er-ccapi-python package, you need to provide the following information, which is stored in a yaml file in the directory in which you run your script:

```yaml title="config.yml"
auth_service:
  endpoint: "https://login.energy-robotics.com/api/loginApi"
  user_email: "<add your email here>"
  user_api_key_file: "<add the name of your key file here>"
  refresh_interval: 300

api:
  production_deployment: False
  dev_url: "https://ccapi-development.devtest.energy-robotics.com/graphql"
  prod_url: "https://api.graphql.energy-robotics.com/graphql"

```
Save this file and use the filename to initialize a client. For example if your config file is named `config.yml`.
```python title="simple_test.py"
import yaml
from er_ccapi_python.client import GraphqlClient
# load the config.yml
config = yaml.safe_load(open("test_config.yml"))

er_client = GraphqlClient(config)

```

For security reasons, your API key should be placed in a separate file containing only your key in the same folder. Add the filename to your `config.yml` as shown above. The name of the file could be `key-file`.
