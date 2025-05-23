import base64
import json
import os

def read_json_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print("Could not read JSON file. Exception:", e)
        return None

def validate_path(path):
    return os.path.isfile(path)

examples_root = './superdoc/examples'
example_dir_names = os.listdir(examples_root)
example_dir_names.sort()

demo_configs = []

for dir_name in example_dir_names:
    # get config json
    config_path = f'{examples_root}/{dir_name}/demo-config.json'
    is_valid_path = validate_path(config_path)
    if not is_valid_path:
        continue
    config_dict = read_json_file(config_path)

    # set directory name
    config_dict["dirname"] = dir_name

    demo_configs.append(config_dict)

demo_config_strings = [json.dumps(config, indent=4)+",\n" for config in demo_configs]

file_lines = [
    "const demosConfigGlobal = [\n",
    *demo_config_strings,
    "]"
]

with open('./public/demos/demos-config.js', 'w', encoding='utf-8') as f:
    f.writelines(file_lines)