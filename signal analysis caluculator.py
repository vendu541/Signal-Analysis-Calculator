def signal_analysis(arr, n):
    result = 0

    for value in arr:
        result += value * n

    return result


arr = list(map(int, input("Enter array: ").split()))
n = int(input("Enter n: "))

answer = signal_analysis(arr, n)

print("Output:", answer)