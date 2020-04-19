# **************************************************************************** #
#                                                                              #
#                                                __________________________    #
#    counting_elements.py                        _______ ______   ______ __    #
#                                                ___    |___  /   ___  //_/    #
#    By: akovalyo <al.kovalyov@gmail.com>        __  /| |__  /    __  ,<       #
#                                                _  ___ |_  / ___ _  /| |      #
#    Created: 2020/04/07 20:11:42 by akovalyo    /_/  |_|/_/  _(_)/_/ |_|      #
#    Updated: 2020/04/07 20:11:42 by akovalyo    __________________________    #
#                                                                              #
# **************************************************************************** #

class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr.sort()
        copy_arr = arr.copy()
        count = 0
        for nbr in arr:
            if nbr + 1 in copy_arr:
                count += 1
                copy_arr.remove(nbr)
        return count
