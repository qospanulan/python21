import time


def running_time(my_func):
    def wrapper(a, b):
        print("Starting...")
        start_time = time.time()

        res = my_func(a, b)

        time.sleep(1)
        end_time = time.time()
        print("Finished!")
        print(f"Running time: {end_time - start_time}")
        return res

    return wrapper


@running_time
def get_sum(a, b):

    return a + b


@running_time
def get_pow(x, n):

    return x ** n


res = get_sum(1, 6)
print(f"result: {res}")
print("================================================")

res = get_pow(3, 3)
print(f"result: {res}")


