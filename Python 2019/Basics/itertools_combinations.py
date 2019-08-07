# Task
#
# You
# are
# given
# a
# string.
# Your
# task is to
# print
# all
# possible
# combinations, up
# to
# size, of
# the
# string in lexicographic
# sorted
# order.
#
# Input
# Format
#
# A
# single
# line
# containing
# the
# string and integer
# value
# separated
# by
# a
# space.
#
# Constraints
#
# The
# string
# contains
# only
# UPPERCASE
# characters.
#
# Output
# Format
#
# Print
# the
# different
# combinations
# of
# string
# on
# separate
# lines.
#
# Sample
# Input
#
# HACK
# 2
# Sample
# Output
#
# A
# C
# H
# K
# AC
# AH
# AK
# CH
# CK
# HK

from itertools import combinations

if __name__ == '__main__':
    a,b=input().split()
    b=int(b)
    final_list=[]
    for i in range(1,b+1):
        A=list(combinations(sorted(a),i))
        final_list.extend(A)
    A = ["".join(x) for x in final_list]
    print(*A, sep='\n')
    # A=list(combinations(sorted(a),b))
    # print(A)
    # A=["".join(x) for x in A] # Joining with empty string.
    # print (*A,sep='\n')







