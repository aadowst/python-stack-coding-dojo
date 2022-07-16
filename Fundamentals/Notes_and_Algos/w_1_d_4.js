/* 
Zip Arrays into Map


Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.
Associative arrays are sometimes called maps because a key (string) maps to a value 
*/

const keys1 = ["abc", 3, "yo"];
const vals1 = [42, "wassup", true];
const expected1 = {
yo: true,   
abc: 42,
3: "wassup",
};

// const keys2 = [];
// const vals2 = [];
// const expected2 = {};

// const keys3 = ["abc", 3, "yo"];
// const vals3 = [42, "wassup", true, "something"];

// const expected3 = False

// const keys4 = ["abc", 3, "yo", "something"];
// const vals4 = [42, "wassup", true];
// const expected4 = {
// yo: true,   
// abc: 42,
// 3: "wassup",
// something: ""
// };

function createHash(keysList, valuesList){
    var expected = {};

    for (var i = 0; i < keysList.length; i++){

        expected[keysList[i]]=valuesList[i];
    }
    return expected
}

console.log(createHash(keys1, vals1))
// /**
//  * Converts the given arrays of keys and values into an object.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {Array<string>} keys
//  * @param {Array<any>} values
//  * @returns {Object} The object with the given keys and values.
//  */
// function zipArraysIntoMap(keys, values) {}