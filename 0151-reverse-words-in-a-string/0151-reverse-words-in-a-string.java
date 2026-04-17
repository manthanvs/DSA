class Solution {
    public String reverseWords(String s) {
        char[] arr = s.toCharArray();
        int n = arr.length;

        // Step 1: reverse whole array
        reverse(arr, 0, n - 1);

        // Step 2: reverse each word
        int i = 0;
        int j = 0;

        while (i < n) {
            // skip spaces
            while (i < n && arr[i] == ' ') i++;

            if (i >= n) break;

            j = i;
            while (j < n && arr[j] != ' ') j++;

            // reverse word
            reverse(arr, i, j - 1);

            i = j;
        }

        // Step 3: clean spaces
        return cleanSpaces(arr);
    }

    private void reverse(char[] arr, int l, int r) {
        while (l < r) {
            char temp = arr[l];
            arr[l] = arr[r];
            arr[r] = temp;
            l++;
            r--;
        }
    }

    private String cleanSpaces(char[] arr) {
        int n = arr.length;
        int i = 0, j = 0;

        while (j < n) {
            // skip spaces
            while (j < n && arr[j] == ' ') j++;

            // copy word
            while (j < n && arr[j] != ' ') {
                arr[i++] = arr[j++];
            }

            // skip spaces
            while (j < n && arr[j] == ' ') j++;

            // add single space
            if (j < n) arr[i++] = ' ';
        }

        return new String(arr, 0, i);
    }
}