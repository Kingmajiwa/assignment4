def calculate_grade(maths, physics, geo, chem):
    
    if any(mark < 0 or mark > 100 for mark in [maths, physics, geo, chem]):
        return "Unrecognized marks/avg"
    
  
    avg = (maths + physics + geo + chem) / 4
    
    
    if 0 <= avg <= 30:
        return "D"
    elif 31 <= avg <= 50:
        return "C"
    elif 51 <= avg <= 70:
        return "B"
    elif 71 <= avg <= 100:
        return "A"
    else:
        return "Unrecognized marks/avg"


maths = float(input("87: "))
physics = float(input("47: "))
geo = float(input("35: "))
chem = float(input("50: "))


result = calculate_grade(maths, physics, geo, chem)
print("Grade:", result)
