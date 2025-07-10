from pathlib import Path

import pet_store_api_autotests


def abs_path_from_project(file_name):
    return str(Path(pet_store_api_autotests.__file__).parent.parent.joinpath(file_name))
