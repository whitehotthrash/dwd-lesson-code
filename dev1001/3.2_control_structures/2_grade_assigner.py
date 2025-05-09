# --- USE: Grade Assigner ---
score = 85 # Try 95, 72, 65, 40
letter_grade = ""
is_passing = score >= 60 # Simple pass/fail check
has_honors = False

print(f"Score: {score}")

if score >= 90 and is_passing: # Using 'and'
    letter_grade = "A"
    has_honors = True
elif score >= 80 and is_passing:
    letter_grade = "B"
elif score >= 70 and is_passing:
    letter_grade = "C"
elif score >= 60 and is_passing: # is_passing is redundant here if score >= 60 implies passing
    letter_grade = "D"
elif not is_passing: # Using 'not'
    letter_grade = "F"
else: # Catch-all, though unlikely with current logic
    letter_grade = "Error in grading"

print(f"Letter Grade: {letter_grade}")
if has_honors:
    print("Congratulations on achieving honors!")
if not is_passing and letter_grade == "F": # Example of 'or' could be: if score < 0 or score > 100: print("Invalid score")
    print("Student needs to retake the course.")
