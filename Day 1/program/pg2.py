def sum(*arr):
    result = 0
    for i in arr:
        result += i
    return result

def main():
    arr=[1, 2, 3, 4, 5]
    print(sum(*arr))
          
if __name__ == "__main__":
    main()