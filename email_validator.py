email=input("Enter the email:") #g@g.com
k,s,d=0,0,0
if len(email)>7 and email[0]!=email.isalnum():
    if (email[-4]=="." and email[-1:-4:-1]=="moc") or  (email[-1:-3:-1]=="in" and email[-2]=="ni"):
        if email.count('@')==1 and email.lower():
            for i in email:
                if i==i.isspace():
                    k=1
                elif i==i.isalpha():
                    if i==i.upper():
                        s=1
                elif i==i.isdigit():
                    continue
                elif i=="@" or i=="_" or i==".":
                    continue
                else:
                    d=1
            if k==1 or s==1:
                print("Email is not valid") 
            else:
                print("Valid email")       
        else:
            print("Email  not valid")
    else:
        print("Email not valid")  
 
else:
    print("Email not valid")    