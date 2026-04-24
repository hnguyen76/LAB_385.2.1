tools =['laptop', 'Monitor', 'Keyboard', 'Mouse']

print(tools[0])

removed = tools[1:3]
print('removed list: ',removed)

tools[1] = 'Webcam' # change the value at index 1 to 'Webcam'
print(tools)

tools.append('Desk')
print(tools)

# #let add headphones to the 1st index
tools.insert(1, 'Headphones')
print(tools)
# # now tool list is ['laptop', 'Headphones', 'Webcam', 'Mouse', 'Desk']
tools.remove('Keyboard') 
print(tools)

# #how many items are in my list of tools?
print('Number of tools:', len(tools))

# Pass by reference
og_list = [1,2,3]

# # Not creating a copy
new_reference = og_list
print('og list: ', og_list)
print('new reference: ', new_reference)

# def appNewThing(list, newitem): #list is a parameter, newitem is a parameter
def appNewThing(list, newitem): #list is a parameter, newitem is a parameter
    list.append(newitem)        

appNewThing(og_list, 7) #og_list is an argument, 7 is an argument
print('og list after function call: ', og_list) #og_list is changed because it is passed by reference, meaning the function modifies the original list.

def add3(num): # define a function that takes a number as an argument and adds 3 to it
    num += 3   
    print('num inside function: ', num) #num is a local variable, it is not the same as the original variable outside the function

print(og_list == new_reference) #True, because they reference the same list in memory

ref2 = [1,2,3,4]
print(ref2 == new_reference) #False, because they are different lists in memory, even though they have the same values
print(ref2 == og_list) #False, because they are different lists in memory, even though they have the same values    

# Deep copy - for when you want to create a new list that is a copy of the original list, but is not the same list in memory
# creates a new list that is a copy of the original list, but is not the same list in memory
new_deep_copy = og_list.copy()

new_deep_copy.append(10) # adds 10 to the new deep copy list
print('new deep copy: ', new_deep_copy) # new deep copy list is [1, 2, 3, 7, 10]
print('og list: ', og_list) # og list is [1, 2, 3, 7] because it is not changed by the function call that modified the new deep copy list



#Part 3
#List and Functions
recent_first = [1989, 1991, 1997, 2000]
recent_last = [2022,2018,2016,2011]

def reorder_years(recentFirst, recentLast): # define a function that takes two lists of years as arguments and reorders the years in each list from oldest to newest
    recentLast.reverse() # reverse the recentLast list to reorder it from oldest to newest
    recentFirst.extend(recent_last) # extend the recentFirst list with the recentLast list to combine the two lists into one list
    return recentFirst # return the combined list of years

reorder_years(recent_first, recent_last) # call the function with the recentFirst and recentLast lists as arguments
print('reordered years: ', recent_first) # print the reordered list of years, which is now [1989, 1991, 1997, 2000, 2011, 2016, 2018, 2022]
