# Task 1:
def sum_series(number):

    if number < 0:
        return number + 1
    if number == 0:
        return number
    else:
        return number + sum_series(number-2)


# Task 2
def drill_sum(data):
    if type(data) is int:
        return data

    sum = 0

    for element  in data:
        sum += drill_sum(element)
    return sum


# Task 3 v2 # giving me 14 instead of 15 so it needs to be fixed
def count_pages(list_of_pages):
    count = 1
    for i in range(len(list_of_pages)):
        if "pages" not in list_of_pages[i].keys():
            print("page not there")
            print(list_of_pages[i].keys())
            count += len(list_of_pages)
            return count
        for element in list_of_pages[i]["pages"]:
            if "page" not in element.keys():
                print("page not found in element")
                count += len(list_of_pages[i]["pages"]) + count_pages(list_of_pages[i]["pages"])
                return count

            else:
                print("page found in element")
                print(element["pages"])
                count += len(element["pages"]) + count_pages(element["pages"])
                return count



if __name__ == '__main__':
    # print(sum_series(7))
    # print(sum_series(8))
    # print(sum_series(15))

    # test_data1 = [
    #     1,
    #     [1, 2],
    #     [1, [2, 3]],
    #     [1, [2, [3, 4]]],
    #     [1, [2, [3, [4, 5]]]],
    # ]
    #
    # test_data2 = [
    #     [1, [[2, 6], [3, 4]]],
    #     [[5, 6, [7, 8]], [2, [3, [4, 5]]]],
    #     [1, [2, 3]],
    #     [1, 2],
    #     1,
    # ]
    # print(drill_sum(test_data1))
    # print(drill_sum(test_data2))

    test_data1 = [
        {
            "title": "Home",
            "pages": [
                {
                    "title": "About",
                    "pages": [
                        {
                            "title": "The company"
                        },
                        {
                            "title": "Our services"
                        },
                        {
                            "title": "Our products"
                        },
                        {
                            "title": "Our deliveries",
                            "pages": [
                                {
                                    "title": "National"
                                },
                                {
                                    "title": "International"
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "Shop",
                    "pages": [
                        {
                            "title": "Browse all"
                        },
                        {
                            "title": "Categories"
                        }
                    ]
                },
                {
                    "title": "My account",
                    "pages": [
                        {
                            "title": "Settings"
                        },
                        {
                            "title": "Edit profile"
                        },
                        {
                            "title": "My transactions"
                        }
                    ]
                }
            ]
        }
    ]


    test_data2 = [
        {"title": "something",
         "pages": [
             {"title": "something",
              "pages": [{"title": "something",
                         "pages": [{"title":"ghhhgh"}]}
                        ]
              }

         ]
         }
    ]
    test_data3= [
        {"title":"something2"}
    ]
    print(count_pages(test_data1))



