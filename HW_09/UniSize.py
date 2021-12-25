def sizer(cls):
    class SizedClass(cls):
        def __init__(self, *args, **kwargs):
            self.obj = cls(*args, **kwargs)
            print('__len__' in dir(self.obj))
            
            if hasattr(self.obj, '__len__'):
                self.size = len(self.obj)
            elif hasattr(self.obj, '__abs__'):
                self.size = abs(self.obj)
            else:
                self.size = 0
                
        def __str__(self):
            return f'{self.obj}'
            
    return SizedClass

@sizer
class R(dict):
    pass


@sizer
class S(str):
    pass
    
@sizer
class N(complex):
    pass
    
@sizer
class E(Exception):
    pass
    
for obj in S("QWER"), N(3+4j), E("Exceptions know no lengths!"):
    print(obj, obj.size)

'''
Различие в строке 1: вывод:
>{} 0<
эталон:
>{2: 102, 3: 104, 4: 106, 5: 108, 6: 110, 7: 112, 8: 114, 9: 116, 10: 118, 11: 120} 10<
'''