import numpy as np
from pathlib import Path
import win32com.client
import model

emailFolder = Path.cwd() / "emails"
emailFolder.mkdir(parents=True, exist_ok=True)

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

# Microsofts docs label inbox as 6
inbox = outlook.GetDefaultFolder(6)

emails = inbox.Items
spamFilter,vectorizor = model.makefilter()

targetSpam = emailFolder / "spam"
targetSpam.mkdir(parents=True, exist_ok=True)

targetHam = emailFolder / "ham"
targetHam.mkdir(parents=True, exist_ok=True)
for email in emails:
    try: 
        text = (str(email.Subject) + " " + str(email.body))
        spam = spamFilter.predict(vectorizor.transform([text]))
        if spam:
            Path(targetSpam / str(email.Subject)).write_text(str(email.body))
            #email.Attachments.SaveAsFile(targetSpam / str(email.Attachments))
        else:
            Path(targetHam / str(email.Subject)).write_text(str(email.body))
            #email.Attachments.SaveAsFile(targetHam / str(email.Attachments))
    except:
        pass