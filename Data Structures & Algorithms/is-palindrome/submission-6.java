class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder newString = new StringBuilder();
        for (char chr: s.toCharArray()) {
            if (Character.isLetterOrDigit(chr)) {
                newString.append(Character.toLowerCase(chr));
            }
        }

        return newString.toString().equals(newString.reverse().toString());
    }
}
