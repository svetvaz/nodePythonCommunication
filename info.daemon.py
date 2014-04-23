import redis
try:
    import json
except ImportError:
    import simplejson as json
from daemon import Daemon
import sys

class InfoDaemon(Daemon):
	# def __init__(self):
	# 	pass

	def get_person_info(self,name):
		if name =='John Doe':
			age = 30
			location='Santa Clara'
		elif name == 'Jane Doe':
			age=28
			location='San Francisco'
		elif name=='Baby Doe':
			age=5
			location='Mountain View'
		return age,location			

	def run(self):
		self.r11 = redis.StrictRedis(host='localhost', port=6379, db=11)
		try:
			sub = self.r11.pubsub()
			sub.subscribe('RequestChannel')
			for message in sub.listen():
				if message['type'] == "message":
					response={}
					name = message['data']
					age,location = self.get_person_info(name)
					response = {'age':age,'location':location}
					result = json.dumps(response)
					self.r11.publish("ResponseChannel",result)  	
		except (KeyboardInterrupt, SystemExit):
			sys.exit()





if __name__ == "__main__":
  daemon = InfoDaemon('/tmp/info-daemon.pid')
  if len(sys.argv) == 2:
    if 'start' == sys.argv[1]:
      daemon.start()
    elif 'stop' == sys.argv[1]:
      daemon.stop()
    elif 'restart' == sys.argv[1]:
      daemon.restart()
    else:
      print "Unknown command"
      sys.exit(2)
    sys.exit(0)
  else:
    print "usage: %s start|stop|restart" % sys.argv[0]
    sys.exit(2)
# daemon = InfoDaemon()
# daemon.run()