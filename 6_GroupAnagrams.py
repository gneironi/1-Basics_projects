#Anagrams are words formed by rearranging the letters of another word,
#For example, car and arc, cat and act, etc
#Here you will be given a list of words, 
#and you have to write an algorithm to group all the words which are anagrams of each other.


from collections import defaultdict

def group_anagrams(a):
    my_list = defaultdict(list)
    for i in a:
        sorted_i = " ".join(sorted(i))
        my_list[sorted_i].append(i)
    return my_list.values()

words = ["tea", "eat", "bat", "ate", "arc", "car"]
print(group_anagrams(words))



