#import the library
import redis
# Create connection object on instanceA Redis OSS which is being replicated to instanceB
instanceA = redis.Redis(
host='ip-172-31-8-240', port=6379, password='')
# Use the pipeline() method to create a pipeline instance

# Connect to instanceB on Redis Enterprise to retrieve the values inserted into instanceA
instanceB = redis.Redis(
host='ip-172-31-6-88', port=15228, password='redis123')

numlist='mylist'

# Let's first show that the values in numlist are not currently in instanceA or instanceB
print("mylist is empty on both InstanceA on Redis OSS and InstanceB on Redis Enterprise")
print("InstanceA:element 0",instanceA.lindex(numlist,0)) 
print("InstanceB:element 0",instanceB.lindex(numlist,0)) 

print("Insert values 1 to 100 into mylist on InstanceA Redis OSS")
pipe = instanceA.pipeline()
for counter in range(1,101):
    instanceA.rpush(numlist, counter)
pipe.execute()

print("Retrieve values 1 to 100 in reverse order from InstanceB Redis Enterprise")
while(instanceB.llen(numlist) != 0):
   print(instanceB.rpop(numlist))
