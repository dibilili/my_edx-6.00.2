#============================
#Part 1: Greedy Cow Transport
#============================

#20/20 points (graded)
#One way of transporting cows is to always pick the heaviest cow that will fit onto the spaceship first. This is an example of a greedy algorithm. So if there are only 2 tons of free space on your spaceship, with one cow that's 3 tons and another that's 1 ton, the 1 ton cow will get put onto the spaceship.

#Implement a greedy algorithm for transporting the cows back across space in the function greedy_cow_transport. The function returns a list of lists, where each inner list represents a trip and contains the names of cows taken on that trip.

#Note: Make sure not to mutate the dictionary of cows that is passed in!

#Assumptions:

#The order of the list of trips does not matter. That is, [[1,2],[3,4]] and [[3,4],[1,2]] are considered equivalent lists of trips.
#All the cows are between 0 and 100 tons in weight.
#All the cows have unique names.
#If multiple cows weigh the same amount, break ties arbitrarily.
#The spaceship has a cargo weight limit (in tons), which is passed into the function as a parameter.
#Example:

#Suppose the spaceship has a weight limit of 10 tons and the set of cows to transport is {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}.

#The greedy algorithm will first pick Jesse as the heaviest cow for the first trip. There is still space for 4 tons on the trip. Since Maggie will not fit on this trip, the greedy algorithm picks Maybel, the heaviest cow that will still fit. Now there is only 1 ton of space left, and none of the cows can fit in that space, so the first trip is [Jesse, Maybel].

#For the second trip, the greedy algorithm first picks Maggie as the heaviest remaining cow, and then picks Callie as the last cow. Since they will both fit, this makes the second trip [[Maggie], [Callie]].

#The final result then is [["Jesse", "Maybel"], ["Maggie", "Callie"]].



    
def greedy_cow_transport(cows, limit):
    copyCow = cows.copy()
    sortedCow = sorted(copyCow.items(), key=lambda x:x[1], reverse=True)
    trip = []       
    while sum(copyCow.values())>0:
        total = 0
        ship = []
        
        for cow, value in sortedCow:
                                   
            if copyCow[cow] != 0 and value + total <= limit:
                ship.append(cow)
                total += value
                copyCow[cow] = 0                
        trip.append(ship)
    return trip
