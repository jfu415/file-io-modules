""" This file is part of the File I/O exercise.

It should be used with the two input files, fruits_1.txt and fruits_2.txt."""

def open_and_read_file(filename):
    """Opens file as a file object and returns list of contents."""

    file_list = open(filename)
    #file_list_print = file_list.read()
    #print file_list_print
    newlist = []
    for item in file_list:
        newlist.append(item)
    print newlist
    file_list.close()




def compare(lst1, lst2):
    """Takes in two lists and returns a list of items in common. """
   
    # Write your code below.


    pass


# Call your functions at the bottom, after they've been defined.
open_and_read_file("fruits_1.txt")