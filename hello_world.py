def say_hello(name):
  #these lines are indented therefore part of the function
  if name:
   print 'Hello, ' + name + 'from inside the function'
  else:
   print 'No name'
say_hello("Tom")

def reply(name):
  if name:
    print 'Hello to you too, %s!' % name

  else:
    print 'Please enter a name!'

reply('Jeremy')