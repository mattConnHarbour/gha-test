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

examples_root = './superdoc/examples'
example_dir_names = os.listdir(examples_root)
example_dir_names.sort()

demo_configs = []

for dir_name in example_dir_names:
    # get config json
    config_path = f'{examples_root}/{dir_name}/demo-config.json'
    config_dict = read_json_file(config_path)
    if not config_dict:
        continue

    # set directory name
    config_dict["dirname"] = dir_name

    demo_configs.append(config_dict)

with open('./public/demos/demos-config.json', 'w', encoding='utf-8') as f:
    json.dump(demo_configs, f, ensure_ascii=False, indent=4)