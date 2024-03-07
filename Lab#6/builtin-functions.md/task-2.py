str = "AsdFGHjkL"
up = sum(1 for ch in str if ch.isupper())
low = sum(1 for ch in str if ch.islower())
print(f"Up: {up}")
print(f"Low: {low}")