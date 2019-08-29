class SingletonInstance:
    __instance = None

    @classmethod
    def get_instance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.get_instance
        return cls.__instance

