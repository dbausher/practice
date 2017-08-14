/*http://practice.geeksforgeeks.org/problems/merge-sort/1*/


/* The task is to complete merge() which is used
in below mergeSort() */
class GfG
{
   // Merges two subarrays of arr[].  First subarray is arr[l..m]
   // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {
      List<Integer> sorted = new ArrayList<>();
      int i = l;
      int j = m + 1 ;
      while(i <= m || j <= r){
        if(i <= m){
          if(j > r || arr[i] <= arr[j] ){
            sorted.add(arr[i]);
            i++;
            continue;
          }
        }
        
        sorted.add(arr[j]);
        j++;
      }

      for(int k = 0;k <= r-l;k++){
        arr[l+k] = sorted.get(k);
      }
    }
}
 /* This method is present in a class other than GfG class .
static void mergeSort(int arr[], int l, int r)
 {
    GfG g = new GfG();
    if (l < r)   
   {
        int m = (l+r)/2;
        mergeSort(arr, l, m);
        mergeSort(arr , m+1, r);
        g.merge(arr, l, m, r);
    }
}*/