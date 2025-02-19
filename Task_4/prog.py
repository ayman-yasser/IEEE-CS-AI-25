import math


def get_numbers():
    valid = False
    while not valid:
        try:
            lst = list(input("Enter a list of numbers: ").split())
            lst = [float(x) for x in lst]
            if len(lst) > 0:
                valid = True
        except :
            lst = list(input("Enter a list of numbers (Numbers only are valid): ").split())
    return lst



lst = get_numbers()



def find_min(numbers):
    mini = numbers[0]
    for i in numbers:
        if mini > i:
            mini = i
    return round(mini)

def find_max(numbers):
    maxi = numbers[0]
    for i in numbers:
        if maxi < i:
            maxi = i
    return round(maxi)

def find_mean(numbers):
    sum = 0.0
    for i in numbers:
        sum += i
    return round(sum/len(numbers),1)

def find_mode(numbers):
    freq = dict()
    for i in numbers:
        if freq.__contains__(i):
            freq[i] += 1
        else:
            freq[i] = 1
    maxi = freq[numbers[0]]
    for i in freq.values():
        if maxi < i:
            maxi = i

    if int(maxi) <= 1:
        return f"No mode"

    lst = []
    for k,v in freq.items():
        if maxi == v:
            lst.append(round(k))
    return lst

def find_median(numbers):
    numbers.sort()
    h = int(len(numbers)/2)
    return round(numbers[h] if len(numbers)%2 == 1 else (numbers[h]+numbers[h-1])/2.0,1)

def find_range(numbers):
    return round(find_max(numbers) - find_min(numbers))

def find_variance(numbers):
    s2 = 0
    M = find_mean(numbers)
    for x in numbers:
        s2 += (x-M)*(x-M)/(len(numbers)-1)
    return round(s2,2)

def find_STD(numbers):
    return round(math.sqrt(find_variance(numbers)),5)

def find_Quariles(numbers):
    numbers.sort()
    h = int(len(numbers)/2)
    lst = []
    for i in range(h):
        lst.append(numbers[i])
    q1 = round(find_median(lst))
    lst.clear()
    for i in range(h,int(len(numbers))):
        lst.append(numbers[i])
    q3 = round(find_median(lst))
    q2 = round(find_median(numbers))
    return (q1,q2,q3)

def find_IQR(numbers):
    quariles = find_Quariles(numbers)
    return round(quariles[2] - quariles[0])

print(f'''Min: {find_min(lst)}
Max: {find_max(lst)}
Mean: {find_mean(lst)}
Mode: {find_mode(lst)}
Median: {find_median(lst)}
Range: {find_range(lst)}
Variance: {find_variance(lst)}
Standard Deviation: {find_STD(lst)}
Quartiles: {find_Quariles(lst)}
Interquartile Range (IQR): {find_IQR(lst)}
''')


