class Solution {
    public boolean isValid(String s) {
        if (s.length() < 2) {
            return false;
        }

        HashMap<Character, Character> map = new HashMap<>();
        map.put('}', '{');
        map.put(')', '(');
        map.put(']', '[');

        ArrayList<Character> arr = new ArrayList<Character>();

        for (char chr: s.toCharArray()) {
            if (chr == '(' || chr == '[' || chr == '{') {
                arr.add(chr);
            } else {
                Character match = map.get(chr);
                if (arr.isEmpty()) {
                    return false;
                }
                if (!arr.isEmpty() && match != arr.remove(arr.size() - 1)) {
                    return false;
                }
            }
        }

        return arr.size() == 0;
    }
}
