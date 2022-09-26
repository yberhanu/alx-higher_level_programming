#!/usr/bin/python3
""" inheritance class form list """
class MyList(list):
    """ inherits list """
    def append(self, element):
        return list.append(self, element)

    def print_sorted(self):
        """ print in sorted order """
        s = self[:]
        s.sort()
        print(s)
