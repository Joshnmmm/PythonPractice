if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    arr = list(dict.fromkeys(arr))
    maxNum = arr[0]
    arr.remove(maxNum)
    runnerUp = arr[0]
    print(runnerUp)