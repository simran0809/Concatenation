#creating constructor 

text = "python"
print(list(text))

my_list = []
my_list = [10,20,30,40]
print(my_list)

List = [20,30,40,50]
print(List[1:5])
print(List[2 :])
print(List[: :])
print(list(List))


hm = "hekkookoo"
print(hm[1:5])
print(hm[2 :])
print(hm[: :])
print(list(hm))


list1 = "hii"
list2 = "binny"
print(list1+list2)


#Concatenating means obtaining a new string that contains both of the original strings. In Python, there are a few ways to concatenate or combine strings. The new string that is created is referred to as a string object.


# 1. Using the + operator sumUp both strings .

my_string1 = "Today"
my_string2 = "Day is awesome"
combined_string = my_string1+""+my_string2
print(combined_string)


#2 Join () method  
#by , can be separated using single list if we want to use 
# and join along with string 

y_strings = ["Awesome day", "for Rainny"]  
combined_string = " " .join(y_strings)
print(combined_string)


#3 f"string" formatted string literals  
#different string then combined with f"{string}{string}""

my_sim = "Nice"
my_si = "Day"
my_combine = f"{my_sim} {my_si}"
print(my_combine)

#https://www.datacamp.com/tutorial/python-concatenate-strings