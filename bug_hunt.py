count = 1
total = 0

# BUG: The while condition was missing a colon. Added : to start the loop block.
while count <= 5:
    # BUG: The original loop stopped before adding 5. Changed < 5 to <= 5.
    total = total + count
    count = count + 1

# BUG: total is an integer, so it cannot be joined directly to a string. Converted total using str().
print("Sum of 1 to 5 is: " + str(total))