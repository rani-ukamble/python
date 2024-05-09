# d = ['hey' , 'You', 'are', 'Awesome']
# for i in d:
#     print(i)
    
# # print(dir(d))

# itr = iter(d)

# print(itr)

# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))


# for key in {'a':1, 'b': 2}:
#     print(key)
    
# for char in "1234":
#     print(char)

def process():
    try:
        with open("F:\\Rani\\Rani UPwork - Empowering Solutions Through ML, Ma.txt") as f:
            for line in f:
                print(line, end=' ')
    except FileNotFoundError as e:
        print("File not found")

process()
