# The goal of this program is to give you the best suitable schedule for your exam preparation

days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"] # vars, we have 6 days of preparation
nb_subjects = 5 # the number of subjects/themes (eg: math, physics, ...)
Domain = [1,2] # Di=1 or Di=2 ; i= 1..card(days). # In each day, we only study 1 or 2 subjects
capacity_per_day = 2

# Constraints:
  # - In each day we can only study 1 or 2 subjects
  # - We have to be able to sudy all the subjects at the end of the preparation period (days)

def max_capacity(nb_units, capacity_per_unit):
  # Return the maximum capacity that the units can hold
  return nb_units * capacity_per_unit

def get_nb_days_available(assignment:dict):
  global days
  s = 0
  for d in days:
    if d not in assignment.keys():
      s += 1
  return s

def check_constraints(assignment:dict):
  # Check if the current configuration allows for future assignemnts
  global nb_subjects
  assigned_subjects = sum(assignment.values()) # the number of the subjects already assigned
  remaining_subjects = nb_subjects - assigned_subjects
  nb_days_avail = get_nb_days_available(assignment)
  if max_capacity(nb_days_avail, capacity_per_day) >= remaining_subjects:
    return True
  return False

def check_goal(assignment:dict):
  global nb_subjects
  if sum(assignment.values()) == nb_subjects:
    return True
  return False

def get_unassigned_var(assignment:dict)->tuple:
  # Return an unassigned variable
  # Return None if not found
  global days
  for var in days:
    if var not in assignment.keys():
      return var
  return None # Can be removed (by default it returns None)

def csp_rec(assignment:dict, solutions_set:list):
  # assignment should be an empty dict {}
  print("Call: ", assignment)
  global Domain
  if check_goal(assignment):
    solutions_set.append(assignment)
    return None
  var = get_unassigned_var(assignment)
  for d in Domain:
    assignment[var] = d
    if check_constraints(assignment):
      res = csp_rec(assignment, solutions_set)
      if res == None:
        return
    # else continue to the next posibility
  
  return None # The search was complete. Note!: this does not give any info about the result


assignment = {}
list_results = []
res= csp_rec(assignment, list_results)
print(assignment)

