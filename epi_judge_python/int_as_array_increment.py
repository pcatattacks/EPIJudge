from test_framework import generic_test


def plus_one(A):
    # TODO - you fill in here.
    # return []
    
    A.reverse()
    for i in range(len(A)):
        if A[i] + 1 == 10:
            A[i] = 0
            if i == len(A) - 1:
                A.append(1)
        else:
            A[i] += 1
            break
    
    A.reverse()
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
