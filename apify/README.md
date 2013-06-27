Moksaya :
======================================================================

apify an attempt to create a restful interface to moksaya 


###Setup:
    $virtualenv ../ENV
    $source ../ENV/bin/activate
    $pip install -r requirements.txt
    $python manage.py syncdb
    $python manage.py migrate	
    $python manage.py runserver

###Usage:

You can use your browser to acces the restful apis,
Lets say I want to access list of all user profiles so 

http://127.0.0.1:8000/api/v1/profile/list/?format=json 
So the above request would return list of all the user profiles along with their uploaded projects and could be further extended to include other related fields. 

	{
	meta: {
	limit: 20,
	next: null,
	offset: 0,
	previous: null,
	total_count: 2
	},
	objects: [
	{
	about_me: "DjangoNaut",
	birth_date: "1991-06-20",
	gender: 1,
	language: "en",
	location: "India",
	mugshot: "/media/mugshots/d749832b7a.jpg",
	privacy: "registered",
	projects: [],
	user: "aregee",
	website: "http://rahulgaur.info/"
	},
	{
	about_me: "Profile BIO",
	birth_date: "2013-06-26",
	gender: 2,
	language: "en",
	location: "Delhi",
	mugshot: null,
	privacy: "registered",
	projects: [ ],
	user: "testuser",
	website: "http://Something.com/"
	}
	]
	}

Now we want to access the userprofile of particular user say we use pk here as refference , so pk 1 can be accesed in the following way

http://127.0.0.1:8000/api/v1/profile/list/1/?format=json 

This request list the user profile requested by the pk and list all the assoiciated fields like projecs of the User , and comments associated with it.


	{
	about_me: "DjangoNaut",
	birth_date: "1991-06-20",
	gender: 1,
	language: "en",
	location: "India",
	mugshot: "/media/mugshots/d749832b7a.jpg",
	privacy: "registered",
	projects: [
	{
	comment: [
	{
	resource_uri: "",
	text: "MAhn this is some awesome shit "
	},
	{
	resource_uri: "",
	text: "cool Man comments are returned in APIs"
	}
	],
	desc: "here is another hack by me and I am doing this right now",
	owner: "aregee",
	screenshot: "/media/projects/Screenshot_from_2013-01-21_030756.png",
	shared_date: "2013-06-25T18:48:18.205760",
	src: "/media/proejcts/admin.py",
	title: "Another story i am covering and i want to test the constrains this time"
	},
	{
	comment: [ ],
	desc: "Wired Hack ",
	owner: "aregee",
	screenshot: "/media/projects/background.png",
	shared_date: "2013-06-26T05:59:48.445868",
	src: "/media/proejcts/startconky.sh",
	title: "Someting Wong"
	}
	],
	user: "aregee",
	website: "http://rahulgaur.info/"
	}


This is how we can generate Profile pages for the users.

Next part , each project uploaded by the user can be indvidually accessed by the pk here and would be associated to their respective owners and other necessary meta deta ,say for the forked project we can keep a record of who is the initial author and current version.


http://127.0.0.1:8000/api/v1/projects/?format=json

	{
	meta: {
	limit: 20,
	next: null,
	offset: 0,
	previous: null,
	total_count: 3
	},
	objects: [
	{
	comment: [
	{
	resource_uri: "",
	text: "MAhn this is some awesome shit "
	},
	{
	resource_uri: "",
	text: "cool Man comments are returned in APIs"
	}
	],
	desc: "here is another hack by me and I am doing this right now",
	owner: "aregee",
	screenshot: "/media/projects/Screenshot_from_2013-01-21_030756.png",
	shared_date: "2013-06-25T18:48:18.205760",
	src: "/media/proejcts/admin.py",
	title: "Another story i am covering and i want to test the constrains this time"
	},
	{
	comment: [ ],
	desc: "Wired Hack ",
	owner: "aregee",
	screenshot: "/media/projects/background.png",
	shared_date: "2013-06-26T05:59:48.445868",
	src: "/media/proejcts/startconky.sh",
	title: "Someting Wong"
	},
	{
	comment: [ ],
	desc: "This is my first hello world code",
	owner: "testuser",
	screenshot: "/media/projects/Screenshot_from_2013-02-03_173238.png",
	shared_date: "2013-06-27T15:31:22.560494",
	src: "/media/proejcts/hello.c",
	title: "First Project Upload"
	}
	]
	}


Further each profject can be individually reached in the following way 
http://127.0.0.1:8000/api/v1/projects/<1,2,3....>/?format=json


