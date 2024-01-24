# <div style="text-align:center;">Drishya Nepal</div>

## <div style="text-align:center;">Documentation of The Project</div>

#### Functional Requirements:

1. 3-Tier Architecture

2. Hiring System 

3. Contact

4. Services

#### Non - functional Requirements:

1. Chat System

2. Location 

3. Review/Rating/Feedback System

4. Tags #photographer status

### <div style="text-align:center">Completed Requirements</div>

#### Functional Requirements:

1. 

2. 

3. 

4. 

#### Non - functional Requirements:

1. 

2. 

3. 

4. 

### Description of Functional requirements:

1. 3-Tier Architecture:
   
       Our project has customer, photographer and admin panel.

2. Hiring System:
   
       Customers can hire photographers based on location, experience, equipment, ratings and feedback.

3. Contact:
   
       This page contains details of developers so that clients can directly contact if there are any other bugs.

4. Services:
   
       Photographers can add, update, and delete various services.
   
       Clients/Customers can also get various services according to photographers’ duration, price,etc.

5. Equipments:
   
       Photographers can upload equipment based on their availability and can manage equipment.

6. Search/Filter: 
   
       Customers can search photographers with respect to their location, equipment, tags,etc.

### Description of Non-functional Requirements:

1. Chat System: 
   
   After the hiring process is completed, customers can chat with their respective photographers for more information.

2. Location: 
   
   Customers can search photographers based on their location.

3. Review/Rating: 
   
   Customers can review and give rating to their respective photographer after events.

4. Tags: 
   
   This is a predefined value which is given by developers to photographers based on their skills. For eg, portrait, vlog,etc.

<hr>

#### Main Documentation

- Django-Project-Name : Drishya_Nepal
  
  <code>Command : django-admin.py startproject project-name</code>

- Created superuser:
  
  <pre>
  Username : test
  Password : test
  </pre>

- Image field cannot be used. To use image field:

  <code>Command : pip install pillow</code>

- The database theme used : Jazzmin -v2.6.0
  
  <code>Command : pip install django-jazzmin</code>

- The basic django setup is done as django is in MVT architecture. So, the “templates” folder is created in “website application” and .html formats are stored whereas other assets like js, css, img,etc. are stored in the “static” folder.
  
  

- In settings.py, the basic django setup is done as:
  
  ```django
  Import os
  BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  STATIC_URL = '/static/'
  STATICFILES_DIRS = [
      os.path.join(BASE_DIR , 'static')
  ]
  STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
  #media 
  MEDIA_URL = '/media/'
  
  
  MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
  ```



- Applications_Created:
  1. Client
  
  2. Management
  
  3. Service_Provider
  
  4. Website
  
  
  
  
- Inside Applications, inside models.py, classes were made accordingly as follows:
  1. **<u>client</u>**
     
     1. Customer
        
        - username
        
        - name
        
        - age
        
        - email
        
        - address
        
        - phone_number
        
        - ! Profile Picture
     
     2. Feedback
        
        - message
        
        - rating
          
          
  
  2. **<u>mangement</u>**
     
     1. Hire
        
        - location
        
        - date
        
        - price (according to photographerservice rate)
        
        - description
          
          
  
  3. **<u>service_provider</u>**
     
     1. Tag
        
        - name
     
     2. Photographer
        
        - username
        
        - name
        
        - age
        
        - address
        
        - email
        
        - phone_number
        
        - experience
        
        - tags
        
        - is_available
        
        - images (photos of photographer)
        
        - is_videographer
        
        - created_at
        
        - updated_at
     
     3. Photo
        
        - name
        
        - location
        
        - description
        
        - type
        
        - date_taken
        
        - photo
     
     4. Equipment
        
        - name
        
        - description
        
        - photo (equipment photo)
     
     5. Services
        
        - name
        
        - description
        
        - price
        
        - duration
          
          
  
  4. **<u>Website</u>**
     
     1. Information
        
        - name
        
        - email
        
        - address
        
        - phone_number
     
     2. Developer
        
        - name
        
        - email
     
     3. About
        
        - name
        
        - description
        
        - photo (logo in about page)
- **Note: any changes in database (models.py) makemigrations!!!**
  
  **<code>Command : python manage.py makemigration</code>**
  
  **<code>Command : python manage.py migrate</code> **
  
  
- The base/ backbone of our project is stored in “base.html” which contains the header and footer of our projects and other web pages are spread around.
  
  
- We are frequently trying to use **JINJA** code in our templates to connect backend to frontend. 
  
  **JINJA** command:
  1. <code>
     {%for photographer in photographers %}
     <br>
     {{ photographer.name }}
     </code>
  
  2.  <code>{% url “index”%}</code>



### GIT & GITHUB INILIZATIONS

#### Push:

GIT rules to push **ACP!!!! (add, commit push)**

Firstly create, “.gitignore” file in the folder and paste the document from website “Toptal”

We did git pushing process,

1. git init

2. git add .

3. git branch -M branch_name

4. git remote add origin "link"

5. git commit -m "#changes haru lekhney"

6. git push origin branch_name



To check branch : git checkout branch_name



#### Pull:

To pull the file,

1. git status

2. git reset -hard HEAD

3. git status

4. git pull origin branch_name
