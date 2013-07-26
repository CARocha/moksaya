import gdata.docs.service
import getpass
import android

app = android.Android()

client = gdata.docs.service.DocsService()
user = "rahul.nbg@gmail.com"
pw = "gottagotode20"

client.ClientLogin(user,pw)
documents_feed = client.GetDocumentListFeed()
document_list = [""]
for document_entry in documents_feed.entry:
  #print document_entry.title.text
  
  document_list.append(document_entry.title.text)
print document_list,   
app.dialogSetSingleChoiceItems(document_list)
app.dialogSetPositiveButtonText("Okay! ")
app.dialogSetNegativeButtonText("Bitch please!")
app.dialogShow()
result= app.dialogGetResonse().result
app.vibrate()
app.makeToast("Nailed it!")
