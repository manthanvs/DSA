class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        // Frequency array to store count of numbers
        // Size = 20001 to handle numbers from -10000 to 10000
        int[] freqs = new int[20001];

        // Spacer is used to shift negative numbers into valid index range
        // Example: -10000 becomes index 0
        int spacer = 10000;

        // Count frequency of each number
        // num + spacer ensures index is non-negative
        for (int num : nums) {
            freqs[num + spacer]++;
        }

        // Max Heap based on frequency
        // Higher frequency elements come first
        PriorityQueue<Integer> pq = 
            new PriorityQueue<>((a, b) -> freqs[b] - freqs[a]);

        // Add indices (numbers) that actually appeared
        for (int i = 0; i < freqs.length; i++) {
            if (freqs[i] != 0) {
                pq.add(i);
            }
        }

        // Extract top k frequent elements
        int[] res = new int[k];
        for (int i = 0; i < k; i++) {
            // Subtract spacer to get original number
            res[i] = pq.poll() - spacer;
        }

        return res;
    }
}