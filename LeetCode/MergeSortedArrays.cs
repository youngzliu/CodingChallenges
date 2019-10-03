public class Solution {
    public void Merge(int[] nums1, int m, int[] nums2, int n) {
        int current1 = m-1; //pointer to first list in two pointer method
        int current2 = n-1; //pointer to second list in two pointer method
        for(int i = nums1.Length - 1; i >= 0; i--){ //iterate backwards from end of list to keep memory to o(1)
            if((current2 < 0) || (current1 >= 0 && nums1[current1] > nums2[current2])){
                nums1[i] = nums1[current1];
                current1--;
            }
            else{
                nums1[i] = nums2[current2];
                current2--;
            }
        }
    }
}