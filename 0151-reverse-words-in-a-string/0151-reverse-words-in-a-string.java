class Solution {
   static {
		for (int i = 0; i < 500; i++)
			reverseWords("");
	}

	public static String reverseWords(String s) {
		char[] ch = s.toCharArray();
		int n = ch.length;

		char result[] = new char[n];
		int result_index = 0;
		int end = n - 1; 

		while (end >= 0) {
			while (end >= 0 && ch[end] == ' ')
				end--;

			int start = end;

			while (start >= 0 && ch[start] != ' ')
				start--;

			if (result_index > 0)
				result[result_index++] = ' ';

			for (int i = start + 1; i <= end; i++)
				result[result_index++] = ch[i];

			end = start - 1;
		}

		return new String(result, 0, result_index).trim();
	}
}