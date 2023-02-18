from fibonacci import fibonacci


def test_fibo_5(benchmark):
    @benchmark
    def _():
        fibonacci(5)


def test_fibo_10(benchmark):
    @benchmark
    def _():
        fibonacci(10)


def test_fibo_15(benchmark):
    @benchmark
    def _():
        fibonacci(15)
