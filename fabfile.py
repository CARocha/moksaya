from fabric.api import *

user = "aregee"
#Provide the username you used while setting up the project.
key =  "b621a010883163b125bb93cef9ed9d2eba5cf0e3"
#Add the api_key that you createdd in the admin 


def setup():

    local("python manage.py syncdb --noinput")
    local("python manage.py migrate")

def update_search():
    local("python manage.py update_index")

def start():
    local("python manage.py runserver")


def PostUser():
    
    print("\nNow we will Recruit  new caddets for Starfleet  using POST request \n")
    local("""curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"username":"spock","password":"notebook"}' http://127.0.0.1:8000/api/v1/register/""" )
    local("""curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"username":"uhura","password":"notebook"}' http://127.0.0.1:8000/api/v1/register/""" )
    local("""curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"username":"kirk", "password":"notebook"}' http://127.0.0.1:8000/api/v1/register/""" )

def GetUser():
    print("\n~ Testing APIS for USER Resource with GET request ~ \n")
    local("""curl --dump-header - -H "Content-Type:application/json"-X http://127.0.0.1:8000/api/v1/user/kirk/?username=%s\&api_key=%s""" % (user,key))
    local("""curl --dump-header - -H "Content-Type:application/json"-X http://127.0.0.1:8000/api/v1/user/spock/?username=%s\&api_key=%s""" % (user,key))
    local("""curl --dump-header - -H "Content-Type:application/json"-X http://127.0.0.1:8000/api/v1/user/uhura/?username=%s\&api_key=%s""" % (user,key))


def PostProfile():
    print("\n ~ Testing APIS for Profile Resource with POST request ~ \n")
    local("""curl --dump-header - -H "Content-Type:application/json" -X POST --data '{"user":"/api/v1/user/spock/" , "about_me":"Hello I am Mister Spock" }' http://127.0.0.1:8000/api/v1/profile/?username=%s\&api_key=%s""" % (user,key))
    local("""curl --dump-header - -H "Content-Type:application/json" -X POST --data '{"user":"/api/v1/user/uhura/" , "about_me":"Hello I am Uhura" }' http://127.0.0.1:8000/api/v1/profile/?username=%s\&api_key=%s""" % (user,key))
    local("""curl --dump-header - -H "Content-Type:application/json" -X POST --data '{"user":"/api/v1/user/kirk/" , "about_me":"Hello I am Kirk,Captain of the USS Enterprise" }' http://127.0.0.1:8000/api/v1/profile/?username=%s\&api_key=%s""" % (user,key))

def GetProfile():
    print("\n ~ Testing APIS for Profile Resource with GET request ~\n")
    
    local("""curl http://127.0.0.1:8000/api/v1/profile/?username=%s\&api_key=%s""" % (user,key))



def PatchProfile():

    print("\n ~ Testing APIS for Profile Resource with PATCH request ~ \n")
    local("""curl --dump-header - -H "Content-Type:application/json" -X PATCH --data '{"user":"/api/v1/user/spock/" , "about_me":"Hello I am Mister Spock ,I am updated with patch request" }' http://127.0.0.1:8000/api/v1/profile/2/?username=%s\&api_key=%s""" % (user,key))
    local("""curl --dump-header - -H "Content-Type:application/json" -X PATCH --data '{"user":"/api/v1/user/uhura/" , "about_me":"Hello I am Uhura , I am updated with patch request" }' http://127.0.0.1:8000/api/v1/profile/3/?username=%s\&api_key=%s""" % (user,key))
    local("""curl --dump-header - -H "Content-Type:application/json" -X PATCH --data '{"user":"/api/v1/user/kirk/" , "about_me":"Hello I am Kirk,Captain of the USS Enterprise and I am updated with patch request" }' http://127.0.0.1:8000/api/v1/profile/4/?username=%s\&api_key=%s""" % (user,key))


