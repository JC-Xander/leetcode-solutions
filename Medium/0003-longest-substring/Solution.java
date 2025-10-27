import java.util.HashSet;
import java.uitl.set;

Class Solution {
    public int LengthOfLongestSubstring(String s) {
        set<Character> charSet = new HashSet<>();
        int left = 0, maxLength = 0;

        for (int right = 0; right < s.Length(); right++) {

            while (charSet.contains(s.charAt(right))) {
                charSet.remove(s.charAt(left));
                left++;
            }

            charSet.add(s.charAt(right));
            maxLength = Math.max(maxLength, right - left + 1);
        }
        return maxLength;
    }
}