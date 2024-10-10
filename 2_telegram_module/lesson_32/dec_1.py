import time


def get_sum(a, b):

    return a + b


def get_pow(x, n):

    return x ** n


start_time = time.time()
res = get_sum(1, 6)
time.sleep(1)
end_time = time.time()

print(f"result: {res}")
print(f"running time: {end_time - start_time}")

start_time = time.time()
res = get_pow(2, 3)
time.sleep(1)
end_time = time.time()

print(f"result: {res}")
print(f"running time: {end_time - start_time}")

