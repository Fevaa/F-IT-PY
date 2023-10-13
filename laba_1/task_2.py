# TODO Найдите количество книг, которое можно разместить на дискете
simb = 4
co_sim = 25
co_st = 50
co_str = 100
disk = 1440000
book = simb*(co_sim*co_st*co_str)
book_c = round(disk/book)
print("Количество книг, помещающихся на дискету:", book_c)

