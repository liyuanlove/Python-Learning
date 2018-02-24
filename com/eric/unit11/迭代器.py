from collections import Iterable
t = [1, 2, 3, 4, 5]
print(isinstance(t, Iterable))
t_iter = t.iter()
print(next(t_iter))
