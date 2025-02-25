import joblib
from preflop_holdem import PreflopHoldemHistory, PreflopHoldemInfoSet
from postflop_holdem import PostflopHoldemCFR, PostflopHoldemHistory, PostflopHoldemInfoSet




data = joblib.load("../src/postflop_infoSets_batch_19.joblib")
print(type(data))  
print(data)


