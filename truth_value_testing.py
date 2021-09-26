"""Truth value false"""
elist = []
print(bool(elist))

edict = {}
print(type(edict))
print(bool(edict))

edict = {1, 2, 3}
print(type(edict))

'''Custom objects default bool value is true'''


class Check:
    pass


class MakeFalse:
    def __bool__(self):
        return False

    def __len__(self):
        return 0


print(bool(Check))
print(bool(MakeFalse))
