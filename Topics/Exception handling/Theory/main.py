#  You can experiment here, it won’t be checked
def my_func():
    try:
        1/0
    except:
        1/0
    finally:
        return 'Ok'



print(my_func())
