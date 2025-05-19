import yaml

config_path = "E:/VSProjekte/SkyDefenseRL/config/config.yaml"

class ConfigLoader():
    def __init__(self):
        self.config = {}
        with open(config_path) as f:
            self.config = yaml.load(f, Loader=yaml.FullLoader)

            
