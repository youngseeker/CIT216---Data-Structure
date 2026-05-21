public class SelectionSort {
    public static void main(String[] args) {
        int nums[] = {6, 5, 2, 8, 9, 4};
        int size = nums.length;
        int temp = 0;
        int minIndex = -1;

        System.out.println("Before sorting:");
        for(int num : nums) {
            System.out.print(num + " ");
        }

        for(int i = 0; i < size - 1; i++) 
            {
            minIndex = i;
            for(int j = i + 1; j < size; j++) 
                {
                if(nums[j] < nums[minIndex]) 
                    {
                    minIndex = j;
                }
            }
            temp = nums[i];
            nums[i] = nums[minIndex];
            nums[minIndex] = temp; 

            for(int num : nums) {
            System.out.print(num + " ");
        } 
        }
        System.out.println();
        System.out.println("\n\nAfter sorting:");
        for(int num : nums){
            System.out.print(num + " ");
        }
        }

    }
