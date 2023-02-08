/**
 Do not return anything, modify nums1 in-place instead.
 */
function merge(nums1: number[], m: number, nums2: number[], n: number): void {
  let i = m-1;
  let j = n-1;
  for(let index = m+n-1; index>= 0 && j>=0  ; index--){
    if(nums1[i] > nums2[j]){
      nums1[index] = nums1[i];
      i--;
    }else{
      nums1[index] = nums2[j];
      j--;
    }
  }

};