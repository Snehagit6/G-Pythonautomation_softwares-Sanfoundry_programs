def binary_search(x):
    arr = [1,4,9,89,56]

    l_i, f_i = len(arr)-1, 0

    while l_i>f_i:
        mid = (l_i+f_i)//2
        if x == arr[mid]:
            print(f"Element{x} found at {mid}")
            return mid
        elif x>arr[mid]:
            f_i = mid+1
        elif x<arr[mid]:
            l_i= mid-1
            
    return -1

def recursive_binary_search(l_i,f_i,x):


    while l_i>f_i:
        mid = (l_i+f_i)//2
        if x == arr[mid]:
            print(f"Element{x} found at {mid}")
            return mid
        elif x>arr[mid]:
            f_i = mid+1
            return binary_search(l_i,f_i,x)
        elif x<arr[mid]:
            l_i= mid-1
            return binary_search(l_i,f_i,x)
            
    return -1
        

if __name__ =="__main__":
    arr = [1,4,9,29,56]
    t1 = process_time()
    #if binary_search(-9)==-1:
        #print("Element notfound")
    if binary_search(len(arr)-1,0,56)==-1:
        print("Element notfound")
    t2 = process_time()
    print(f"Process time: {t2-t1}")
        







