class Solution {
    public boolean hasDuplicate(int[] nums) {
        // hash set?
        Set<Integer> isNumSeen = new HashSet<>();

        for (int num : nums) {
            if (isNumSeen.contains(num)) {
                return true;
            }
            isNumSeen.add(num);
        }
        return false;
    }
}