def PostProject():

    print("\nSpock has no projects , so lets POST a project for him \n")
    local("""curl -F "user=/api/v1/profile/2/" -F "title=Fiddle with JS" -F "desc=this file documents my PROGRESS with learning JavaScript" -F "src=@projects/objects.js" -F "screenshot=@projects/img_screen.png" http://127.0.0.1:8000/api/v1/projects/?username=%s\&api_key=%s""" % (user,key))
    print("\nUhura has no projects , so lets POST a project for her \n")
    local("""curl -F "user=/api/v1/profile/3/" -F "title=Looping for a While " -F "desc=It been a while and I know how to iterate" -F "src=@projects/while.js" -F "screenshot=@projects/img_screen.png" http://127.0.0.1:8000/api/v1/projects/?username=%s\&api_key=%s""" % (user,key))
    print("\nKirk has no projects , so lets POST a project for him \n")
    local("""curl -F "user=/api/v1/profile/4/" -F "title=Gallery Lock " -F "desc=This python script changes extension of all the media files in the directory so they are not skipped in a media scan" -F "src=@projects/file_rem.py" -F "screenshot=@projects/img_screen.png" http://127.0.0.1:8000/api/v1/projects/?username=%s\&api_key=%s""" % (user,key))   
    
    #GetProfile()


def GetProject():

    print("\nWe can directly access the projects by making GET request to the Resource URI of the project\n")

    local("""curl http://127.0.0.1:8000/api/v1/projects/?username=%s\&api_key=%s""" % (user,key))
    

def PatchProject():

    print("\nlets  PATCH a project for Spock \n")
    local("""curl --dump-header - -H "Content-Type:application/json" -X PATCH --data '{"title":"Gallery Lock ++ " }' http://127.0.0.1:8000/api/v1/projects/1/?username=%s\&api_key=%s""" % (user,key))
    print("\nso lets PATCH a project for Uhura \n")
    local("""curl --dump-header - -H "Content-Type:application/json" -X PATCH --data '{"title":"Looping ++ " }' http://127.0.0.1:8000/api/v1/projects/2/?username=%s\&api_key=%s""" % (user,key))
    print("\nso lets PATCH a project for Kirk \n")
    local("""curl --dump-header - -H "Content-Type:application/json" -X PATCH --data '{"title":"Gallery Lock  ++ " }' http://127.0.0.1:8000/api/v1/projects/3/?username=%s\&api_key=%s""" % (user,key))

def forkProject():
    print("\n %s is logged in as a Admiral of the StarFlee  and  can fork the projects of all the USS Enterprise Officiers \n" % user)
    local("""curl http://127.0.0.1:8000/api/v1/forking/1/?username=%s\&api_key=%s""" %(user,key))
    local("""curl http://127.0.0.1:8000/api/v1/forking/2/?username=%s\&api_key=%s""" %(user,key))
    local("""curl http://127.0.0.1:8000/api/v1/forking/3/?username=%s\&api_key=%s""" %(user,key))
    print("\nLets take a look at the %s Profile again \n" % (user))

def PostMyprofile():
    print("\nOkay first We need to create a Profile for %s \n" % (user))
    local("""curl --dump-header - -H "Content-Type:application/json" -X POST --data '{"user":"/api/v1/user/aregee/" , "about_me":"Hello I am %s" }' http://127.0.0.1:8000/api/v1/profile/?username=%s\&api_key=%s""" % (user,user,key))
    
#    myProfile()
    

def GetMyprofile():
    print("\nLets GET the %s's Profile \n" % (user))
    local("""curl http://127.0.0.1:8000/api/v1/profile/1/?username=%s\&api_key=%s""" % (user,key))


def DeleteMyProfile():
    local("""curl --dump-header - -H "Content-Type:application/json" -X DELETE http://127.0.0.1:8000/api/v1/profile/1/?username=%s\&api_key=%s;""" % (user,key))
def DeleteProject():
    print("\nWe can DELETE the Spocks only project by making a delete request to Projects URI \n")
    local("""curl --dump-header - -H "Content-Type:application/json" -X DELETE http://127.0.0.1:8000/api/v1/projects/1/?username=%s\&api_key=%s""" % (user,key))
    local("""curl --dump-header - -H "Content-Type:application/json" -X DELETE http://127.0.0.1:8000/api/v1/projects/2/?username=%s\&api_key=%s""" % (user,key))
    local("""curl --dump-header - -H "Content-Type:application/json" -X DELETE http://127.0.0.1:8000/api/v1/projects/3/?username=%s\&api_key=%s""" % (user,key))    

    #checkProfile()

