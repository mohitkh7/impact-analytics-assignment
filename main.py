import sys
from solution import Solution

if __name__ == "__main__":
    try:
        days = int(sys.argv[1])
        print("Number of days is {}".format(days))
    except IndexError:
        print("Please pass 'days' argument in command line")
    except ValueError:
        print("'Days' argument must be of integer type")
    except Exception as e:
        print(e)
    else:
        solution = Solution(days)
        print("Number of ways to attend classes over {} days is {}".format(days, solution.number_of_ways_to_attend_classes()))
        print("probability to miss graduation ceremony is {}".format(solution.probability_to_miss_gradution_ceremony()))