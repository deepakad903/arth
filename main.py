import os
import getpass

print("\033[1;33;40m \t\t\t\t\t\t   Automation Menu  \n")


def runCommands(command, host=''):
    os.system(host+command)


def AwsSubMenu():
    print("Aws cli installed in")
    hasAwsCli = os.system('aws --version')
    if hasAwsCli != 0:
        print("\033[1;31;40mCannot Find AWS CLI\n")
        printMainMenu()
    else:
        commandDict = {
            1: 'configure',
            2: 'ec2 describe-instances',
            3: 'ec2 describe-key-pairs',
            4: 'ec2 create-key-pair',
            5: 'ec2 delete-key-pair',
            6: 'ec2 run-instances',
            7: 'ec2 create-volume',
            8: 'ec2 attach-volumme',
            9: ''
        }
        print(
            "\033[1;32;40mThis application assumes that aws cli is already configured. In case the cli is not configured, choose option 1 for the same")
        print("\033[1;37;40m1. Configure AWS CLI")
        print("2. View Running Instances")
        print("3. View Key pairs")
        print("4. Create a new key pair")
        print("5. Remove a Key pair")
        print("6. Create a new ec2 Instance")
        print("7. Create a new EBS Volume")
        print("8. Attach EBS Volume to an Instance")
        print("9. Create a new s3 Bucket")
        print("10. Go to main menu")
        choice = int(input("Enter Your Choice: "))
        if choice > 10:
            print("\033[1;31;40mInvalid Option. Try Again.")
            AwsSubMenu()
        elif choice == 10:
            printMainMenu()
        else:
            command = 'aws ' + commandDict[choice]
            if choice == 4:
                name = input("Enter the name of the key pair: ")
                command += " --key-name " + name + \
                    " --query 'KeyMaterial' --output text > " + name + ".pem"
            elif choice == 5:
                name = input("Enter the name of the key pair: ")
                command += " --key-name " + name
            elif choice == 6:
                imageId = input("Enter image id: ")
                instanceType = input("Enter the instance type: ")
                keyPairName = input("Enter Key Pair name: ")
                command += " --image-id " + imageId + " --instance-type " + \
                    instanceType + " --key-name " + keyPairName
            elif choice == 7:
                size = input("Enter size in GiB: ")
                command += " --size " + size
            elif choice == 8:
                volumeId = input("Enter volume id: ")
                instanceId = input("Enter value of instance id: ")
                command += " --volume-id " + volumeId + " --instance-id " + instanceId
            elif choice == 9:
                pass
            runCommands(command)
            AwsSubMenu()


def osSubMenu():
    commandDict = {
        2: 'date',
        3: 'cal',
        4: 'free -m',
        1: 'ps -aux'
    }
    print("Enter IP to work with")
    hostIP = input("Ip (Defaults to localhost): ")
    hostIP.strip()
    username = ''
    command = ''
    if not hostIP == '':
        print("Enter username")
        username = input("username (Defaults to root): ")
        if username == '':
            username = 'root'
        command += 'ssh {}@{}'.format(username, hostIP)
    else:
        print(
            "\033[1;32;40mThis machine will be assumed as host for OS commands")

    print("\033[1;37;40m1. Check Runinning Processes")
    print("2. Check Current Date")
    print("3. Run Cal command")
    print("4. Check Memory Usage")
    print("5. Run a custom command")
    print("6. Go to main menu")
    choice = int(input("Enter Your Choice: "))
    if choice > 6:
        print("\033[1;31;40mInvalid Option. Try Again.")
        osSubMenu()
    elif choice == 6:
        printMainMenu()
    else:
        if choice == 5:
            customCommand = input("Enter the command: ")
            command += customCommand
        else:
            command += commandDict[choice]
        runCommands(command)
        osSubMenu()


def dockerSubMenu():
    commandDict = {
        1: 'systemctl status docker',
        2: 'systemctl start docker',
        3: 'docker images',
        4: 'docker pull ',
        5: 'docker ps -a',
        6: 'dokcer run -it --name {} {}',
        7: 'docker start -i {} ',
        8: "docker exec {} sh -c 'yum install httpd -y && /usr/sbin/httpd' ",
        9: "docker exec {} sh -c 'yum install python3 -y'"
    }
    print("Enter IP to work with")
    hostIP = input("Ip (Defaults to localhost): ")
    hostIP.strip()
    username = ''
    command = ''
    if not hostIP == '':
        print("Enter username")
        username = input("username (Defaults to root): ")
        if username == '':
            username = 'root'
        command += 'ssh {}@{}'.format(username, hostIP)
    else:
        print(
            "\033[1;32;40mThis machine will be assumed as host for OS commands")

    print("\033[1;37;40m1. Check running status of Docker")
    print("2. Start Docker Services")
    print("3. List dokcer images")
    print("4. Pull a new Image")
    print("5. List all containers")
    print("6. Launch a new container")
    print("7. Login into a container")
    print("8. Configure apache web server in docker")
    print("9. Set up the container to run python code")
    print("10. Go to main menu")
    choice = int(input("Enter Your Choice: "))
    if choice > 10:
        print("\033[1;31;40mInvalid Option. Try Again.")
        osSubMenu()
    elif choice == 10:
        printMainMenu()
    else:
        if choice == 6:
            dokcerCommand = commandDict[6].format(
                input("Enter the name of os: "), input("Enter name of image: "))
            command += dokcerCommand
        elif choice == 7 or choice == 8 or choice == 9:
            dokcerCommand = commandDict[7].format(
                input("Enter name/id of container: "))
            command += dokcerCommand
        else:
            command += commandDict[choice]
        runCommands(command)
        dockerSubMenu()


def apacheSubMenu():
    commandDict = {
        1: 'yum install httpd -y',
        2: 'systemctl start httpd',
        3: 'systemctl status httpd'
    }
    print("Enter IP to work with")
    hostIP = input("Ip (Defaults to localhost): ")
    hostIP.strip()
    username = ''
    command = ''
    if not hostIP == '':
        print("Enter username")
        username = input("username (Defaults to root): ")
        if username == '':
            username = 'root'
        command += 'ssh {}@{}'.format(username, hostIP)
    else:
        print(
            "\033[1;32;40mThis machine will be assumed as host for OS commands")

    print("\033[1;37;40m1. Install Apache httpd server")
    print("2. Start the httpd server")
    print("3. check status of web server")
    print("4. Go to main menu")
    choice = int(input("Enter Your Choice: "))
    if choice > 4:
        print("\033[1;31;40mInvalid Option. Try Again.")
        osSubMenu()
    elif choice == 4:
        printMainMenu()
    else:
        command += commandDict[choice]
        runCommands(command)
        apacheSubMenu()


def mapToSubMenu(choice):
    if choice == 1:
        AwsSubMenu()
    elif choice == 2:
        dockerSubMenu()
    elif choice == 3:
        osSubMenu()
    else:
        apacheSubMenu()


def printMainMenu():
    print("\033[1;32;40mEnter Your choice. This menu will lead to different submenu depending on the choice make.")
    print("\033[1;37;40m1. AWS")
    print("2. Docker")
    print("3. OS Commands")
    print("4. Apache Web Server")
    print("5. Exit")
    choice = int(input("Enter Your Choice: "))
    if choice > 5:
        print("\033[1;31;40mInvalid Option. Try Again.")
        printMainMenu()
    elif choice == 5:
        pass
    else:
        mapToSubMenu(choice)


try:
    printMainMenu()
except:
    print("\033[1;31;40mAn Error Occured\n")
