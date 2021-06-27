# Job-Tracking

- In this project I have collected data related to `Job advertisement` from a website using `web scrapping `
- And I will send the latest information through `Gmail`
- URL of the website : [Link](https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=) 

### Libraries or Packages Used :
- beautifulsoup4
- lxml
- requests
- smtplib
- ssl
- email

### Set up
- Create a new Gmail account [ For safety Purpose ] and "Turn Allow less secure apps to ON" in account settings. Be aware that this makes it easier for others to gain access to your account. 
- Instead of creating new Gmail account, you can give access to less secure apps for your present Gmail account before running the code & later turn off the access.

### How it works ?
- User need to provide his gmail credentials.
- In the next step user need to provide the skills which are unfamiliar to him.
- There few options to user, like
  - To run the code only once [ i.e to extract the data only once ].
  - Or to run the code continuosly to update the data after few minutes.
- Next our code processes and extract the data from the website.
- Once the data is extracted we save it in a '.txt' file [ Company Name, Required Skills etc... ].
- Finally we send the '.txt' file through email.

#### Screenshot of the data : [Link](/images/img_1.png)

![](https://github.com/giridhar04/Job-Tracking/blob/main/images/img_1.png)

#### Screenshot of Email : [Link](/images/img_2.png)

![](https://github.com/giridhar04/Job-Tracking/blob/main/images/img_2.png)

### Important Links :
- https://www.freecodecamp.org/news/send-emails-using-code-4fcea9df63f/ 
- https://realpython.com/python-send-email/ 
- https://youtu.be/XVv6mJpFOb0
