india = "vishwaguru" 

# [START : STOP : STEP]
# Logic: Start at index 2, go up to (but not including) index 8.
# The 'Step' of 3 means: Pick a character, then jump 3 positions to the next one.
print(india[2:8:3]) 

# REPLACED COMMENT:
# 1. Start at index 2 -> Picks "s"
# 2. Jump 3 steps (2 + 3) = index 5 -> Picks "a"
# 3. Jump 3 steps (5 + 3) = index 8 -> STOP! (Index 8 is excluded)
# Final Result: "sa"