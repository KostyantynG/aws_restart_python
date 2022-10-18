press_release = """

Doody Calls, a nationwide leader in dog poop removal services, is growing its footprint in the pooper scooper industry with the opening of an office in Orlando, Florida. Doody Calls currently cleans up dog poop in over 57 territories across 23 states and has been named the number-one dog poop removal franchise in the United States by Entrepreneur Magazine's annual Franchise 500 list.

"""

# Remove the leading and trailing whitespace (new lines) from press_release

version_1 = press_release.strip()

# Replace the phrase "dog poop" with "pet waste" in the press release.  Our research shows "pet waste" tests better than "dog poop"

version_2 = version_1.replace("dog poop","pet waste")

# We changed our company name! replace the phrase "Doody Calls" with "DoodyCalls" (no space between the words)

version_3 = version_2.replace("Doody Calls","DoodyCalls")

# Our research shows that it's best to shout our press releases. Make the entire press release uppercased!

version_final = version_3.upper()

# Print out the updated press release with all of the above changes:

print(version_final)