from tabulate import tabulate

def firstFit(block_Size, no_Of_Blocks, process_Size, no_Of_Process, block_Status):
    allocate = [-1] * no_Of_Blocks # Create list to hold IDs of allocated blocks
    print(f"Block list before allocation: {block_Size}")
    print(f"Block status before allocation: {block_Status}")

    for i in range(no_Of_Process): 
        for j in range(no_Of_Blocks): 
            if block_Size[j] >= process_Size[i] and block_Status[j]=="Free": # Check if block is free and there is enough space
                allocate[i] = j+1  # Assign the block j+1 to no_Of_Process[i] process (to avoid count from 0)
                block_Size[j] -= process_Size[i] # Place process in block
                block_Status[j] = "Busy" 
                break # terminate inner loop iteration and go to next iteration of outer loop

    # create "tuples" with each process' block and block status
    results = [(i+1, process_Size[i], allocate[i], block_Size[allocate[i]-1], block_Status[allocate[i]-1]) for i in range(no_Of_Process)] 

    print(tabulate(results, headers=["Process No.", "Process Size", "Block No.", "Block Size", "Block Status"]))
    print(f"\nBlock list after allocation: {block_Size}")
    print(f"Block status after allocation: {block_Status}")


process_Size = [212, 417, 112, 426, 100]
block_Size = [100, 500, 200, 300, 600] 
no_Of_Blocks = len(block_Size) 
no_Of_Process = len(process_Size) 
block_Status = ["Free"] *  no_Of_Blocks

firstFit(block_Size, no_Of_Blocks, process_Size, no_Of_Process, block_Status)