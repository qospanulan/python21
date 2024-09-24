
class ParametersAreZero(Exception):
    ...


def get_sum(a=0, b=0):
    if a == 0 and b == 0:
        raise ParametersAreZero("а и б равно 0")
    else:
        return a + b


try:
    res = get_sum()
except ParametersAreZero as e:
    res = None
    print(f"Error: {e}")

print(res)
