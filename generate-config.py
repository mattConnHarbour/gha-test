import requests
import base64
import json
import os

def get_file_base64(url, headers):
    response = requests.get(url, headers=headers)
    file_json = response.json()
    if file_json.get("status") == "404":
        return None

    file_base64 = file_json.get("content")
    return file_base64

secret_key = "GH_PAT"
api_key = os.environ.get(secret_key)

if not api_key:
    raise Exception("No GitHub API token found.")

# root_url = "http://api.github.com/repos/Harbour-Enterprises/SuperDoc/contents/examples/"
root_url = "http://api.github.com/repos/mattConnHarbour/superdoc-examples-config/contents/"
headers={
    "Authorization": f"Bearer {api_key}"
}

response = requests.get(root_url, headers=headers)
response_json = response.json()

example_dirs = [file for file in response_json if file.get("type") == "dir"]
example_dir_names = [dir.get("name") for dir in example_dirs]

demo_configs = []

for dir_name in example_dir_names:
    # get config json
    config_url = f"{root_url}{dir_name}/demo-config.json"
    config_base64 = get_file_base64(config_url, headers)
    if not config_base64:
        continue

    config_decoded = base64.b64decode(config_base64).decode('utf-8')
    config_dict = json.loads(config_decoded)

    # set directory name
    config_dict["dirname"] = dir_name

    demo_configs.append(config_dict)

with open('demos-config.json', 'w', encoding='utf-8') as f:
    json.dump(demo_configs, f, ensure_ascii=False, indent=4)