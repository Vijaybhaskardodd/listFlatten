from functools import reduce

'''
flatten function takes one input parameter which may contain hierarchical list of integers 
and flatten to single dimension List. 

First parameter of lambda function calls same function recursively if first element of array is list type
 ( [x] , flatten(x) ) [type(x) == list]

Second parameter of lambda function calls same function recursively if second element of array is list type
( [y] , flatten(y) ) [type(y) == list]

reduce function pulls the elements in array till the end and append to array

last part of code executes for least granular element
if  type(hierachial_list) == list and len(hierachial_list) > 1 else hierachial_list

'''
def flatten(hierarchical_list):
    try:
        return reduce(lambda  x , y: \
                      ( [x] , flatten(x) ) [type(x) == list]  \
                    + ( [y] , flatten(y) ) [type(y) == list] \
                      , hierarchical_list )  \
        if  type(hierarchical_list) == list and len(hierarchical_list) > 1 else hierarchical_list
    except(Exception):
        print("Error :--" + Exception)
        raise

