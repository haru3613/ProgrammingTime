function validParentheses(str){
  //TODO 
  let notPaired = 0;
  const firstOpen = str.search(/(\()/), 
        firstClose = str.search(/(\))/);
  if (str.length > 100) return false;
  if (firstOpen > firstClose) return false;
  
  for (let char = 0; char < str.length; char++ ) {
      if (str[char] ==='(') notPaired++;
      if (str[char] ===')') notPaired--;
      if (notPaired === -1) {
      	return false
      }
  }
  return notPaired === 0 ? true : false;
}