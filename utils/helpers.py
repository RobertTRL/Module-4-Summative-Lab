class ClassProperty:
    """Descriptor that works on the class itself, not instances."""

    def __init__(self, fget=None, fset=None):
        self.fget = fget
        self.fset = fset

    def __get__(self, obj, owner):
        return self.fget(owner)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("This class property is read-only.")
        self.fset(type(obj), value)

    def setter(self, fset):
        return ClassProperty(self.fget, fset)

