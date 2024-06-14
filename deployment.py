import subprocess   #This is used to run the terminal commands in python 
import os           #This is used for interacting os with the python program ex:- create dir
import sys

def install_schemchange():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade" , "pip"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "schemachange"])
    print("Installed all the dependencies")

def run_schemachange():
    command = (
        f"schemachange -f "
        f"{os.getenv('PROJECT_FOLDER')}/Fasttrack/SQL "
        f"-a {os.getenv('SF_ACCOUNT')} "
        f"-u {os.getenv('SF_USERNAME')} "
        f"-r {os.getenv('SF_ROLE')} "
        f"-w {os.getenv('SF_WAREHOUSE')} "
        f"-d {os.getenv('SF_DATABASE')} "
        f"-c {os.getenv('SF_DATABASE')}.SCHEMACHANGE.CHANGE_HISTORY "
        f"--create-change-history-table "
    )
    print(f"Command is prepared = ${command}")
    print(command)

    result = subprocess.run(command, shell=True, check=True)
    return result

if __name__ == "__main__":
    install_schemchange()
    run_schemachange()
