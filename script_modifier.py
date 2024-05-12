import subprocess
from code_generator import *



file_path = 'script_to_modify.py'

for i in range(random.randint(3,6)):
    insert_content_at_line(file_path, random.randint(5,15), generate_df_code_line())
    
    


subprocess.call(["/usr/bin/git", "add", "script_to_modify.py"])
subprocess.call(["/usr/bin/git", "commit", "-m", commit_message_generator()])
subprocess.call(["/usr/bin/git", "push"])
