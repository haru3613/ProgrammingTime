<?php

/*
()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
 */
$cls = new test();
$cls->pairBrackets('()');
$cls->pairBrackets(')(()))');
$cls->pairBrackets('(');
$cls->pairBrackets('(())((()())())');

class test
{
    /**
     * @var 搜尋字串
     */
    private $search = '()';

    public function pairBrackets(string $string)
    {

        $result = $this->recursive($string);
        if($result){
            echo "$string == true<br>\n";
        }else{
            echo "$string == false<br>\n";
        }
    }

    /**
     * 遞迴取代字串
     *
     * @param string $string 搜尋字串
     * @return bool 結果
     */
    private function recursive(string $string)
    {
        if(strpos($string,$this->search) !== false){
            $tmp = join("",explode($this->search, $string));
            return $this->recursive($tmp);
        }else if($string=="") {
            return true;
        }else{
            return false;
        }
    }
}
