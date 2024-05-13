// Given a number n, draw stairs using the letter "I", n tall and n wide, with the tallest in the top left.

// For example n = 3 result in:

// "I\n I\n  I"
// or printed:

// I
//  I
//   I
// Another example, a 7-step stairs should be drawn like this:

// I
//  I
//   I
//    I
//     I
//      I
//       I
// My solution:
    function drawStairs(x) {
        if (x == 1) {
            stairs = "I";
        } else {
            stairs = ""
            for (var i = 1; i < x; i++){
                stairs += "I\n";
                stairs += " ".repeat(i);
            }
            stairs += "I"
        }    
        return stairs
    }

console.log(drawStairs(3));