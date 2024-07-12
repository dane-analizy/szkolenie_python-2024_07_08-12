import yaml


def get_config(nazwa_pliku):
    config = {}
    with open(nazwa_pliku, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return config
