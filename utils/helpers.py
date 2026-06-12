class ClassProperty:
    """Descriptor that works on the class itself, not instances."""

    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, obj, owner):
        return self.fget(owner)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("This class property is read-only.")
        self.fset(type(obj), value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("This class property cannot be deleted.")
        self.fdel(type(obj))

    def setter(self, fset):
        return ClassProperty(self.fget, fset, self.fdel)

    def deleter(self, fdel):
        return ClassProperty(self.fget, self.fset, fdel)