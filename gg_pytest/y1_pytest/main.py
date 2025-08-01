def get_weather_details(temp):
    if temp > 25:
        return "Hot"
    else:
        return "Cold"    


def add(a,b):
    return a + b


def divide(n,d):
    if d == 0:
        raise ValueError("Cannot divide by zero")
    
    return n / d    