import time
def factors(target, arr):
    '''
    The factors function returns an object with a list of all cobminations of factors that multiply up to a given number, from a given array of numbers. Both JavaScript and Python versions of this library are provided.

    Parameters:

        (1) target
            The number (integer or float0 being sought (integer or
            float, cientific notation accepted).

        (2) arr
            A numeric array of numbers from which to draw potential
            factor combinations. Text, boolean values and objects
            are ignored.


    Output:
    An object with the following properties:

        (1) array
            The array used to compute factors with only numeric
            values kept.

        (2) target
            The value for which factors are being sought.

        (3) combinations
            An array with all found combinations of factors
            that sum up to the 'target' number.

        (4) iterations
            The total number of sums explored when searching
            with all possible combinations of factors.

        (5) time
            Processing time, in milliseconds.

    '''

    # Parameters test/fix
    if target == None or target == 0 or arr == None or len(arr) < 2:
        return None

    # Declarer
    start = int(round(time.time() * 1000))
    global iterations
    global combinations
    iterations=0
    combinations=[]

    # Keep only non-zero numbers
    arr = [x for x in arr if isinstance(x, float) or isinstance(x, int)]
    if len(arr) <= 1:
        return None

    # Sort
    arr.sort()

    # Recurse each array element
    for j in range(len(arr)):
        i = j
        r = []
        def recurse(v, i):
            global iterations, combinations
            while i < len(arr) and (v*arr[i-1]) < abs(target):
                iterations += 1
                r.append(arr[i])
                recurse(v*arr[i], i+1)
                i += 1
                r.pop()
            if v == target and len(r) > 1:
                combinations.append("".join(str(r)))
            return 1
        r.append(arr[j])
        recurse(arr[j], j+1)

    # Return
    return {
        "combinations": combinations
        , "count": len(combinations)
        , "time": str(int(round(time.time()*1000))-start) + " ms"
        , "array": arr
        , "target": target
        , "iterations": iterations
    }



