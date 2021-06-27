"""
Before running this code please make sure you have following packages
1) beautifulsoup4
2) requests
3) lxml

Url of the website : https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=
"""

from webScrapping import filter_jobs
from sendMail import sendMail
import time

if __name__ == '__main__':

    print("""\
    Note : Turn Allow less secure apps to ON in your google account.
    Be aware that this makes it easier for others to gain access to your account.
    Turn off the feature once you finished working with this code...
    """)

    print("Enter your Google mail Id : ")
    gmailId = input('>')
    print("Enter your password for Gmail Id : ")
    password = input('>')

    print("\nPlease provide some un-familiar skills in the below mentioned format... : ")
    print('sql,linux')
    #Eg: sql,linux,java
    unfamiliar_skills=input('>').split(',')

    print("\nChoose one option :")
    print('1) Do you want the code to run once and stop :')
    print('2) Or do you want the code to run continuously to extract the latest updates :')
    option=int(input())

    if option==1:
        print("\nFiltering out unfamiliar skills...\n")
        # Clear the previous Job details file
        open('Posts/Jobs_Details.txt', 'w').close()
        filter_jobs(unfamiliar_skills)
        sendMail(gmailId, password)
    elif option==2:
        wait_time=int(input("\nPlease enter the waiting time in minutes : "))
        print("Filtering out unfamiliar skills...\n")
        # Here We are running a infinite loop so that we can get latest information
        while True:
            # Clear the previous Job details file
            open('Posts/Jobs_Details.txt', 'w').close()
            filter_jobs(unfamiliar_skills)
            sendMail()
            # Choose the waiting time to get the latest information
            print('')
            print(f'Waiting {wait_time} minutes...\n')
            time.sleep(wait_time * 60)
    else:
        print("Please choose from above options :(\n")


    

    


