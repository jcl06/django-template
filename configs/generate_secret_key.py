import importlib
import os
import re
import traceback
from django.core.exceptions import ImproperlyConfigured

def generate_secret_key():
    output = "SECRET_KEY Generation Failed."
    try:
        config_path = os.getenv('configuration', 'configs.configuration')
        try:
            configuration = importlib.import_module(config_path)
        except ModuleNotFoundError as e:
            if getattr(e, 'name') == config_path:
                raise ImproperlyConfigured(
                    f"Specified configuration module ({config_path}) not found. Please define project_name/configs/configuration.py"
                )
            raise Exception(str(e))
        # print("Config path:", config_path)
        config_file = os.path.abspath(configuration.__file__)
        ENCRYPTED_KEY = configuration.generate_secret_key()
        file_data = open(config_file, 'r')
        data = file_data.readlines()
        file_data.close()
        matched = 0
        regenerated = False
        for i, line in enumerate(data):
            if re.search(r'^SECRET_KEY_GENERATED.*=.*True\n', line):
                matched += 1
                regenerated = True
            if re.search(r'^SECRET_KEY_GENERATED.*=.*False\n', line):
                data[i] = 'SECRET_KEY_GENERATED = True\n'
                matched += 1
            if re.search(r'^SECRET_KEY.*=.*decrypt\(*.*\)\n', line):
                data[i] = "SECRET_KEY = decrypt('{0}')\n".format(ENCRYPTED_KEY)
                matched += 1
            if matched == 2:
                break
        if matched == 2:
            file_data = open(config_file, 'w')
            file_data.writelines(data)
            file_data.close()
            output = 'SECRET_KEY has successfully generated.'
            if regenerated:
                output = 'SECRET_KEY has successfully changed.'
    except Exception as err:
        print(traceback.print_exc())
        output = str(err)
    finally:
        print(output)
