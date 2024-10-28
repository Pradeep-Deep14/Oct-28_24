def func(bools: list):
    if bools.count(True)==len(bools)\
            or bools.count(False)==len(bools):
        return True
    else:
        return False
    
print(func([False,False,True]))