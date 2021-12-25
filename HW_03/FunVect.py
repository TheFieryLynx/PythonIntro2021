def superposition(funmod, funseq):
    funres = []
    for i in funseq:
        def func(x, j = i):
            return funmod(j(x))
        funres.append(func)
    print(funres)
    return funres

from math import *
F = superposition(abs, (sin, cos))