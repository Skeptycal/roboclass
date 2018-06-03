import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class Client(object):

	# use creds to create a client to interact with the Google Drive API
	scope = ['https://spreadsheets.google.com/feeds',  'https://www.googleapis.com/auth/drive' ]
	creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
	client = gspread.authorize(creds)
	# find a Google spreadshit by name, which will be used instead of a database
	db = client.open("roboclass")
 
class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'sdkjfbkbbt45hktbkhbkvqdb8r8e'