def DeleteProfile():
    
    print("\nWe can DELETE the Spock's Profile by  making a delete request to Profile URI \n")
    local("""curl --dump-header - -H "Content-Type:application/json" -X DELETE http://127.0.0.1:8000/api/v1/profile/2/?username=%s\&api_key=%s;""" % (user,key))
    local("""curl --dump-header - -H "Content-Type:application/json" -X DELETE http://127.0.0.1:8000/api/v1/profile/3/?username=%s\&api_key=%s;""" % (user,key))
    local("""curl --dump-header - -H "Content-Type:application/json" -X DELETE http://127.0.0.1:8000/api/v1/profile/4/?username=%s\&api_key=%s;""" % (user,key))


def DeleteMyprofile():
    
    print("\nWe can DELETE the SuperUser's Profile by  making a delete request to Profile URI \n")
    local("""curl --dump-header - -H "Content-Type:application/json" -X DELETE http://127.0.0.1:8000/api/v1/profile/1/?username=%s\&api_key=%s;""" % (user,key))



def DeleteUser():
    print("\nWe can DELETE the Spock from user database as well \n")
    local(""" curl --dump-header - -H "Content-Type:application/json" -X DELETE http://127.0.0.1:8000/api/v1/user/spock/?username=%s\&api_key=%s""" % (user,key))
    local(""" curl --dump-header - -H "Content-Type:application/json" -X DELETE http://127.0.0.1:8000/api/v1/user/uhura/?username=%s\&api_key=%s""" % (user,key))
    local(""" curl --dump-header - -H "Content-Type:application/json" -X DELETE http://127.0.0.1:8000/api/v1/user/kirk/?username=%s\&api_key=%s""" % (user,key))





def PostRelations():
    print("\nUsing RESTful interface to create follower followee relationship between users with POST ")
    local("""curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"follower":"/api/v1/profile/2/","followee":"/api/v1/profile/1/"}'  http://127.0.0.1:8000/api/v1/relations/?username=%s\&api_key=%s""" % (user,key))
    
    local("""curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"follower":"/api/v1/profile/2/","followee":"/api/v1/profile/4/"}'  http://127.0.0.1:8000/api/v1/relations/?username=%s\&api_key=%s""" % (user,key))

    local("""curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"follower":"/api/v1/profile/3/","followee":"/api/v1/profile/4/"}'  http://127.0.0.1:8000/api/v1/relations/?username=%s\&api_key=%s""" % (user,key))

    local("""curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"follower":"/api/v1/profile/3/","followee":"/api/v1/profile/2/"}'  http://127.0.0.1:8000/api/v1/relations/?username=%s\&api_key=%s""" % (user,key))
    
    local("""curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"follower":"/api/v1/profile/3/","followee":"/api/v1/profile/1/"}'  http://127.0.0.1:8000/api/v1/relations/?username=%s\&api_key=%s""" % (user,key))


    local("""curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"follower":"/api/v1/profile/4/","followee":"/api/v1/profile/1/"}'  http://127.0.0.1:8000/api/v1/relations/?username=%s\&api_key=%s""" % (user,key))



def GetRelations():
    
    local("""curl http://127.0.0.1:8000/api/v1/relations/?username=%s\&api_key=%s""" % (user,key))


def DeleteRelations():

    local("""curl --dump-header - -H "Content-Type: application/json" -X DELETE http://127.0.0.1:8000/api/v1/relations/1/?username=%s\&api_key=%s""" % (user,key))
    local("""curl --dump-header - -H "Content-Type: application/json" -X DELETE http://127.0.0.1:8000/api/v1/relations/2/?username=%s\&api_key=%s""" % (user,key))
    local("""curl --dump-header - -H "Content-Type: application/json" -X DELETE http://127.0.0.1:8000/api/v1/relations/3/?username=%s\&api_key=%s""" % (user,key))
    local("""curl --dump-header - -H "Content-Type: application/json" -X DELETE http://127.0.0.1:8000/api/v1/relations/4/?username=%s\&api_key=%s""" % (user,key))    
    local("""curl --dump-header - -H "Content-Type: application/json" -X DELETE http://127.0.0.1:8000/api/v1/relations/5/?username=%s\&api_key=%s""" % (user,key))

def PostLikes():
    print("\nUsing RESTful interface to POST likes to the Projects")
    local("""curl --dump-header - -H "Content-Type:application/json" -X POST --data '{"user":"/api/v1/profile/2/" ,"liked_content_type":"/api/v1/projects/2/" }' http://127.0.0.1:8000/api/v1/liking/?username=%s\&api_key=%s""" % (user,key))
    local("""curl --dump-header - -H "Content-Type:application/json" -X POST --data '{"user":"/api/v1/profile/1/" ,"liked_content_type":"/api/v1/projects/2/" }' http://127.0.0.1:8000/api/v1/liking/?username=%s\&api_key=%s""" % (user,key))

