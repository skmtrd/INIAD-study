const reverse = (s) => {
  let result = "";
  for (let i = 0; i < s.length; i++) {
    result = s[i] + result;
  }
  return result;
};

const go = () => {
  console.log("ok");
  reverse();
};
