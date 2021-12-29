"""21.1L5Q3 - Senhor das Buscas"""

def bubble_sort(arr: list) -> list:
    """Sort a list array (int/float) and return sorted list."""

    # Create new list to be more safe
    new_arr: list = arr.copy()

    # Sort process
    for j in range(len(new_arr) - 1):
        for k in range(len(new_arr) - 1):
            if new_arr[k] > new_arr[k+1]:
                new_arr[k], new_arr[k+1] = new_arr[k+1], new_arr[k]
    return new_arr


def binary_search(arr: list, start, end, item) -> int:
    """Optimized search recursive algorithm and return the index of item found or -1 (not found)."""

    # Index middle list
    middle = (start + end) // 2

    # Base cases
    if end < start:
        return -1
    if arr[middle] == item:
        return middle

    if item > arr[middle]:
        return binary_search(arr, middle + 1, end, item)
    else:
        return binary_search(arr, start, middle - 1, item)


# Number of battalions waited
battalions_amount: int = int(input())

# Process to append valid battalions
battalions: list = []
for i in range(battalions_amount):
    battalion_size: int = int(input())
    if battalion_size >= 0:
        battalions.append(battalion_size)

# Sort battalions and input amount of wished battalions
battalions = bubble_sort(battalions)
searches_amount: int = int(input())

# Process to find the battalions and print them
for i in range(searches_amount):
    size: int = int(input())
    search: int = binary_search(battalions, 0, len(battalions)-1, size)
    if search == -1:
        print(f"Busca falhou: {search}")
    else:
        print(f"Busca com sucesso: {search}")
