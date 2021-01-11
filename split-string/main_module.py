from main_file import emailProcess, printMsg

def main():
    emails = ['khai.to@holistics.io', 'deptrai@salesforce.com', 'ahihi@khai.to']
    for email in emails:
        email_username, email_domain = emailProcess(email) 
        printMsg(email_username, email_domain)

if __name__ == "__main__":
    main()