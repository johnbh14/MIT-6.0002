###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cow_data = open(filename, 'r')
    cow_dict = {}
    for line in cow_data:
        line_list = line.split(',')
        cow_dict[line_list[0]] = int(line_list[1].split('\\')[0])
    return cow_dict

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows = cows.copy()
    final_result = []
    while len(cows) != 0:
        trip_weight = 0
        trip = []
        while trip_weight <= limit:
            remaining_weight = limit - trip_weight
            v=list(cows.values())
            k=list(cows.keys())
            try:
                biggest_possible_cow = k[v.index(max([i for i in v if i <= remaining_weight]))]
            except:
                break
            trip.append(biggest_possible_cow)
            trip_weight += cows[biggest_possible_cow]
            cows.pop(biggest_possible_cow)
        final_result.append(trip)
    return final_result
            

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows = cows.copy()
    result_candidates = []
    for partition in get_partitions(cows.keys()):
        #print('Starting Partition Loop' + str(partition))
        try:
            for trip in partition:
                #print('Starting Trip Loop' + str(trip))
                trip_total = 0
                for cow in trip:
                    trip_total += cows[cow]
                #print('Trip Total = ' + str(trip_total))
                if trip_total > limit:
                    raise ValueError('An individual trip total exceeded the limit.')
        except ValueError:
            continue
        #print('Appending Partition: ' + str(partition))
        result_candidates.append(partition)
    trip_counts = []
    for candidate in result_candidates:
        trip_counts.append(len(candidate))
    return result_candidates[trip_counts.index(min(trip_counts))]
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows('ps1_cow_data.txt')
    
    print('Running Greedy Algorithm')
    start = time.time()
    print(greedy_cow_transport(cows))
    end = time.time()
    print('The Greedy Algo Took ' + str(end - start) + ' Seconds')
    
    print('Running Brute Force Algorithm')
    start = time.time()
    print(brute_force_cow_transport(cows))
    end = time.time()
    print('The Brute Force Algo Took ' + str(end - start) + ' Seconds')
