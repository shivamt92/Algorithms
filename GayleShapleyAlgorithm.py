
"""    STABLE MATCHING : GAYLE SHAPLEY ALGORITHM  """
import time

def GayleShapley(n, men, women):

    """
    :param n : Number of Men or Women in the System
    :param men: List of men with their preferences
    :param women: List of women with their preferences

    :returns List:  List of matchings
    """

    # Result to be returned initially empty
    result = [None] * n
    # Stack of free men. All men are first placed in this
    free_men = [i for i in range(n - 1, -1, -1)]
    # A pointer for each man which points to the index where the man is supposed to propose
    men_pointer = [0] * n
    # pointer for each woman pointing to the index of the man she is married to in her own list
    women_pointer = [-1] * n

    while free_men:
        # Man is popped from stack
        man = free_men.pop()

        while result[man] == None:

            # If the woman is unmarried then her pointer will be -1. So the man and woman become engaged

            if women_pointer[men[man][men_pointer[man]]] == -1:
                result[man] = men[man][men_pointer[man]]
                women_pointer[result[man]] = women[result[man]].index(man)

            # If the woman is married the men_pointer will move forward

            elif women_pointer[men[man][men_pointer[man]]] < women[men[man][men_pointer[man]]].index(man):
                men_pointer[man] += 1

            # Now the woman prefers this man. She will accept and reject the other man who will be appended to the free_men stack
            else:
                new_free = women[men[man][men_pointer[man]]][women_pointer[men[man][men_pointer[man]]]]
                free_men.append(new_free)
                result[new_free] = None
                result[man] = men[man][men_pointer[man]]
                women_pointer[result[man]] = women[men[man][men_pointer[man]]].index(man)

    return result


if __name__ == '__main__':

    path = '/Users/user/Downloads/public_test_cases_q2/Test'

    for i in range(5):

        print('\n\n Test Case: '+str(i) + '\n')
        now = time.time()
        file = path+str(i)+'in.txt'
        result = []
        with open(file, 'r') as file:
            for line in file.readlines():
                result.append([int(i) for i in line.split(' ') if i!='\n'])

        men = result[1:result[0][0] + 1]
        women = result[result[0][0] + 1:]

        try:

            output = GayleShapley(result[0][0],men,women)

        except (IndexError, ValueError, KeyError):

            print('Test ', i, 'Failed')

        true_op = []
        fileop = path+str(i)+'out.txt'
        with open(fileop, 'r') as file:
            for line in file.readlines():
                true_op.append(int(line))

        end = time.time()
        if true_op == output:
            print('Test Passed in {0:.3f} '.format(end-now), 'seconds')
        else:
            print('Failed')










