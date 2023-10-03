def tryexcept (a:int, b:int) -> int: 
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Please provide two integers or floats"
    except:
        return "Something went wrong"
    
a = tryexcept(1,0)
print(a)