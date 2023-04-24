// Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

// Examples input/output:

// XO("ooxx") => true
// XO("xooxx") => false
// XO("ooxXm") => true
// XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
// XO("zzoo") => false

// My answer:
function XO(str) {
    x = 0
    o = 0
    lowStr = str.toLowerCase()
    for (let i = 0; i < lowStr.length; i++) {
        if (lowStr[i] === 'o') {
            o += 1
        } else if (lowStr[i] === 'x') {
            x += 1
        }
    }
    if (o == x) {
        return true
    } else {
        return false
    }
}
console.log(XO("ooxx"))
console.log(XO("xooxx"))
console.log(XO("ooxXm"))
console.log(XO("zpzpzpp"))
console.log(XO("zzoo"))