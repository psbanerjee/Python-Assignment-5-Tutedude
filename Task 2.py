list1 = list(range(1,11,1))                                 #Creates a list of numbers from 1 to 10
print("Original list: {}".format(list1))                    #Prints original list
list2 = list1[0:5:1]                                        #Extracts the first five elements from the list
print("Extracted first five elements: {}".format(list2))    #Prints the extracted elements
list2.reverse()                                             #Reverses the extracted list
print("Reversed extracted elements: {}".format(list2))      #Prints the reversed list