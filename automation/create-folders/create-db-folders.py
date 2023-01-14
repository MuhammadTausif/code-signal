chapters = [
    "1. Welcome to the Table",
    "2. Always Leave Table in ORDER",
    "3. Would you LIKE the Second Meal",
    "4. GROUP Dishes BY Type",
    "5. Time for Tricks",
    "6. Specialties",
    "7. WHEN was it the CASE",
    "8. Regular Paradise",
    "9. Time River Revisited",
    "10. JOIN Us at the Table!",
    "11. Table Metamorphoses",
    "12. Selecting What to SELECT",
    "13. Express your CREATivity",
    "14. Exotic Dishes",
    "15. Between JOIN and SELECT",
    "16. A Table of Desserts"
]

exercises = [
    "1- projectList",
    "2- countriesSelection",
    "3- monthlyScholarships",
    "4- projectsTeam",
    "5- automaticNotifications",
    "6- volleyballResults",
    "7- mostExpensive",
    "8- contestLeaderboard",
    "9- gradeDistribution",
    "10- mischievousNephews",
    "11- suspectsInvestigation",
    "12- suspectsInvestigation2",
    "13- securityBreach",
    "14- testCheck",
    "15- expressionsVerification",
    "16- newsSubscribers",
    "17- countriesInfo",
    "18- itemCounts",
    "19- usersByContinent",
    "20- movieDirectors",
    "21- travelDiary",
    "22- soccerPlayers",
    "23- marketReport",
    "24- websiteHacking",
    "25- nullIntern",
    "26- legsCount",
    "27- combinationLock",
    "28- interestClub",
    "29- personalHobbies",
    "30- booksCatalogs",
    "31- habitatArea",
    "32- orderOfSuccession",
    "33- orderingEmails",
    "34- placesOfInterest",
    "35- soccerGameSeries",
    "36- correctIPs",
    "37- validPhoneNumbers",
    "38- importantEvents",
    "39- dateFormatting",
    "40- pastEvents",
    "41- netIncome",
    "42- alarmClocks",
    "43- companyEmployees",
    "44- scholarshipsDistribution",
    "45- userCountries",
    "46- placesOfInterestPairs",
    "47- localCalendar",
    "48- routeLength",
    "49- currencyCodes",
    "50- coursesDistribution",
    "51- nicknames",
    "52- tableSecurity",
    "53- officeBranches",
    "54- restaurantInfo",
    "55- studentsInClubs",
    "56- emptyDepartments",
    "57- sunnyHolidays",
    "58- closestCells",
    "59- top5AverageGrade",
    "60- salaryDifference",
    "61- recentHires",
    "62- checkExpenditure",
    "63- dancingCompetition",
    "64- trackingSystem",
    "65- storageOptimization",
    "66- consecutiveIds",
    "67- holidayEvent",
    "68- hostnamesOrdering"
]

import os
from pathlib import Path
dirc_path = Path(r"C:\Users\Public\Dev\practice\python-exercises\code-signal\automation\create-folders")

for chap in chapters:
    os.mkdir(dirc_path / chap)
    # print(chap)
    # pass

for exercise in exercises:
    # open(exercise + ".py", "x")
    pass


