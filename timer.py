import time


class Timer:

    def __init__(self, count, f=None, param=None):
        self.count = count  # количество попыток
        self.param = param  # аргумент для функции
        self.f = f  # функция

    def __call__(self, *args):
        for i in args:
            if callable(i):
                self.f = i
                return self.timecheck(self.f)

    def __enter__(self):
        self.t0_cont = time.time()
        for _ in range(self.count):
            result = self.f(self.param)
        self.t1_cont = time.time()
        avrg_time = (self.t1_cont - self.t0_cont) / self.count
        print('Среднее время выполнения из контекстного оператора %.7f seconds' % avrg_time)
        return result

    def __exit__(self, *args, **kwargs):
        return self

    def timecheck(self, func):  # декоратор
        count = self.count
        func = self.f
        argum = self.param

        def wrapper(argum):
            t0 = time.time()
            for _ in range(count):
                func(argum)
            t1 = time.time()
            avrg_time = (t1 - t0) / count
            print('Среднее время выполнения из декоратора %.7f seconds' % avrg_time)
            return func(argum)

        return wrapper


# тут можно создать экземпляр класса Timer, в аргументах количество повторений функции. Нужен только для декоратора
# d = Timer(2)

# одна из функций для проверки
# @d
# def f1(x):
#     x = 1
#     a = 0
#     for i in range(1000):
#         a += x
#     return a


# Функция построения ряда фиббоначи бля проверки. Используется yield, так что скорее всего всегда будет "0" :)
#
# @d
# def fibo_gen(l):
#     f, s = 1, 1
#     for i in range(l):
#         yield f
#         f, s = s, f + s


# Функция для проверки
# @d
def quad(x):
    for i in range(x):
        r = i ** 4
    return r


# fi - для проверки декоратором, раскомменть если надо
# fi = quad(1000)
# print(fi)
# для проверки контекстом. Одновременно и декоратором и контекстом одну и ту же функцию проверить не выйдет
# синтаксис Timer(количество попыток, f=функция, param=аргумент для функции)


with Timer(2, f=quad, param=1000) as a:
    pass
print(a)
