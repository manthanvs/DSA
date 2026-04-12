class Solution {
    public String mergeAlternately(String word1, String word2) {
        char w1[] = word1.toCharArray();
        char w2[] = word2.toCharArray();
        int len1 = w1.length;
        int len2 = w2.length;
        char answer[] = new char[len1 + len2];
        int index = 0;
        int idx = 0;
        for (int i = 0; i < answer.length; i++) {
            if (i % 2 == 0) {
                if (index < len1) {
                    answer[i] = w1[index++];
                } else {
                    answer[i] = w2[idx++];
                }
            } else {
                if (idx < len2) {
                    answer[i] = w2[idx++];
                } else {
                    answer[i] = w1[index++];
                }
            }
        }
        return new String(answer);
    }
}
