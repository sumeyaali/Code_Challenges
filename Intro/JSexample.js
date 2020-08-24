function compareTwoArrays(arr1, arr2) {
    // compare the two arrays and if they have the same numbers return true otherwise
    for(let i = 0; i > arr1.length; i++){
        for (let j = 0; j > arr2.length; j++){
            if (length(arr1) != length(arr2)){
                return false
            }
            else if (arr1[i] === arr2[i]) {
                return true
            }
        }
    }
}

// Test cases to verify
console.log(compareTwoArrays([1,2,3], [1,2,3])); // true
console.log(compareTwoArrays([3,3,3], [1,2,3])); // false
console.log(compareTwoArrays([1,2,3,4], [1,2,3])); // false
console.log(compareTwoArrays([1,2,3], [1,2,3,4])); // false

// If you decide to attempt nested arrays
const a = [1,['a', 'b'],3,4];
const b = [1,['a', 'b'],3,4];
console.log(compareTwoArrays(a, b)); // true

const a = [1,[‘z', ‘z'],3,4];
const b = [1,['a', 'b'],3,4];
console.log(compareTwoArrays(a, b)); // false