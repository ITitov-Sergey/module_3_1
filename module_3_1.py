calls = 0
def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    tuple_1 = len(string)
    tuple_2 = string.upper()
    tuple_3 = string.lower()
    tuple_ = (tuple_1, tuple_2, tuple_3)
    print(tuple_)


def is_contains(string, list_to_search=None):
    if list_to_search is None:
        list_to_search = []
    count_calls()
    list_to_search_2 = [name.lower() for name in list_to_search]
    res = string.lower() in list_to_search_2
    print(res)


string_info("Urban")
string_info("University")
is_contains("dog", ["Dog", "Cat", "Bear"])
is_contains("Dog", ["dog", "cat", "bear"])
is_contains("Hawk", ["Dog", "Cat", "Bear"])
print(calls)