all: start

start:
	python info.daemon.py start
	forever start info.node.js

stop:
	python info.daemon.py stop
	forever stop info.node.js

restart:
	python info.daemon.py restart
	forever restart info.node.js

install:
	if command -v npm; then \
    	sudo npm install forever -g; \
    	sudo npm install forever-monitor; \
    	sudo npm install redis;\
    	sudo npm install express; \
    	sudo npm install express.io; \
    	sudo npm install socket.io; \
    	else echo "Please install npm first."; fi

clean:
	rm -rf node_modules/*