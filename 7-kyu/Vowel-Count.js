// Return the number (count) of vowels in the given string.

// We will consider a, e, i, o, u as vowels for this Kata (but not y).

// The input string will only consist of lower case letters and/or spaces.

// My answer:
function getCount(str) {
    count = 0
    let onlyWordsArr = str.split(/ /g)
    console.log(onlyWordsArr)
    for (var i=0; i < onlyWordsArr.length; i++) {
        console.log(onlyWordsArr[i])
        for (var e=0; e < onlyWordsArr[i].length; e++) {
            console.log(onlyWordsArr[i][e])
            if (onlyWordsArr[i][e].match(/[aeiou]/)) {
                count += 1
            }
        }
    }
    return count;
  }

  
  console.log(getCount('yo quiero una cita'))