def GetLikes():

    local("""curl --dump-header - -H "Content-Type:application/json" -X GET http://127.0.0.1:8000/api/v1/liking/?username=%s\&api_key=%s""" % (user,key))

def DeleteLikes():
    print("\nUsing RESTful interface to Delete likes from the Projects")
    local("""curl --dump-header - -H "Content-Type:application/json" -X DELTE http://127.0.0.1:8000/api/v1/liking/1/?username=%s\&api_key=%s""" % (user,key))
    local("""curl --dump-header - -H "Content-Type:application/json" -X DELTE http://127.0.0.1:8000/api/v1/liking/2/?username=%s\&api_key=%s""" % (user,key))



def PostComment():
    print("\nUsing RESTful interface to POST comments to the Projects")
    local("""curl --dump-header - -H "Content-Type:application/json" -X POST --data '{"user":"/api/v1/profile/1/","entry":"/api/v1/projects/2/" , "text":"Comment posted with REST" }' http://127.0.0.1:8000/api/v1/comment/?username=%s\&api_key=%s""" % (user,key))
    local("""curl --dump-header - -H "Content-Type:application/json" -X POST --data '{"user":"/api/v1/profile/1/","entry":"/api/v1/projects/1/" , "text":"Good Work Spock" }' http://127.0.0.1:8000/api/v1/comment/?username=%s\&api_key=%s""" % (user,key))

def GetComment():
    print("\nUsing RESTful interface to GET comments to the Projects")
    local("""curl --dump-header - -H "Content-Type:application/json" -X GET http://127.0.0.1:8000/api/v1/comment/?username=%s\&api_key=%s""" % (user,key))


def PatchComment():
    print("\nUsing RESTful interface to PATCH and PUT  comments to the Projects")
    local("""curl --dump-header - -H "Content-Type:application/json" -X PATCH --data '{"user":"/api/v1/profile/1/","entry":"/api/v1/projects/2/" , "text":"Comment POSTed with updated with PATCH" }' http://127.0.0.1:8000/api/v1/comment/1/?username=%s\&api_key=%s""" % (user,key))
    local("""curl --dump-header - -H "Content-Type:application/json" -X PATCH --data '{"entry":"/api/v1/projects/1/" , "text":"ahm correction Good Woork Mister Spock"}' http://127.0.0.1:8000/api/v1/comment/2/?username=%s\&api_key=%s""" % (user,key))

def DeleteComment():
    print("\nUsing RESTful interface to DELETE comments to the Projects")
    local("""curl --dump-header - -H "Content-Type:application/json" -X PATCH --data '{"text":"Comment posted with REST but then updated with Patch" }' http://127.0.0.1:8000/api/v1/comment/1/?username=%s\&api_key=%s""" % (user,key))
    local("""curl --dump-header - -H "Content-Type:application/json" -X PUT --data '{"user":"/api/v1/profile/2/","entry":"/api/v1/projects/4/" , "text":"Yet another comment with REST was posted on wrong project its rectified and PUT on new project" }' http://127.0.0.1:8000/api/v1/comment/2/?username=%s\&api_key=%s""" % (user,key))

    
def allProfiles():
    print("\n Getting the list of all user profiles ")
    local("""curl http://127.0.0.1:8000/api/v1/profile/?username=%s\&api_key=%s""" % (user,key))


def GetTest():
    GetUser()
    GetProfile()
    GetProject()
    GetRelations()
    GetLikes()
    GetComment()
    GetMyprofile()
    forkProject()
    allProfiles()

def PostTest():
    PostUser()
    PostMyprofile()
    PostProfile()
    
    PostRelations()
    PostProject()
    PostLikes()
    PostComment()
    

def PatchTest():
    PatchProfile()
    PatchComment()
    PatchProject()

   
def test():

    PostTest()
    
   
    
    GetTest()
    PatchTest()
    
    #DeleteProject()
    
    allProfiles()
    local("echo If you see Spocks project in your Profile which you forked then +1  ")
    

def clean():
    DeleteComment()
    DeleteLikes()
    DeleteProject()
    DeleteRelations()
    DeleteProfile()
    DeleteUser()
    DeleteMyProfile()
