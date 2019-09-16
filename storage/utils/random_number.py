# the random generation of string id's 
  
import random 
import string 
from datetime import datetime, timedelta
  
# defining function for random 
# string id with parameter 
def ran_gen(size, chars=string.ascii_uppercase + string.digits): 
    generateID = ''.join(random.choice(chars) for x in range(size)) 
    return generateID

def ran_gen_with_date(size, chars=string.ascii_uppercase + string.digits ):
    generateID = ''.join(random.choice(chars) for x in range(size)) 
    date = datetime.now().strftime('%Y%m%d')
    reference_code = '{0}-{1}-KIERO-CC'.format(date,str(generateID))
    return reference_code
    