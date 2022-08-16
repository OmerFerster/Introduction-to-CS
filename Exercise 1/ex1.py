num = input("""Put a 3rd number
""")  # קלט של מס תלת ספרתי

a = int(num) // 100  # ספרת מאות
b = (int(num) - a * 100) // 10  # ספרת עשרות
c = (int(num) - a * 100) - b * 10  # ספרת אחדות

sum_bricks = a + b + c  # סכום כל הלבנים
each_bricks = sum_bricks // 3  # חלוקה שווה של הלבנים בין שלושת החזירים
left_bricks = sum_bricks % 3  # שארית החלוקה ביניהם
okay = left_bricks != 0  # בודק האם נשאר שארית

print("How Much Bricks They Have:", sum_bricks)
print("How Many Bricks Each Pig Got:", each_bricks)
print("Do They Have a Left Overs?", okay)


def fix_age(age):
    if (13 > age or age > 14) and (17 > age or age > 19):
        return age
    else:
        return 0


def filter_teens(d=13, e=13, f=13):
    first_age = fix_age(d)
    second_age = fix_age(e)
    third_age = fix_age(f)
    sum1 = first_age + second_age + third_age
    return sum1


print("Your Teen sum age is:", filter_teens(2, 5, 13))


def are_lists_equal(list1, list2):
    if sorted(list1) == sorted(list2):
        return True
    else:
        return False


first_list = [0.6, 1, 2, 3]
second_list = [3, 2, 0.6, 1]
third_list = [9, 0, 5, 10.5]
print(are_lists_equal(first_list, third_list))


def longest(my_list):
    new_list = sorted(my_list, key=len)
    print("The Longest str is:", new_list[-1])


list_ex = ["111", "234", "2000", "goru", "birthday", "09"]
longest(list_ex)

