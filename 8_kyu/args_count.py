def args_count(*arg, **args):
    lists = arg
    dicts = args
    count = len(arg) + len(args)
    return count