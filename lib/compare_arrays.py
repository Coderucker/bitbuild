def compare_arrays(arr1, arr2):
    result = []
    for x in arr1:
        for j in arr2:
            print(f"X: {x} J: {j}", x != j)
            if x != j:
                result.append(x)
                break
    
    print(result)

compare_arrays(["./internals/main.py", "code.py", "./aaa/"], ["./internals/main.py", "./aaa/", "internals/main.py"])