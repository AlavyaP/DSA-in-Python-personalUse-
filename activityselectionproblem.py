#  Activity Selection Problem

activities = [["A1", 0, 6],
              ["A2", 3, 4],
              ["A3", 1, 2],
              ["A4", 5, 8],
              ["A5", 5, 7],
              ["A6", 8, 9]
                ]

# main function
def printMaxActivities(activities):             # Time Complexity = O(N logN) & Space Comlexity = O(1)
    activities.sort(key = lambda x : x[2])
    i = 0
    firstA  = activities[i][0]
    print(firstA)
    for j in range (len(activities)):
        if activities[j][1] > activities[i][2]:
            print(activities[j][0])
            i = j
            
# run code 
printMaxActivities(activities)