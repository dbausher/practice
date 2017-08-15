/*http://practice.geeksforgeeks.org/problems/heap-sort/1*/


class GfG
{
    void buildHeap(int arr[], int n)
    {
        for(int i = n-1; i >=0; i--){
            heapify(arr,n,i);
        }
        //Had to include this here because I'm pretty sure the website forgot it
        heapSort(arr,n);
        
    }
    
    void heapSort(int arr[], int n){
        for(int i = n-1; i >=0; i--){
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;
            heapify(arr,i,0);
        }
    }
 
    // To heapify a subtree rooted with node i which is
    // an index in arr[]. n is size of heap
    void heapify(int arr[], int n, int i)
    {
        //System.out.println(Arrays.toString(arr));
        int max = i;
        int leftIndex = (i*2) + 1;
        int rightIndex = (i*2) + 2;

        if(leftIndex < n && arr[leftIndex] > arr[max]){
            max = leftIndex;
        }

        if(rightIndex  < n && arr[rightIndex] > arr[max]){
            max = rightIndex;
        }

        if(max != i){
            int temp = arr[i];
            arr[i] = arr[max];
            arr[max] = temp;
            heapify(arr,n,max);
        }
    }
 }