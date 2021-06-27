from bs4 import BeautifulSoup
import requests



def filter_jobs(unfamiliar_skills):
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    #print(html_text)
    soup=BeautifulSoup(html_text,'lxml')
    #print(soup)

    #All the jobs are present with <li> tag in unordered list with class='clearfix job-bx wht-shd-bx'
    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    #print(jobs)

    for job in jobs:
        #Published date is present in the tag <span> with class 'sim-posted'
        published_date=job.find('span',class_='sim-posted').text

        #I want to extract the details of the job which has posted notification only few days earlier
        #So the published date will be like "Posted few days ago"
        if 'few' in published_date:
            company_name=job.find('h3',class_='joblist-comp-name').text.strip()
            #print(company_name)
            skills=job.find('span',class_='srp-skills').text.strip().replace('  ',' ')
            #print(skills)
            more_info=job.find('header',class_='clearfix').a['href']
            #print(more_info)

            flag=1
            for unfamiliar_skill in unfamiliar_skills:
                if unfamiliar_skill in skills:
                    flag=0
                    break

            if flag==1:

                #Uncomment below code if you want to see the output on terminal
                '''
                print(f'Company Name : {company_name}')
                print(f'Required Skills : {skills}')
                print(f'More Information : {more_info}')
                print('')
                '''
                with open('Posts/Jobs_Details.txt','a') as f:
                    f.write(f"Company Name : {company_name} \n")
                    f.write(f"Required Skills : {skills}\n")
                    f.write(f"More Information : {more_info}\n")
                    f.write("\n\n")

    print('File Saved....')
