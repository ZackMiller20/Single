# Task 1


# num = int(input())
# dict_1 = {i: i ** 2 for i in range(1, num + 1)}
# print(dict_1)


# Task 2


# num = int(input())
# dict_1 = {i: i ** 2 for i in range(1, num + 1)}
# blabla = 0
# for a in dict_1.values():
#     blabla += a
# c = blabla / num
# print(c)


# Task 3


# dict_1 = {i + 2: str(i ** 4) + "abc" for i in range(10)}
# dict_2 = {j: j + 5 for j in range(10)}
# # print(dict_1)
# # print(dict_2)
# # print(len(dict_1))
# # print(len(dict_2))
# if len(dict_1) == len(dict_2):
#     dict_3 = dict_1 | dict_2
#     print(dict_3)
# else:
#     print(dict_1 | dict_2, "Длина была не одинаковая но всё равно объеденил")


# Task 4


cities = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
m1 , m2 = 0, 0
l1 , l2 = 0, 0
p1 , p2 = 0, 0
counter = 1
for x1, x2 in cities.values():
    if counter == 1:
        m1 += x1
        m2 += x2
    elif counter == 2:
        l1 += x1
        l2 += x2
    elif counter == 3:
        p1 += x1
        p2 += x2
    counter += 1

distance_m_l = ((m1 - l1) ** 2 + (m2 - l2) ** 2) ** 0.5
distance_m_p = ((m1 - p1) ** 2 + (m2- p2) ** 2) ** 0.5
distance_p_l = ((p1 - l1) ** 2 + (p2 - l2) ** 2) ** 0.5
print(m1, m2)
print(distance_p_l, distance_m_l, distance_m_p)



# Task 5

