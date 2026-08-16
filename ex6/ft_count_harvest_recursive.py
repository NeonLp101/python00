def ft_count_harvest_helper(i, days_until_harvest):
    if i > days_until_harvest:
        print("Harvest time!")
        return
    print("Day: ", i)
    ft_count_harvest_helper(i + 1, days_until_harvest)


def ft_count_harvest_recursive():
    days_until_harvest = int(input("Days until harvest: "))
    ft_count_harvest_helper(1, days_until_harvest)
