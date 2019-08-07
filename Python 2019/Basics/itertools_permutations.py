from itertools import permutations


# Input (stdin)Download
# HACK 2
# Expected OutputDownload
# AC
# AH
# AK
# CA
# CH
# CK
# HA
# HC
# HK
# KA
# KC
# KH


if __name__ == '__main__':
    a,b=input().split()
    b=int(b)
    A=list(permutations(sorted(a),b))
    #print(A)
    A=["".join(x) for x in A] # Joining with empty string.
    print (*A,sep='\n')
