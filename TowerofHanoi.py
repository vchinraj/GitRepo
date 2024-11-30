def tower_of_hanoi(n,source,target,axiliary):

    if n==1:
        print(f"Move disk {n} from {source} to {target} ")
        return
    
    else:
        tower_of_hanoi(n-1,source,axiliary,target)

        print(f"Move disk {n} from {source} to {target} ")

        tower_of_hanoi(n-1,axiliary,target,source)


n=3
result=tower_of_hanoi(n,'A','B','C')
print(result)