# We use PIP (Pip Installs Packages), the official Python package manager.
# It's used to install and manage libraries and packages that aren't included in the standard library.

# Console $ pip install requests

import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())