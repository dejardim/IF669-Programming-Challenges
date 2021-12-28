"""21.1L1Q7 - Programador do spotify"""

name_1: str = input(); views_1: int = int(input())
name_2: str = input(); views_2: int = int(input())
name_3: str = input(); views_3: int = int(input())

# (WHAT_IS): conditional structure to "order" the most viewed songs
if views_1 == views_2 and views_2 == views_3:
    # (a, a, a)
    pass
elif views_1 == views_2:
    # (a, a, b) when b > a
    if views_1 < views_3:
        name_1, name_2, name_3 = name_3, name_1, name_2
        views_1, views_3 = views_3, views_1
    else:
        pass
elif views_1 == views_3:
    # (a, b, a) when b > a
    if views_1 < views_2:
        name_1, name_2 = name_2, name_1
        views_1, views_2 = views_2, views_1
    else:
        name_2, name_3 = name_3, name_2
        views_2, views_3 = views_3, views_2      
elif views_2 == views_3:
    # (b, a, a) when a > b
    if views_1 < views_2:
        name_1, name_2, name_3 = name_2, name_3, name_1
        views_1, views_3 = views_3, views_1
    else:
        pass
else:
    if views_2 < views_3:
        """(a, b, c) if b < c, then aux=b -> b = c and c = aux"""
        name_2, name_3 = name_3, name_2
        views_2, views_3 = views_3, views_2

    if views_1 < views_3:
        """(a, b, c) if a < c, then aux=a -> a = c and c = aux"""
        name_1, name_3 = name_3, name_1
        views_1, views_3 = views_3, views_1

    if views_1 < views_2:
        """(a, b, c) if a < b, then aux=a -> a = b and b = aux"""
        name_1, name_2 = name_2, name_1
        views_1, views_2 = views_2, views_1

# (WHAT_IS): The prints of results
print(f"{name_1} {views_1}")
print(f"{name_2} {views_2}")
print(f"{name_3} {views_3}")
