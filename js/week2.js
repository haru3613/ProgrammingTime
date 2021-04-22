function calRoman (s) {
    const romanMap = new Map([
      ['I', 1],
      ['V', 5],
      ['X', 10],
      ['L', 50],
      ['C', 100],
      ['D', 500],
      ['M', 1000]
    ]);
    if (s.length > 15 || s < 1) return false;
    s.split('').forEach(s => {
        if (!romanMap.get(s)) return false
    })
    
    const reverseRomanArr = s.split('').reverse();
    const sumArr = [];
    
    let reduceCount = 1;
    let reduceBase = romanMap.get(reverseRomanArr[0]);
    let nextReduce = romanMap.get(reverseRomanArr[reduceCount]);
    let sum = 0;
    function reduce () {
      if (reduceBase - nextReduce > 0) {
        reduceCount++;
        reduceBase = reduceBase - nextReduce;
        nextReduce = romanMap.get(reverseRomanArr[reduceCount]);
        if (nextReduce === undefined) {
          sumArr.push(reduceBase);
          return ''
        }
        reduce();
      }
      else {
        sumArr.push(reduceBase);
        reverseRomanArr.splice(0, reduceCount);
        reduceCount = 1;
        reduceBase = romanMap.get(reverseRomanArr[0]);
        nextReduce = romanMap.get(reverseRomanArr[reduceCount]);
        if (reverseRomanArr.length === 0) return ''
        if (reverseRomanArr.length === 1) {
          sumArr.push(reduceBase);
          return ''
        }
        reduce()
      }
    }
    reduce();
    sumArr.forEach(num => {
      sum = sum + num;
    });
      
    if (sum >= 1 && sum <= 3999) {
      return sum;
    } else {
      return false
    }
  }
  return calRoman(s);
  
// console.log(calRoman("I"));  
// console.log(calRoman("II"));
// console.log(calRoman("LVIII"));
// console.log(calRoman("IX"));
// console.log(calRoman("MCMXCIV"));
// console.log(calRoman("CM"));