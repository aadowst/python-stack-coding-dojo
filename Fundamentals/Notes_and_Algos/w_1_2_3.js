const str1 = "aaaabbcdddaa";
const expected1 = "a4b2c1d3a2";

const str2 = "";
const expected2 = "";

const str3 = "a";
const expected3 = "a";

const str4 = "bbcc";
const expected4 = "bbcc";

// ****************this is the solution in progress from group in Algos session**************
function encodeStr(str){
    if (str == ""){
        return str;
    }
    var count = 1,
    temp = [];
    temp = str.split('');
    var letter = temp[0];
        for (var i = 0; i < str.length; i++) {
            if (str[i] == letter && str[i+1] == letter) {
                count++;
            }else{
                console.log(letter, count);
                letter = temp[i+1];
                count = 1;
            }

    }

}

// ********************this is my solution (done after)*************************************
// console.log(encodeStr(str4))

function encodeStr(str) {
    if (str == ""){
        return str;
    }
    else{
    var letter = str[0];
    var count = 1;
    var encodeStr = "";
    for (let i = 1; i < str.length; i++){
            if (str[i] == letter){
                count++
            }else{
                encodeStr += letter + count;
                letter = str[i];
                count = 1;
            }
        }
        encodeStr += letter + count;

        if (encodeStr.length < str.length){

            return encodeStr;
        }else {
            return str;
        }

    }
}

// Another solution(?)
console.log(encodeStr3(str1));

function encodeStr3(str){
    if (str.legth < 2){
        return str;
    }else{
    let encodeStr ="";
    let i = 0;
    let count =1;
    let letter1 = str[i];
    let letter2 = str[i+1];
    while (i< str.length){
        letter1 = str[i];
        letter2 = str[i+1];
        if(letter1 == letter2){
            count++
        }else{
            encodeStr += letter1 + count;
            count = 1;
        }
        i++
    }
    if (encodeStr.length < str.length){
        return encodeStr;
    }else {
        return str;
    }

    }
}


// Algo 2. Do the reverse of the above

const two_str1 = "a3b2c1d3";
const two_expected1 = "aaabbcddd";

const two_str2 = "a3b2c12d10";
const two_expected2 = "aaabbccccccccccccdddddddddd";

// console.log(decodeStr(two_str2));


function decodeStr(str) {
    var letter = "";
    var repeat = "";  //repeat represents how many times a letter should be repeated in the decoded string
    var decodeStr = ""

// loop through the string 
    for (let i = 0; i < str.length; i++){
        repeat = "";

// if the value at index i is Not a Number (i.e. it IS a letter), store the value as letter 
        if (isNaN(str[i])){
            letter = str[i]

// otherwise, the value at index i is a Number, so do the else 
        }else{

// checks to make sure we are not at the end of the string (i.e. that str[i+1] exists), if we're not at the end, add the current index to the repeat
            if(str[i+1]){
                repeat += str[i];
// checks to see if the next digit(s) are also numbers. If once a letter is reached (i.e. Not a Number is true), break out of loop. Otherwise, continue adding digits to repeat
                for (let j = i+1; j< str.length; j++){
                    if (isNaN(str[j])){
                        break
                    }else{
                        repeat += str[j];

                    }
                }
// now that we have saved all digits in repeat, convert from a string to a Number. then add letter than many times to the string.
                repeat = Number(repeat);
                decodeStr += letter.repeat(repeat);

            }
        }
    }

    return decodeStr;
}

