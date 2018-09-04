#import the library
import redis
# Create connection object
r = redis.Redis(
host='ip-172-31-8-240', port=6379, password='')
#Use the pipeline() method to create a pipeline instance
numlist='mylist'
pipe = r.pipeline()
for counter in range(1,101):
    r.rpush(numlist, counter)
pipe.execute()
while(r.llen(numlist) != 0):
   print(r.rpop(numlist))
