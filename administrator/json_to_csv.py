# select * from mantis_config_table where config_id = "plugin_EmailReporting_mailboxes"; 

import json

with open("email_list.json", "r", encoding="utf-8") as File_e:
    obj_email = json.load(File_e)

for i in range(1,100):
    conv_i = str(i)
    try: 
        if conv_i in obj_email:
            Email = obj_email[conv_i]["erp_username"]
            Password = obj_email[conv_i]["erp_password"]
            Project = obj_email[conv_i]["project_id"]
            print(f"Email: {Email}\nPassword: {Password}\nProject: {Project}")
    except:
        print("THERE IS EXCEPTION:") 
