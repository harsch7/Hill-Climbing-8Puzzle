"""
Author: Harsh Vardhan Singh
Hill Climbing 8-Puzzle Program
Init State
0 1 3
4 2 5
7 8 6
"""
import csv
import random

class HillClimbing8Puzzle:
    # Goal States
    goalStateOne = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    goalStateTwo = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    # calculates G(n) value for a number in a state
    def calG(self, state, n):

        nCount = 0
        for i in range(state.index(n) + 1, len(state)):
            if state[i] != 0 and state[i] < n:
                nCount += 1

        return nCount

    # calculates the h value of a state
    def calPerformanceH(self, state):

        hSum = 0
        for i in range(len(state)):
            hSum += self.calG(state, i)

        return hSum

    def createNeighbors(self, state):

        neighborsList = []

        emptyBlock = state.index(0)

        # move block up and swap with 0
        if emptyBlock <= 5:
            upIndex = state.index(0) + 3
            newState = state.copy()
            newState[emptyBlock], newState[upIndex] = (newState[upIndex],
                                                       newState[emptyBlock])
            neighborsList.append(newState)

        # move block left and swap with 0
        if not emptyBlock in [2, 5, 8]:
            leftIndex = state.index(0) + 1
            newState = state.copy()
            newState[emptyBlock], newState[leftIndex] = (newState[leftIndex],
                                                         newState[emptyBlock])
            neighborsList.append(newState)

        # move block right and swap with 0
        if not emptyBlock in [0, 3, 6]:
            rightIndex = state.index(0) - 1
            newState = state.copy()
            newState[emptyBlock], newState[rightIndex] = (newState[rightIndex],
                                                          newState[emptyBlock])
            neighborsList.append(newState)

        # move block down and swap with 0
        if emptyBlock >= 3:
            downIndex = state.index(0) - 3
            newState = state.copy()
            newState[emptyBlock], newState[downIndex] = (newState[downIndex],
                                                         newState[emptyBlock])
            neighborsList.append(newState)

        return neighborsList

    # Implementation of Hill Climbing Algorithm
    def hillClimbing(self, initState):

        currentState = initState

        # Create csv file and write lowestH

        with open("../h_output.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(["h-value"])

        while True:

            neighbors = self.createNeighbors(currentState)

            neighborH = [self.calPerformanceH(neighbor)
                         for neighbor in neighbors]

            neighborState = [neighbor
                             for neighbor in neighbors]
            lowestH = min(neighborH)


            with open("../h_output.csv", "a") as f:
                writer = csv.writer(f)
                writer.writerow([lowestH])

            if lowestH > self.calPerformanceH(currentState):
                break

            currentState = neighborState[neighborH.index(lowestH)]
            print("New State: ", currentState)

            if (currentState == self.goalStateOne or currentState ==
                    self.goalStateTwo):
                return currentState

        return None


puzzle = HillClimbing8Puzzle()

initState = [0, 1, 3, 4, 2, 5, 7, 8, 6]
solution = puzzle.hillClimbing(initState)
print("Solution State:", solution)

"""
def randomState():
    state = list(range(9))
    random.shuffle(state)
    return state

success = 0
for _ in range(1000):
    randInitState = randomState()
    print("New Initial State:", randInitState)
    newSolution = puzzle.hillClimbing(randInitState)
    print("New Solution State:", newSolution)
    if newSolution is not None:
        success += 1

print("Success Ration: ", success / 1000)
"""