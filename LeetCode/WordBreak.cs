public class Solution {
    public bool WordBreak(string s, IList<string> wordDict) {
        bool[] track = new bool[s.Length];
        for(int i = 0; i < s.Length; i++){
            foreach(string word in wordDict){
                if((i - word.Length + 1) >= 0 && s.Substring(i - word.Length + 1, word.Length) == word){
                    if(i - word.Length == -1 || track[i - word.Length] == true){
                        track[i] = true;
                        break;
                    }
                }
            }
        }
        return track[s.Length - 1];
    }
}