age = 19
money = 40

# OPERATORY LOGICZNE
if age >= 18 and money >= 35: # AND
    print("Może wejść")
if age <= 12 or money >= 30: # OR
    print("Może wejść")
if not age > 12 or money >= 30:
    print("Może wejść")

# KOLEJNOŚĆ WYKONYWANIA OPERATORÓW LOGICZNYCH
if True or False and False:
    print("Prawda")

# OPERATOR AND - LOGICZNE MNOŻENIE
# OPERATOR OR  - LOGICZNE SUMOWANIE