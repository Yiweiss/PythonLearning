import math


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5,67, 32)")


def get_user_input(_inp):
    return [float(val) for val in _inp.split(",")]


def calc_average(nums):
    return sum(nums)/len(nums)


def find_min_max(nums):
    return [min(nums), max(nums)]


def sort(nums):
    return sorted(nums)


def calc_median(nums):
    if len(nums) % 2 == 0:
        return (sort(nums)[math.floor(len(nums)/2)] + sort(nums)[math.floor(len(nums)/2)-1])/2
    return sort(nums)[math.floor(len(nums)/2)]


def main():
    display_main_menu()
    userInput = get_user_input(input())
    print(userInput)
    print(calc_average(userInput))
    print(find_min_max(userInput))
    print(sort(userInput))  
    print(calc_median(userInput))




if __name__ == "__main__":
    main()
