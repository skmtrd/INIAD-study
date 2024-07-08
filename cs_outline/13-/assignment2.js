const abbrev = (text) => {
  const vowels = ["a", "i", "o", "u", "e"];
  return text
    .split("")
    .filter((char) => !vowels.includes(char))
    .join("");
};

console.log(abbrev("sakamotosouya")); // "skmtsy"

const max_len = (xs) => {
  return Math.max(...xs.map((x) => x.length));
};

console.log(max_len(["a", "ab", "sdadsdabc"])); // 3
