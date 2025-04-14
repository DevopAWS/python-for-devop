global inforamtion tracking (git) system

version control ---> 

we should always go back to previous version if something goes wrong

track the changes--->through git we can understand who didthat and why

review the chaanges --> our team members should br review

git ::::::::::::::>>>>>>
 
git repo---> store the code

repository ---------> some storage just like a folder with some extra capabilities

push ----> authenetcation 

username/pasword -----> every time or frequently asked username and password

username/key->>>>>> one stime setup (it will be automatically taken from the private key)

key ---> public key shoulb be stored in server like git
	 private key should be stored in our laptop (locally)


key genaraion >>>>>>>>>>>>>>>

open git bash and type as ssh-keygen -f <key-name> <daws-76s-github>
enter,enter

cat dwas-76s-github.pub  enter


copy public-key and goto github account under setting select ssh and GPG Keys
select new ssh key
titel as MyWindowsLaptop
paste the key in box and add sshkey

goto c drive and next to user then automatically create a .ssh folder 
if .ssh foler is not created you can createe as well
	in .ssh folder one file is there i.e config (no extension to this file) all small letters in config

    if any extension is there goto contorol pannel and select file explorer option
    and click view ,then unclick the hide extensions for known file types 
    apply and ok 


http -----> http:/github.com/....... >>>>>username/password
ssh ----->   git/github.com: ...........>>>just private key

google search ---> git ssh config syntax

in config file paste this synatx and save it

Host gitlab.com
    HostName gitlab.com
    User git
    PreferredAuthentications publickey
    IdentityFile ~/<private-keyname> like daws-76s-github

private key as under c drive user ---> daws-76s-github  (privte key name)

first time git bash opend you must applied username and mailid like

git config --global user.name "suresh"
git config --global user.email "info@email.com"

above error comes commit the code without credtials this is one time job 


   






