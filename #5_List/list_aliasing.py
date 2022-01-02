# yaha things ra a_list duitai list ho ...
# auta list ko refrence or memory location arko lai assign gareko, so yesto lai aliasing vaninxa
# both list le same memory location lai refer gareko xa... auta list ma change garda arko pani chane hunxa


def test(a_list):                                       # things vanni list ko memory location, a_list vanni list lai reference gareko ho
    for index in range(len(a_list)):
        a_list[index] = a_list[index] * 2               # a_list vanni list ko value change hunu vaneko things vanni list ko pani value change hunu nai ho
    print('a_list :', a_list)


things = [2, 5, 'spam', 9.5]
print('Original things list : ', things)

test(things)
print('things list being modified by a_list :', things)



