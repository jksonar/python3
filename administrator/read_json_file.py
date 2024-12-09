# select * from mantis_config_table where config_id = "plugin_EmailReporting_mailboxes"; 

import json

with open("email_list.json", "r", encoding="utf-8") as File_e:
    obj_email = json.load(File_e)
    print(json.dumps(obj_email, indent=4,sort_keys=True))