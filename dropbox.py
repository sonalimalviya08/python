import dropbox
class transferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def uploadFile(self,file_from,file_to):
        #upload a file to dropbox using API #
        dbx=dropbox.Dropbox(self.access_token)
        with open(file_from,'rb') as f:
            dbx.files_upload(f.read(),file_to)
            
    