from main_file import emailProcess, printMsg

def main():
    emails = ['acb@gmail.com', 'hohaha@admin.com', 'ahihi@khai.to']
    for email in emails:
        email_username, email_domain = emailProcess(email) 
        printMsg(email_username, email_domain)

if __name__ == "__main__":
    main()