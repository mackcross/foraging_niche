class Species:
    _registry = []

    def __init__(self, name):
        self.name = name
        Species._registry.append(self)

    @classmethod
    def all_instances(cls):
        return cls._registry
    
    
