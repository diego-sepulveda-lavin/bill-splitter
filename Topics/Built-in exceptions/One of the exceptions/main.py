exception_number = int(input())
exceptions = dir(locals()['__builtins__'])
print(exceptions[exception_number])
