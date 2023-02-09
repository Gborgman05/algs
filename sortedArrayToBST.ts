class TreeNode {
      val: number
      left: TreeNode | null
      right: TreeNode | null
      constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
          this.val = (val===undefined ? 0 : val)
          this.left = (left===undefined ? null : left)
          this.right = (right===undefined ? null : right)
      }
  }

function sortedArrayToBST(nums: number[], hi: number = nums.length-1, low: number =0): TreeNode | null {
    if (nums.length == 0) return null;
    if(nums.length == 1) return new TreeNode(nums[0]);

    var piv = Math.floor(nums.length / 2);

    return new TreeNode(
    nums[piv],
    sortedArrayToBST(nums.slice(0, piv)),
    sortedArrayToBST(nums.slice(piv+1, nums.length))
    );
    

};