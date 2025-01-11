from soduko_create import create_soduko
import time as t

start = t.perf_counter()
soduko= create_soduko()
print(soduko)
#print(solution_soduko)
end = t.perf_counter()
time = end - start 
print(time)
