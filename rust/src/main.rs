use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut result: HashMap<[i32; 26], Vec<String>> = HashMap::new();
        let start_ascii = 'a' as usize;

        for word in strs {
            let mut map = [0; 26];

            for letter in word.chars() {
                let position = (letter as usize) - start_ascii;
                map[position] += 1
            }

            result.entry(map).or_insert(Vec::new()).push(word)
        }

        return result.into_values().collect();
    }
}

fn main() {
    let input = vec![
        "eat".to_string(),
        "tea".to_string(),
        "tan".to_string(),
        "ate".to_string(),
        "nat".to_string(),
        "bat".to_string(),
    ];

    let grouped_anagrams = Solution::group_anagrams(input);
    println!("{:?}", grouped_anagrams);
}
