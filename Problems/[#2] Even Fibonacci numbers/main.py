class FibonnacciCache(object):
    def __init__(self, size=100, startup=5):
        self.size = size
        self.cache = {}
        self.startup = startup

    def __call__(self, func):
        def _access_cache(*args, **kwargs):
            key = str(args) + str(kwargs)
            hit = self.cache.get(key)
            if hit is not None:
                hit[0] += 1
                result = hit[1]
            else:
                result = func(args[0])
                self.cache[key] = [self.startup, result]
                if len(self.cache) > self.size:
                    low_score = [self.startup, key]
                    for _key, _value in self.cache.items():
                        if _value[0] < low_score[0]:
                            low_score = [_value[0], _key]
                    del self.cache[low_score[1]]
            return result
        return _access_cache


@FibonnacciCache()
def fibbonacci_recursive(n: int):
    if n == 0 or n == 1:
        return n
    else:
        return fibbonacci_recursive(n - 1) + fibbonacci_recursive(n - 2)


def _fibbonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


def fibonnacci_generated(n: int):
    gen = _fibbonacci_generator()
    val = next(gen)
    for i in range(1, n+1):
        val = next(gen)
    return val


if __name__ == '__main__':
    sum_fib = 0
    limit = 4000000
    for value in _fibbonacci_generator():
        if value > limit:
            break
        elif value % 2 == 0:
            sum_fib += value
    print(sum_fib)
