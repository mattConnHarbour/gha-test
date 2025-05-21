import base64
import json
import os

def read_json_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

example_dir_names = os.listdir('superdoc/examples')

demo_configs = []

for dir_name in example_dir_names:
    # get config json
    config_dict = read_json_file(f'./{dir_name}/demo-config.json')

    # set directory name
    config_dict["dirname"] = dir_name

    demo_configs.append(config_dict)

with open('./public/demos/demos-config.json', 'w', encoding='utf-8') as f:
    json.dump(demo_configs, f, ensure_ascii=False, indent=4)