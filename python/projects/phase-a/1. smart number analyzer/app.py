from reporter import process

print("\nSMART NUMBER ANALYZER")

n = int(input("\nEnter a number: "))

process.display(n)

# Here’s a precise, no-fluff summary of what you need to improve for Project A1:

# Core Fixes (must do)
# Handle edge cases properly
# 0, 1 → not prime
# Negative numbers → define behavior (especially Armstrong, factors)
# Prevent incorrect outputs for these cases
# Add input validation
# Prevent crashes on invalid input (abc, empty input, etc.)
# Logic Improvements
# Optimize performance
# Prime check → loop till √n
# Factors → loop till √n and build pairs
# Ensure clean outputs from functions
# Functions must only return, never print
# Design Improvements
# Separate concerns clearly
# analyze(n) → returns data
# format_output(data) → handles printing
# Improve report structure
# Make output readable and structured
# Show clear Yes/No instead of True/False
# Present factors cleanly
# Quality Upgrades (Version 3)
# Add one meaningful feature (choose one)
# Batch input (analyze multiple numbers)
# Performance-optimized implementation
# Extra property (e.g., perfect number)
# Mindset Fix (most important)
# Define behavior explicitly
# Don’t leave ambiguous cases
# Decide and handle them intentionally
# Bottom Line

# To reach a strong submission:

# Fix correctness (edge cases)
# Improve efficiency (√n logic)
# Clean architecture (logic vs output)
# Add one meaningful upgrade