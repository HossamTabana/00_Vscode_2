import os
c = get_config()
# Kernel config
c.IPKernelApp.pylab = 'inline'  # if you want plotting support always in your notebook
# Notebook config
c.NotebookApp.notebook_dir = 'work'
c.NotebookApp.allow_origin = u'localhost' # put your public IP Address here
c.NotebookApp.ip = '*'
c.NotebookApp.allow_remote_access = True
c.NotebookApp.open_browser = True
#jupyter server --generate-config
#jupyter notebook --config=./conf/jupyter.py
#from jupyter_server.auth import passwd
#ipython -c "from jupyter_server.auth import passwd; passwd()"
#c.NotebookApp.password = u'argon2:$argon2id$v=19$m=10240,t=10,p=8$Ttk45n8S0OyltcqEOWBbhA$wrZcuQ4AdYSxzGDOKZz2vNDPFq2DskbQaXm41UP6wZA'
#c.NotebookApp.password = u'argon2:$argon2id$v=19$m=10240,t=10,p=8$Eg7/Y23jC4Cs1MlFDa4NPQ$wXnPjHSV8XNZCfGqmZk+Wf1mPotO4tSzvFt+wGNfPPE'
c.NotebookApp.password = u''
c.NotebookApp.token = ''
c.NotebookApp.port = int(os.environ.get("PORT", 8888))
c.NotebookApp.allow_root = True
c.NotebookApp.allow_password_change = True
c.ConfigurableHTTPProxy.command = ['configurable-http-proxy', '--redirect-port', '80']

# without password
 #c.NotebookApp.token = ''
 #c.NotebookApp.password = u''
 #c.NotebookApp.open_browser = True
 #c.NotebookApp.ip = 'localhost'

