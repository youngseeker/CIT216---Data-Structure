def generate_permutations(nums, start, end):
    # Base Case: If we are at the last index, we have a complete permutation
    if start == end:
        print(nums)
    else:
        # Loop through the list from the 'start' index to the end
        for i in range(start, end + 1):
            
            # STEP 1: SWAP (The Choice)
            # We place the element at index 'i' into the 'start' position
            nums[start], nums[i] = nums[i], nums[start]
            
            # STEP 2: RECURSE (The Dive)
            # We move to the next position (start + 1) and repeat
            generate_permutations(nums, start + 1, end)
            
            # STEP 3: BACKTRACK (The Undo)
            # Critical: We swap them back to restore the original order
            # This ensures the list is clean for the next iteration of the loop
            nums[start], nums[i] = nums[i], nums[start] 

# Driver Code
my_list = [1, 2, 3]
generate_permutations(my_list, 0, len(my_list) - 1)