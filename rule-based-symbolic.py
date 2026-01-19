#RULE BASED SYMBOLIC
RULES = [
    {"if": ["failed_login", "multiple_attempts"], "then": "Brute-Force Attack"},
    {"if": ["large_upload", "unauthorized_location"], "then": "Data Theft"},
    {"if": ["cpu_spike", "Unknown_process"], "then": "Malware Activity"}
]   
Events={
    "failed_login": False,
    "multiple_attempts": False,
    "large_upload": False,
    "unauthorized_location": False,
    "Unknown_process": False,
    "cpu_spike": False}
    

for x in Events:
    user_said=input(f"Do you want to change the state of {x}: ")
    if user_said =="y":
        Events[x]= True
    else:
        Events[x]= False
#print(Events)

def inference_engine(rule,events): #INFERENCE ENGINE
    detected_anomaly=[]
    for ruler in rule:
        trigger=ruler["if"]
        if all(events.get(t) for t in trigger):
            detected_anomaly.append(ruler["then"])
    return detected_anomaly
    
    
RESULT=inference_engine(RULES,Events)

print(" CYBER-SYMBOLIC RULE-BASED AI SYSTEM ")
print("-------------------------------------")

if RESULT:
    for detection in set(RESULT):
        print(f"Detected {detection}")
else:
    print("System Safe")
     