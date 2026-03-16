from secret_base_of_horrible_baddies import get_secret_plan
from functools import lru_cache

stole_plans = {}

def steal_plans(plan_list):
    stolen_plans_list = []
    for number in plan_list:
        if number not in stole_plans:
            plan = get_secret_plan(number)
            
            if plan is not None:
                stole_plans[number] = plan
        plan = stole_plans[number]
        stolen_plans_list.append(plan)
        
    return stolen_plans_list
    
    
    

        

