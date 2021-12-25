class Lock:
    is_locked = False
    lock_name = None
    acquired_locks = set()

    def locked(self):
        class Locked(self):
            def __init__(self, *args, **kwargs):
                self._lock_instance = Lock()

            def __del__(self):
                if self._lock_instance.is_locked:
                    self._lock_instance.release(self._lock_instance.lock_name)
                self._lock_instance.is_locked = False
                del self

            @property
            def lock(self):
                if not self._lock_instance.is_locked:
                    if self._lock_instance.acquire(self._lock_instance.lock_name) is not None:
                        self._lock_instance.is_locked = True
                        return self._lock_instance.lock_name
                    else:
                        return None
                else:
                    return self._lock_instance.lock_name

            @lock.deleter
            def lock(self):
                self._lock_instance.release(self._lock_instance.lock_name)
                self._lock_instance.is_locked = False

            @lock.setter
            def lock(self, name):
                old_lock_name = self._lock_instance.lock_name
                self._lock_instance.lock_name = name
                self._lock_instance.is_locked = False
                self._lock_instance.release(old_lock_name)

        return Locked

    @staticmethod
    def acquire(lock_name):
        if lock_name in Lock.acquired_locks:
            return None
        Lock.acquired_locks.add(lock_name)
        return lock_name

    @staticmethod
    def release(lock_name):
        Lock.acquired_locks.discard(lock_name)


@Lock.locked
class A(str):
    pass
    
    
a, b = A("a"), A("b")
a.lock = "S"       # Регистрация на семафор S
b.lock = "S"       # Регистрация на семафор S
print(a, a.lock)   # Успешный захват семафора S
print(a, a.lock)   # Семафор S уже захвачен нами
print(b, b.lock)   # Неуспешный захват семафора S
del a.lock         # Освобождение семафора S
print(b, b.lock)   # Успешный захват семафора S
b.lock = "T"       # Регистрация на семафор T, освобождает предыдущий семафор
print(b, b.lock)   # Успешный захват семафора T
del b              # Удаление объекта-носителя освобождает семафор
a.lock = "T"       # Регистрация на семафор T, освобождает предыдущий семафор
print(a, a.lock)   # Успешный захват семафора T

# 0 A
# 1 None
# 2 None
# 3 B
# 4 None
# 10 a None
# 10 a None
# 1 a A
# 0 a None
# 0 a None
# 1 a B

# ===
# 1 None
# 2 None
# 3 B
# 4 None
# 10 a None
# 10 a None
# 1 a None
# 0 a None
# 0 a None