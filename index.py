# import pandas as pd
# stu={
#     'name':['ayush','saad','karan','ashi'],
#     'cls':[11,9,12,5],
#     'result':['pass','fail','pass','fail']

# }
# df=pd.DataFrame(stu,index=['one','two','three','four'])
# for key,value in df.iteritems():
#     print(key)
#     print(value)

# import pandas as pd

# stu = {
#     'name': ['ayush', 'saad', 'karan', 'ashi'],
#     'cls': [11, 9, 12, 5],
#     'result': ['pass', 'fail', 'pass', 'fail']
# }

# df = pd.DataFrame(stu, index=[1,2,3,4])

# for key, value in df.items():
#     print(key)
#     print(value)


# import pandas as pd
# stu = {
#     'name': ['ayush', 'saad', 'karan', 'ashi'],
#     'cls': [11, 9, 12, 5],
#     'result': ['pass', 'fail', 'pass', 'fail']
# }

# df = pd.DataFrame(stu, index=[1,2,3,4])
# print(df)
# for key, value in df.iterrows():
#     print(key)
#     print(value)


import pandas as pd

stu = {
    'name': ['ayush', 'saad', 'karan', 'ashi'],
    'cls': [11, 9, 12, 5],
    'result': ['pass', 'fail', 'pass', 'fail']
}
df = pd.DataFrame(stu, index=[1,2,3,4])
for key in df.itertuples():
    print(key)
    # print(value)