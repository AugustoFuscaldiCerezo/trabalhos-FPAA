def maxmin_select(arr): #1

    n = len(arr) #2
 
    if n == 1: #3
        return arr[0], arr[0] #4

    else:
        mid = n // 2 #5

        max1, min1 = maxmin_select(arr[:mid]) #6
        max2, min2 = maxmin_select(arr[mid:]) #7

        if max1 > max2: #8
            maximum = max1 #9
        else: 
            maximum = max2 #10
        if min1 < min2: #11
            minimum = min1 #12
        else: 
            minimum = min2 #13

        return maximum, minimum #14

def main():
    n = int(input("Digite a quantidade de números inteiros: "))
    arr = []
    for i in range(n):
        num = int(input(f"Digite o número {i+1}: "))
        arr.append(num)

    maximum, minimum = maxmin_select(arr)
    print(f"Maior elemento: {maximum}")
    print(f"Menor elemento: {minimum}")

if __name__ == "__main__":
    main()
