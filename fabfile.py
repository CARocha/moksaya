from fabric.api import *

user = "aregee"
#Provide the username you used while setting up the project.
key =  "notebook"
#Add the api_key that you createdd in the admin 


def setup():
    local("python manage.py syncdb")
    local("python manage.py migrate")

def start():
    local("python manage.py runserver")


def createUser():
    
    print("\nNow we will create a user named Spock using POST request \n")
    local("""curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"username":"spock","password":"notebook"}' http://127.0.0.1:8000/api/v1/register/""" )

def checkUser():
    print("\nLets GET the Spocks user details \n")
    local("""curl --dump-header - -H "Content-Type:application/json"-X http://127.0.0.1:8000/api/v1/user/spock/?username=%s\&api_key=%s""" % (user,key))

def createProfile():
    print("\nCreating a  Profile for SPOCK \n")
    local("""curl --dump-header - -H "Content-Type:application/json" -X POST --data '{"user":"/api/v1/user/spock/" , "about_me":"Hello I am Spock" }' http://127.0.0.1:8000/api/v1/profile/?username=%s\&api_key=%s""" % (user,key))

def checkProfile():
    print("\nNow GET  Profile for SPOCK\n")
    
    local("""curl http://127.0.0.1:8000/api/v1/profile/2/?username=%s\&api_key=%s""" % (user,key))

def createProject():
    print("\nSpock has no projects , so lets POST a project for him \n")
    local("""curl -F "user=/api/v1/profile/2/" -F "title=Spocks first Project" -F "desc=Spock created objects with javascript" -F "src=@projects/objects.js" -F "screenshot=@projects/img_screen.png" http://127.0.0.1:8000/api/v1/projects/?username=%s\&api_key=%s""" % (user,key))
   
    checkProfile()


def checkProject():

    print("\nWe can directly access the projects by making GET request to the Resource URI of the project\n")

    local("""curl http://127.0.0.1:8000/api/v1/projects/1/?username=%s\&api_key=%s""" % (user,key))
    

def forkProject():
    print("\n %s is logged in as a super user so lets fork Spocks work to their portfolio\n")
    local("""curl http://127.0.0.1:8000/api/v1/forking/1/?username=%s\&api_key=%s""" %(user,key))
    print("\nLets take a look at the %s Profile again \n" % (user))

def createMyprofile():
    print("\nOkay first We need to create a Profile for %s \n" % (user))
    local("""curl --dump-header - -H "Content-Type:application/json" -X POST --data '{"user":"/api/v1/user/aregee/" , "about_me":"Hello I am %s" }' http://127.0.0.1:8000/api/v1/profile/?username=%s\&api_key=%s""" % (user,user,key))
    
    myProfile()
    

def myProfile():
    print("\nLets GET the %s's Profile \n" % (user))
    local("""curl http://127.0.0.1:8000/api/v1/profile/1/?username=%s\&api_key=%s""" % (user,key))

def deleteProject():
    print("\nWe can DELETE the Spocks only project by making a delete request to Projects URI \n")
    local("""curl --dump-header - -H "Content-Type:application/json" -X DELETE http://127.0.0.1:8000/api/v1/projects/1/?username=%s\&api_key=%s""" % (user,key))

    checkProfile()

def deleteProfile():
    
    print("\nWe can DELETE the Spock's Profile by  making a delete request to Profile URI \n")
    local("""curl --dump-header - -H "Content-Type:application/json" -X DELETE http://127.0.0.1:8000/api/v1/profile/2/?username=%s\&api_key=%s;""" % (user,key))


def deleteUser():
    print("\nWe can DELETE the Spock from user database as well \n")
    local(""" curl --dump-header - -H "Content-Type:application/json" -X DELETE http://127.0.0.1:8000/api/v1/user/spock/?username=%s\&api_key=%s""" % (user,key))

def allProfiles():
    
    local("""curl http://127.0.0.1:8000/api/v1/profile/?username=%s\&api_key=%s""" % (user,key))




def test():
    createMyprofile()
    createUser()
    checkUser()
    createProfile()
    checkProfile()
    createProject()
    checkProject()
    forkProject()
    myProfile()
    deleteProject()
    deleteProfile()
    deleteUser()
    allProfiles()
    local("echo If you see Spocks project in your Profile which you forked then +1  ")
    

