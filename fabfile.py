from fabric.api import local


def fabfun():


		local("cd /home/devops/python000/fab-prac/fab-file01/001-file && touch file11 file12 file13")


	        local("cd /home/devops/python000/fab-prac/fab-file01/001-file && git add . && git commit -m test")


	        local("cd /home/devops/python000/fab-prac/fab-file01/001-file && git push origin master")
