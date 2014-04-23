nodePythonCommunication
=======================

Node.js - Redis - Python Communication

Shows how to make python do all of the heavy loading and then pass the results to node.js which then pushes the results to the client.

#Requirements
Install node and npm

Then run 'make' like so:
make install      # This will install all the npm dependencies. The node module forever is
                  # globally.

make start    # This will start our daemons

make stop    # This will stop our daemons

make clean    # Only used if we want to clean up the node_modules directory.
              # make install will be required to reinstall them again.

make restart     # This allows restarting the daemons if required.

Open your browser and type : http://localhost:7070
