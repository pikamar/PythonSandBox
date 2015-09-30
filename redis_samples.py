# Credits
#   https://pypi.python.org/pypi/redis
#   http://code.runnable.com/UsYEiWi1WK0uAABB/redis-client-python-usage
#   https://github.com/andymccurdy/redis-py/tree/master/tests
# Installation
# sudo pip install redis #hiredis
# sudo easy_install redis #hiredis

import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

print ("\n##########> Redis Pipeline")
# Pipelines are a subclass of the base Redis class that provide support for buffering multiple 
# commands to the server in a single request.
pipe = r.pipeline()
# The following SET commands are buffered
pipe.set('foo', 'bar')
pipe.get('bing')
# the EXECUTE call sends all buffered commands to the server, returning
# a list of responses, one for each command.
print (pipe.execute())
rez = pipe.set('foo', 'bar').sadd('faz', 'baz').incr('auto_number').execute()
print (rez)

print ("\n##########> Key increment in transaction")
def client_side_incr(pipe):
    current_value = pipe.get('OUR-SEQUENCE-KEY')
    next_value = int(current_value) + 1
    pipe.multi()
    pipe.set('OUR-SEQUENCE-KEY', next_value)

r.set('OUR-SEQUENCE-KEY',0)
rez = r.transaction(client_side_incr, 'OUR-SEQUENCE-KEY')
print (rez)

print ("\n##########> Set key value pair")
#with the created redis object we can
#submits redis commands as its methods
r.set('test_key', 'test_value') 

# the previous set key is fetched
print ('previous set key ' + r.get('test_key').decode(encoding='UTF-8'))

'''In the previous example you saw that we introduced a redis
data type: the string, now we will set an integer and try to
increase its value using redis object built-in methods'''

print ("\n##########> Set a counter, incement and decrease it`s value")
#set an integer to a key
r.set('counter', 1) 
#we increase the key value by 1, has to be int
r.incr('counter') 
#notice that the key is increased now
print ('the counter was increased! '+ r.get('counter').decode(encoding='UTF-8'))

#we decrease the key value by 1, has to be int
r.decr('counter')
#the key is back to normal
print ('the counter was decreased! '+ r.get('counter').decode(encoding='UTF-8'))


'''Now we are ready to jump into another redis data type, the list, notice 
that they are exactly mapped to python lists once you get them'''

print ("\n##########> Set lists")
#we use list1 as a list and push element1 as its element
r.rpush('list1', 'element1')

#assign another element to our list
r.rpush('list1', 'element2') 
r.rpush('list2', 'element3')

#with llen we get our redis list size right from redis
print ('our redis list len is: %s'% r.llen('list1'))

#with lindex we query redis to tell us which element is at pos 1 of our list
print ('at pos 1 of our list is: %s'% r.lindex('list1', 1))
print ('at pos 1 of our list is: %s'% r.lmembers('list1'))

'''sets perform identically to the built in Python set type. Simply, sets are lists but, can only have unique values.'''
print ("\n##########> Add more elements to the set")
r.sadd("set1", "el1")
r.sadd("set1", "el2")
r.sadd("set1", "el2")

print ('the member of our set are: %s'% r.smembers("set1"))

