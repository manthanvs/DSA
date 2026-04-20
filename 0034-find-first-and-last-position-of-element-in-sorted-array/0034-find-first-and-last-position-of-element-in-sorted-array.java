class Solution {
  public int[] searchRange(int[] nums, int target) {
    int ans[] = { -1, -1 };

    int first = binarySearch(nums, target, true);
    int last = binarySearch(nums, target, false);

    ans[0] = first;
    ans[1] = last;
    return ans;
  }

  static int binarySearch(int[] arr, int target, boolean findStartIndex) {
    int ans = -1;
    int start = 0;
    int end = arr.length - 1;

    while (start <= end) {
      int mid = (start + end) / 2;

      if (target < arr[mid]) {
        end = mid - 1;
      } else if (target > arr[mid]) {
        start = mid + 1;
      } else {
        ans = mid;
        if (findStartIndex == true) {
          end = mid - 1;
        } else {
          start = mid + 1;
        }
      }
    }
    return ans;
  }

}