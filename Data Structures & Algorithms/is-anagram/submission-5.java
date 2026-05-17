class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        Map<Character, Integer> dictionary = new HashMap<>();

        for (char chr: s.toCharArray()) {
            dictionary.put(chr, dictionary.getOrDefault(chr, 0) + 1);
        }

        for (char chr: t.toCharArray()) {
            if (dictionary.containsKey(chr)) {
                if (dictionary.get(chr) == 0) {
                    return false;
                }
                dictionary.put(chr, dictionary.get(chr) - 1);
            } else {
                return false;
            }
        }

        return true;
    }
}
