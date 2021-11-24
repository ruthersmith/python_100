def func_args(*args):
    print(args)


def use_kwargs(**kwargs):
    print(kwargs)


if __name__ == "__main__":
    func_args('2', '3', '2')
    use_kwargs(add=5, car=4)
