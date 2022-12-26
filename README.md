# [justBLOG](https://justblog.herokuapp.com/)

A blog website, created as project to apply and display my current knowledge of front-end techonologies and back-end, using Django. The website, justBlog, is an open blog created to allow any user to express himself, by creating a blog post or commenting on other's user post as well, or just "surf" the blog and read content.

<img src="https://github.com/gioZAK/justblog/blob/5d1973f4ca64550c18efcb51832c48be752e378e/docs/screenshots/amiresponsive.png">
 
[Click here](https://justblog.herokuapp.com/) to visit the deployed site.


---

# Table of contents

1. [Design](#design)
2. [UX](#ux)
3. [Agile Workflow](#agile-workflow)
4. [Structure](#structure)
5. [Features](#features)
6. [Technologies Used](#technologies-used)    
8. [Testing](#testing)
8. [Deployment](#deployment)
9. [Credits](#credits)

## Design

The main idea was to develop a website with a simple design which would not distract the user, the color scheme used allows a good contrast.

### Colors

The colors used were: 
- White primary color: #fafafa;
- White secondary color: #fff;
- Blue color: #0004ff;
- Dark color: #000000;
- Accent color: #fb0202;

### Typography

- The main font fmaily used is Roboto and sans-serif as backup.
- For the logo Lato was used and sans-serif as a backup.

### Wireframe

<details>
<summary>
Wireframe
</summary>
<details>
<summary>
Wireframe Home
</summary>
<img src="https://github.com/gioZAK/justblog/blob/5d1973f4ca64550c18efcb51832c48be752e378e/docs/wireframes/wireframeshome.png">
</details>
<details>
<summary>
Wireframe Blog Post
</summary>
<img src="https://github.com/gioZAK/justblog/blob/5d1973f4ca64550c18efcb51832c48be752e378e/docs/wireframes/wireframesblogpost.png">
</details>
<details>
<summary>
Wireframe Profile
</summary>
<img src="https://github.com/gioZAK/justblog/blob/5d1973f4ca64550c18efcb51832c48be752e378e/docs/wireframes/wireframesuserprofile.png">
</details>
<details>
<summary>
Wireframe Post/Edit/Profile
</summary>
<img src="https://github.com/gioZAK/justblog/blob/5d1973f4ca64550c18efcb51832c48be752e378e/docs/wireframes/wireframespostedit.png">
</details>
</details>

## UX

The blog objective is to be accessible to everyone, anyone can create an account and post there, there is no fixed topic, any content is accepted.
Only the comments require aprove so insults can be avoided.

### Site User Goal

- Read new content posted by someone.
- Read other user comments related to a post.
- Post and Comment in the website to express himself.

### Site Goal

- Provide a platform where people can express themselves.
- Moderate unwanted comments or if needed delete a post.
- Provide entertainment.

## Agile Workflow

This project was created using Agile techniques during development, such as:

- User stories: displayed using GitHub Issues.
- MoSCoW method: by adding a priority to each issue and display it using tags.
- ToDo, In Progress and Done: using the GitHub Kanban board.

You can access the Kanban board that was used during the project development [here](https://github.com/users/gioZAK/projects/10/views/1).

You can access the list of issues/user stories used during the development of this project [here](https://github.com/gioZAK/justblog/issues?q=is%3Aissue+is%3Aclosed)
<img src="https://github.com/gioZAK/justblog/blob/5d1973f4ca64550c18efcb51832c48be752e378e/docs/screenshots/kanban.png">


[Back to Table of contents](#table-of-contents)
## Features

### Home page
- Content:
    - Blog post list
    - Paginated list of post
    - Post Title, Summary, Author's name and image, number of likes

<img src="https://github.com/gioZAK/justblog/blob/5d1973f4ca64550c18efcb51832c48be752e378e/docs/features/mainimg.png">

### Post Page
- Content:
    - Post content
    - Like button and number of comments
    - Allows the owner of the post to edit or delete the post
    - Display to the blog post viewer an invitation to check on the author's profile
    - Comment field and the posted comments

<img src="https://github.com/gioZAK/justblog/blob/5d1973f4ca64550c18efcb51832c48be752e378e/docs/features/postimg.png">
<img src="https://github.com/gioZAK/justblog/blob/5d1973f4ca64550c18efcb51832c48be752e378e/docs/features/postimg2.png">
<img src="https://github.com/gioZAK/justblog/blob/5d1973f4ca64550c18efcb51832c48be752e378e/docs/features/postimgowner.png">


### Profile
- Content:
    - Username, username picture, biography and his list of post.
    - Allows the owner of the profile to edit his profile, edit or delete account and change his password.

<img src="https://github.com/gioZAK/justblog/blob/5d1973f4ca64550c18efcb51832c48be752e378e/docs/features/profileimg.png">

### NavBar

- Content:
    - The Logo, Home page button, register button, user profile button, login or logout button
    - Welcome user status, which tells which username is logged in.

    <img src="https://github.com/gioZAK/justblog/blob/5d1973f4ca64550c18efcb51832c48be752e378e/docs/features/navbar.png">

### Future Features

- Search bar
    - Could be added so the user can search for the blog topic or user he wants to find
- Post Categories
    - Could be added in order to classify the post by it's content.

## Technologies Used

### Main Tech

 - [Django](https://www.djangoproject.com/) 
 - [JavaScript](https://www.javascript.com/)
 - [Bootstrap](https://getbootstrap.com/)

[Back to Table of contents](#table-of-contents)
### Applications, Libraries and Platforms

- Git
    - Used for version control to commit to Git and Push to GitHub.
- Gitpod
    - Used as the IDE to write all the code used in this project.
- Github
    - GitHub is used to store the projects code after being pushed from Git.
- Heroku
    - Used to deploy the application.
- Google Fonts
    - Used to import the fonts Roboto and Lato.
- FontAwesome
    - Used to import the ThumbsUp and Comment icon.
- Balsamiq Wireframes
    - Used to create the project's wireframe.
- Cloudinary
    - Used to host all images.
- Django AllAuth
    - Used to deal with user account registration.
- Chrome DevTool
    - Used to debug and test new styles.
- ChatGTP
    - Used to debug.


## Testing
- I have used automated test and manual testing to check if all the website's functionalities were working as intended.
    -They all passed.

### Python Testing
- I have tested all python files and they all passed
- Tested with [CI pep8](https://pep8ci.herokuapp.com/)
<img src="https://github.com/gioZAK/justblog/blob/5d1973f4ca64550c18efcb51832c48be752e378e/docs/testing/testblogview.png">

### JavaScript Testing
- I have tested the script.js and it passed with no major error.
- The undefined variable is not a glitch.
- Tested with [JSHint](https://jshint.com/)
<img src="https://github.com/gioZAK/justblog/blob/5d1973f4ca64550c18efcb51832c48be752e378e/docs/testing/jshint.png">

### CSS Testing
- I have tested the script.css file and it passed.
- Tested with [Jigsaw](https://jigsaw.w3.org/css-validator/)
<img src="https://github.com/gioZAK/justblog/blob/5d1973f4ca64550c18efcb51832c48be752e378e/docs/testing/csstest.png">

### HTML Testing
- I have tested all templates and they all passed.
- Tested with [Validator.w3](https://validator.w3.org/nu/#textarea)
<img src="https://github.com/gioZAK/justblog/blob/5d1973f4ca64550c18efcb51832c48be752e378e/docs/testing/htmltest.png">

### LightHouse
- I have tested the all webpages with LightHouse and they all exceeded with good scores
<img src="https://github.com/gioZAK/justblog/blob/5d1973f4ca64550c18efcb51832c48be752e378e/docs/testing/lighthouseimg.png">

[Back to Table of contents](#table-of-contents)
### Manual Testing
 - Here is the sequence of manual test I have applied to check if all applications work.

#### As a user I want to register.
- Steps: 
    1. Click on the REGISTER button in the NavBar.
    2. The Sign Up form is displayed.
    3. User Fill Up the form and press Sign Up.
    4. Success message is displayed and user is now logged in.

- Outcome:
    - Pass.

#### As a user I want to Logout.
- Requirements:
    - User is logged in.

- Steps: 
    1. Click on the Logout button in the NavBar
    2. Click Sign Out.
    3. User will be redirected to the home page and a success message is displayed.
        - User is now Logged out from the blog.

- Outcome:
    - Pass.

#### As a user I want to Logout.
- Requirements:
    - User is already registered.

- Steps: 
    1. Click on the Login button in the NavBar
    2. Fill up the login form.
    3. Click on the Login button.
    4. User will be redirected to the home page and a success message is displayed.
        - User is now Logged in.

- Outcome:
    - Pass.

#### As a user I want to Create a Blog Post.
- Requirements:
    - User is logged in.

- Steps: 
    1. Click on the "Create a new post" button, which is only displayed after the user is logged in.
    2. Fill up the Title and Content, the Excerpt is not mandatory.
    3. Press the "Create" Button
    3. User is redirected to a new page with the post content and a success message is displayed.

- Outcome:
    - Pass.

#### As a user I want to Edit my Blog Post.
- Requirements:
    - User is logged in.
    - Have a post created.
    - Go to the post page.
    - Be the author of that page.

- Steps: 
    1. Go to the post page that you want to edit.
    2. Scroll down and you will see a "Edit Post" button.
    3. Click on the button.
    4. User is redirected to a form which contains the information he posted in the "Create a Blog Post"
    5. User submit the edition by clicking the "Submit Changes" Button.
    6. User is redirected to the post page he just eddited and a success message is displayed.

- Outcome:
    - Pass.

#### As a user I to Delete my Blog Post.
- Requirements:
    - User is logged in.
    - Have a post created.
    - Go to the post page.
    - Be the author of that page.

- Steps: 
    1. Go to the post page that you want to delete.
    2. Scroll down and you will see a "Delete Post" button.
    3. Click on the button.
    4. User is redirected to a page that ask if he is sure that he wants to delete the post.
    5. User clicks on the "Delete" Button
    6. User is redirected to home page and a success message is displayed.

- Outcome:
    - Pass.

#### As a user I want to Comment on a Post.
- Requirements:
    - User is logged in.

- Steps: 
    1. Go to the post that he wants to comment.
    2. Scroll down and on the right side there is a Leave a comment field.
    3. User writes his comment and press the submit button
    4. A message of "Your comment is awaiting approval" appears.
    5. After the admin reads the message he can chose to approve or not.
    6. If approved image is displayed on the Comments field.

- Outcome:
    - Pass.

#### As a user I want to Like a Post.
- Requirements:
    - User is logged in.

- Steps: 
    1. Go to the post that he wants to like.
    2. Scroll down and under the post content there is a like button.
    3. User clicks on the button.
    4. The page reloads.
    5. The like button is now solid red and the like count increases by one.

- Outcome:
    - Pass.

#### As a user I want to unlike a Post.
- Requirements:
    - User is logged in.
    - Have liked the post before

- Steps: 
    1. Go to the post that he wants to unlike.
    2. Scroll down and under the post content there is a solid red like button.
    3. User clicks on the button.
    4. The page reloads.
    5. The like button is now grey and empty and the like count decreases by one.

- Outcome:
    - Pass.

#### As a user I want to edit my Profile
- Requirements:
    - User is logged in.
    
- Steps: 
    1. Click on the "Profile" Button on the NavBar.
    2. Click on the "Edit Profile" Button.
    3. User is redirected to a Edit Profile form.
    4. The user now can update his Bio and Upload a picture.
    5. Submit Changes.
    6. User is redirected to his profile page.
    7. Success message is displayed and changes were made.

- Outcome:
    - Pass.

#### As a user I want to change my password Profile
- Requirements:
    - User is logged in.
    - Remember current password.

- Steps: 
    1. Click on the "Profile" Button on the NavBar.
    2. Click on the "Change Password" Button.
    3. User is redirected to Change Password form.
    4. Fill up the correct information.
    5. Submit Changes.
    6. User is redirected to his profile page.
    7. Success message is displayed and his password is now changed.

- Outcome:
    - Pass.

#### As a user I want to delete my account.
- Requirements:
    - User is logged in.

- Steps: 
    1. Click on the "Profile" Button on the NavBar.
    2. Click on the "Delete Account" Button.
    4. User is to a new page asking if he wants to delete his account.
    5. Click on the Delete Button.
    6. User is now redirected to the home page.
    7. Success message is displayed and this user no longer exist in the database and his post and comments were deleted too.

- Outcome:
    - Pass.

[Back to Table of contents](#table-of-contents)
## Deployment
- In order to Deploy this project:
    1. Either fork or clone this project.
    2. Heroku setup.
    3. Follow the [link](https://docs.google.com/document/d/1P5CWvS5cYalkQOLeQiijpSViDPogtKM7ZGyqK-yehhQ/edit) to set up your ide. Credit do Code Institute

### Forking

- In order to Fork this repository:

    1. Access your GitHub account and find the relevant repository.
    2. Click on 'Fork' on the top right of the page.
    3. You will find a copy of the repository in your own Github account.

### Clone

- In order to Clone this repository:

    1. Create repository where you will work with this clone.
    2. Copy "https://github.com/gioZAK/justblog.git".
    3. Run the directory you want the clone to be.
    6. In your IDE's terminal type 'git clone' and the paste the URL you just copied.
    7. Press Enter.
    8. You now have a local clone.

### Heroku.
-To setup with Heroku:

   1. Create an account at heroku.com
   2. Create a new app, add app name and your region
   3. Click on create app
   4. Go to "Settings"
   5. Under Config Vars, add your sensitive data (creds.json for example)
   6. Now go to your IDE and connect your enviroment with heroku
   7. heroku login -i
   8. Then run the following command: heroku git:remote -a your_app_name_here
   9. Finally: git push heroku main

### Follow the instructions here.
- Further instructions can be follow from [here](https://docs.google.com/document/d/1P5CWvS5cYalkQOLeQiijpSViDPogtKM7ZGyqK-yehhQ/edit)
    - All credits to Code Institute.


## Credits

### Code Institute
- I have relied on the Code Institute Django Blog Walktrough project in order to make my own.

### Corey Schafer
- [Corey Schafer Django Course](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)

### Django For Everybody - Full Python University Course
- [Django For Everybody - Full Python University Course](https://www.youtube.com/watch?v=o0XbHvKxw7Y&t)

### ChatGPT
- I have used [ChatGPT](https://chat.openai.com/chat) as a tool to debug and to guide me on how to apply new functionalities.

### Unsplash
- I have taken the images for the blog post from [Unsplash](https://unsplash.com/)

[Back to Table of contents](#table-of-contents)