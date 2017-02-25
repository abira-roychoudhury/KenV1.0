from random import randint
import logging
from flask import session

def LawFind(parameters, db):
	logging.info("LawFind")

	#from dict of lawa fetched from DB 
	cursor = db.cursor()

	logging.info("cursor built in LawFind")

	if session["profile_json"]:
		logging.info(str(session["profile_json"]))

	LawId = 123
	speech = ["H.R.861 To terminate the Enviornmental Protection Agency.","S.2266 H1B and L1 Visa Reform Act of 2015.","H.R.285 Healthcare Tax Relief and Mandate Repeal Act."]
	response = speech[randint(0,2)]

	logging.info("response from LawFind: "+response)
	return {"response":response+" Do you want more information about this law?", "contextOut":[{"name":"UserAnswer","lifespan":10, "parameters":{"LawId" : LawId }}]}

def LawMoreInformation(parameters, db):
	logging.info("inside LawMoreInformation")

	if parameters["MoreInfo"] == "yes":
		#fetch more info
		response = "fetch more info from DB."
	else:
		#set to not useful
		response = ""

	#check DB for more laws 

	if True:#laws exists:
		response = response + " Do you want to see some more laws." 
		contextOut = [{"name":"MoreLaw", "lifespan" : 1, "parameters" : {"LawId" : parameters["LawId"]} }]
	else:
		response = "Thank you" #stop conversation
		contextOut = []

	logging.info("response from LawMoreInformation: "+response)

	return {"response":response, "contextOut":contextOut}


def MoreLaw(parameters, db):
	logging.info("inside NextLaw")

	CurrentLawId = parameters["LawId"]

	#fetch next law 
	LawId = 123 #next laws Id

	response = "Here is next Law."

	logging.info("response from MoreLaw: "+response)	
	return {"response":response+" Do you want more information about this law?", "contextOut":[{"name":"UserAnswer","lifespan":1, "parameters":{"LawId":LawId}}]}

	
handler = {
	"LawFind" : LawFind,
	"LawMoreInformation" : LawMoreInformation,
	"MoreLaw" : MoreLaw
}
