/*http://practice.geeksforgeeks.org/problems/insertion-sort/1*/


/* The task is to complete insert() which is used 
   as shown below to implement insertionSort() */
/* Function to sort an array using insertion sort
void insertionSort(int arr[], int n)
{
  GfG obj = new GfG();
   for (int i = 1; i < n; i++)
      obj.insert(arr, i);
} */
class GfG
{
  // Function to sort an array using insertion sort
  void insert(int arr[],int i)
  {
       if(arr[i - 1] < arr[i]){
        return;
       }
       int j = 0;
       while(arr[j] < arr[i]){
        j++;
       }
       int prev = arr[j];
       arr[j] = arr[i];
       for(int k = j+1 ;k <= i ;k++) {
        int temp = arr[k];
        arr[k] = prev;
        prev = temp;
       }

  }
}