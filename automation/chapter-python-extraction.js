var chap_db = document.getElementsByClassName("block arcade-map--topic-title -bg-white -layout-h -align-center -padding-8")

chap_db_name = []
for (let i = 0; i < chap_db.length; i++) {
    console.log(chap_db[i].firstChild.innerText)
    chap_db_name.push(chap_db[i].firstChild.innerText)
}

var ex_db = document.getElementsByClassName("-layout-h -center -padding-4 -space-h-16")
ex_db_name = []
for (let i = 0; i < ex_db.length; i++) {
    console.log(ex_db[i].children[0].innerText)
   console.log(ex_db[i].children[1].innerText)
    ex_db_name.push(ex_db[i].children[0].innerText + "- " + ex_db[i].children[1].innerText )
}
chap_db_names = [
    "Meet Python",
    "Slithering in Strings",
    "Lurking in Lists",
    "Lambda Illusions",
    "Complexity of Comprehension",
    "Fumbling in Functional",
    "Caravan of Collections",
    "Itertools Kit",
    "Drilling the Lists",
    "Yin and Yang of Yields",
    "Higher Order Thinking",
    "Showing Class",
    "Picturing the Parsibilities"
]

chap_db_indexed_names = [
    "1. Meet Python",
    "2. Slithering in Strings",
    "3. Lurking in Lists",
    "4. Lambda Illusions",
    "5. Complexity of Comprehension",
    "6. Fumbling in Functional",
    "7. Caravan of Collections",
    "8. Itertools Kit",
    "9. Drilling the Lists",
    "10. Yin and Yang of Yields",
    "11. Higher Order Thinking",
    "12. Showing Class",
    "13. Picturing the Parsibilities"
]

ex_db_name = [
    "Collections Truthness",
    "Efficient Comparison",
    "Special Conditional",
    "Language Differences",
    "Count Bits",
    "Modulus",
    "Simple Sort",
    "Base Conversion",
    "Mex Function",
    "List Beautifier",
    "String Definition",
    "Fix Message",
    "Cat Walk",
    "Convert Tabs",
    "Feedback Review",
    "Is Word Palindrome",
    "Permutation Cipher",
    "Competitive Eating",
    "New Style Formatting",
    "Get Commit",
    "List Multiplication",
    "Lists Concatenation",
    "Two Teams",
    "Remove Tasks",
    "Print List",
    "Repeat Char",
    "Get Points",
    "Sort Students",
    "Is Test Solvable",
    "Create Spiral Matrix",
    "Construct Shell",
    "Word Power",
    "Cool Pairs",
    "Multiplication Table",
    "Chess Teams",
    "Fix Result",
    "College Courses",
    "Create Histogram",
    "Least Common Denominator",
    "Dictionary Keys",
    "Unique Characters",
    "Correct Scholarships",
    "Startup Name",
    "Words Recognition",
    "Transpose Dictionary",
    "Doodled Password",
    "Frequency Analysis",
    "Cyclic Name",
    "Memory Pills",
    "Float Range",
    "Rock Paper Scissors",
    "Kth Permutation",
    "Crazyball",
    "Cracking Password",
    "Twins Score",
    "Pressure Gauges",
    "Correct Lineup",
    "Group Dating",
    "Fix Tree",
    "Pref Sum",
    "Math Practice",
    "Check Participants",
    "Fibonacci List",
    "Primes Sum",
    "Calc Bonuses",
    "Calc Final Score",
    "Fibonacci Generator",
    "Calkin Wilf Sequence",
    "Check Password",
    "Greetings Generator",
    "Range Float",
    "Super Prize",
    "Try Functions",
    "Two Lines",
    "Simple Composition",
    "Functions Composition",
    "Merging Vines",
    "Count Visitors",
    "Sign",
    "Primary School",
    "User Attribute",
    "Sort Codesginal Users",
    "Is Cool Team",
    "Create Die",
    "To Human Age",
    "Xml Tags",
    "Build Command",
    "Website Calendar",
    "Malicious Program",
    "Url Similarity",
    "Page Complexity",
    "Weird Encoding"
]

ex_db_name_indexed = [
    "1- Collections Truthness",
    "2- Efficient Comparison",
    "3- Special Conditional",
    "4- Language Differences",
    "5- Count Bits",
    "6- Modulus",
    "7- Simple Sort",
    "8- Base Conversion",
    "9- Mex Function",
    "10- List Beautifier",
    "11- String Definition",
    "12- Fix Message",
    "13- Cat Walk",
    "14- Convert Tabs",
    "15- Feedback Review",
    "16- Is Word Palindrome",
    "17- Permutation Cipher",
    "18- Competitive Eating",
    "19- New Style Formatting",
    "20- Get Commit",
    "21- List Multiplication",
    "22- Lists Concatenation",
    "23- Two Teams",
    "24- Remove Tasks",
    "25- Print List",
    "26- Repeat Char",
    "27- Get Points",
    "28- Sort Students",
    "29- Is Test Solvable",
    "30- Create Spiral Matrix",
    "31- Construct Shell",
    "32- Word Power",
    "33- Cool Pairs",
    "34- Multiplication Table",
    "35- Chess Teams",
    "36- Fix Result",
    "37- College Courses",
    "38- Create Histogram",
    "39- Least Common Denominator",
    "40- Dictionary Keys",
    "41- Unique Characters",
    "42- Correct Scholarships",
    "43- Startup Name",
    "44- Words Recognition",
    "45- Transpose Dictionary",
    "46- Doodled Password",
    "47- Frequency Analysis",
    "48- Cyclic Name",
    "49- Memory Pills",
    "50- Float Range",
    "51- Rock Paper Scissors",
    "52- Kth Permutation",
    "53- Crazyball",
    "54- Cracking Password",
    "55- Twins Score",
    "56- Pressure Gauges",
    "57- Correct Lineup",
    "58- Group Dating",
    "59- Fix Tree",
    "60- Pref Sum",
    "61- Math Practice",
    "62- Check Participants",
    "63- Fibonacci List",
    "64- Primes Sum",
    "65- Calc Bonuses",
    "66- Calc Final Score",
    "67- Fibonacci Generator",
    "68- Calkin Wilf Sequence",
    "69- Check Password",
    "70- Greetings Generator",
    "71- Range Float",
    "72- Super Prize",
    "73- Try Functions",
    "74- Two Lines",
    "75- Simple Composition",
    "76- Functions Composition",
    "77- Merging Vines",
    "78- Count Visitors",
    "79- Sign",
    "80- Primary School",
    "81- User Attribute",
    "82- Sort Codesginal Users",
    "83- Is Cool Team",
    "84- Create Die",
    "85- To Human Age",
    "86- Xml Tags",
    "87- Build Command",
    "88- Website Calendar",
    "89- Malicious Program",
    "90- Url Similarity",
    "91- Page Complexity",
    "92- Weird Encoding"
]