import os
from pathlib import Path
dirc_path = Path(r"C:\Users\Public\Dev\practice\python-exercises\code-signal\automation\create-folders")
# os.mkdir(r"C:\Users\Public\Dev\practice\python-exercises\code-signal\automation\1")

chap_indexed_name = [
    "1. Intro Gates",
    "2. At the Crossroads",
    "3. Corner of 0s and 1s",
    "4. Loop Tunnel",
    "5. List Forest Edge",
    "6. Labyrinth of Nested Loops",
    "7. Book Market",
    "8. Mirror Lake",
    "9. Well of Integration",
    "10. Lab of Transformations",
    "11. Spring of Integration",
    "12. List Backwoods",
    "13. Waterfall of Integration",
    "14. Sorting Outpost",
    "15. Chess Tavern",
    "16. Time River",
    "17. Regular Hell",
    "18. Secret Archives",
    "19. Cliffs of Pain"
]

exercises_list = [
    "1- Add Two Digits",
    "2- Largest Number",
    "3- Candies",
    "4- Seats in Theater",
    "5- Max Multiple",
    "6- Circle of Numbers",
    "7- Late Ride",
    "8- Phone Call",
    "9- Reach Next Level",
    "10- Knapsack Light",
    "11- Extra Number",
    "12- Is Infinite Process",
    "13- Arithmetic Expression",
    "14- Tennis Set",
    "15- Will You",
    "16- Metro Card",
    "17- Kill K-th Bit",
    "18- Array Packing",
    "19- Range Bit Count",
    "20- Mirror Bits",
    "21- Second-Rightmost Zero Bit",
    "22- Swap Adjacent Bits",
    "23- Different Rightmost Bit",
    "24- Equal Pair of Bits",
    "25- Least Factorial",
    "26- Count Sum of Two Representations 2",
    "27- Magical Well",
    "28- Lineup",
    "29- Addition Without Carrying",
    "30- Apple Boxes",
    "31- Increase Number Roundness",
    "32- Rounders",
    "33- Candles",
    "34- Count Black Cells",
    "35- Create Array",
    "36- Array Replace",
    "37- First Reverse Try",
    "38- Concatenate Arrays",
    "39- Remove Array Part",
    "40- Is Smooth",
    "41- Replace Middle",
    "42- Make Array Consecutive 2",
    "43- Is Power",
    "44- Is Sum of Consecutive 2",
    "45- Square Digits Sequence",
    "46- Pages Numbering With Ink",
    "47- Comfortable Numbers",
    "48- Weak Numbers",
    "49- Rectangle Rotation",
    "50- Crossword Formation",
    "51- Enclose In Brackets",
    "52- Proper Noun Correction",
    "53- Is Tandem Repeat",
    "54- Is Case-Insensitive Palindrome",
    "55- Find Email Domain",
    "56- HTML End Tag By Start Tag",
    "57- Is MAC48 Address",
    "58- Is Unstable Pair",
    "59- Strings Construction",
    "60- Is Substitution Cipher",
    "61- Create Anagram",
    "62- Construct Square",
    "63- Numbers Grouping",
    "64- Different Squares",
    "65- Most Frequent Digit Sum",
    "66- Number of Clans",
    "67- House Numbers Sum",
    "68- All Longest Strings",
    "69- House of Cats",
    "70- Alphabet Subsequence",
    "71- Minimal Number of Coins",
    "72- Add Border",
    "73- Switch Lights",
    "74- Timed Reading",
    "75- Elections Winners",
    "76- Integer to String of Fixed Width",
    "77- Are Similar",
    "78- Ada Number",
    "79- Three Split",
    "80- Character Parity",
    "81- Reflect String",
    "82- New Numeral System",
    "83- Cipher 26",
    "84- Stolen Lunch",
    "85- Higher Version",
    "86- Decipher",
    "87- Alphanumeric Less",
    "88- Array Conversion",
    "89- Array Previous Less",
    "90- Pair of Shoes",
    "91- Combs",
    "92- Strings Crossover",
    "93- Cyclic String",
    "94- Beautiful Text",
    "95- Runners Meetings",
    "96- Christmas Tree",
    "97- File Naming",
    "98- Extract Matrix Column",
    "99- Are Isomorphic",
    "100- Reverse On Diagonals",
    "101- Swap Diagonals",
    "102- Crossing Sum",
    "103- Draw Rectangle",
    "104- Volleyball Positions",
    "105- Star Rotation",
    "106- Sudoku",
    "107- Minesweeper",
    "108- Box Blur",
    "109- Contours Shifting",
    "110- Polygon Perimeter",
    "111- Gravitation",
    "112- Is Information Consistent",
    "113- Correct Nonogram",
    "114- Shuffled Array",
    "115- Sort by Height",
    "116- Sort By Length",
    "117- Boxes Packing",
    "118- Maximum Sum",
    "119- Rows Rearranging",
    "120- Digit Difference Sort",
    "121- Unique Digit Products",
    "122- Bishop and Pawn",
    "123- Chess Knight Moves",
    "124- Bishop Diagonal",
    "125- Whose Turn",
    "126- Chess Bishop Dream",
    "127- Chess Triangle",
    "128- Amazon Checkmate",
    "129- Pawn Race",
    "130- Valid Time",
    "131- Video Part",
    "132- Day of Week",
    "133- Curious Clock",
    "134- New Year Celebrations",
    "135- Regular Months",
    "136- Missed Classes",
    "137- Holiday",
    "138- Is Sentence Correct",
    "139- Replace All Digits RegExp",
    "140- Swap Adjacent Words",
    "141- N-th Number",
    "142- Is Subsequence",
    "143- Eye Rhyme",
    "144- Program Translation",
    "145- Repetition Encryption",
    "146- Bugs and Bugfixes",
    "147- LRC to SubRip",
    "148- HTML Table",
    "149- Chess Notation",
    "150- Cells Joining",
    "151- First Operation Character",
    "152- Count Elements",
    "153- Tree Bottom",
    "154- Befunge-93",
    "155- Pipes Game",
    "156- Game 2048",
    "157- Snake Game",
    "158- Tetris Game",
    "159- Pyraminx Puzzle",
    "160- Lines Game",
    "161- Fractal",
    "162- Time ASCII Representation"
]

for chap in chap_indexed_name:
    # os.mkdir(dirc_path / chap)
    # print(chap)
    pass

# open("test.py", "x")
for exercise in exercises_list:
    open(exercise + ".py", "x")
    # open(no.strsip() + "- " + name.strip() + ".py", "x")
    print(exercise)