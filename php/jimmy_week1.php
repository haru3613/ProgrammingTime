<?php

function ValidParentheses(string $parens)
{
    $result = 0;
    for ($i = 0; $i < strlen($parens); $i++) {
        if ($parens[$i] === "(") {
            $result++;
        }
        if ($parens[$i] === ")") {
            $result--;
        }
        if ($result < 0) {
            return false;
        }
    }
    return $result === 0;
}

var_dump(ValidParentheses("(())"));
var_dump(ValidParentheses("((())"));
var_dump(ValidParentheses(")()"));
var_dump(ValidParentheses("())"));