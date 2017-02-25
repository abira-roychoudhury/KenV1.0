from random import randint
import logging

def LawFind(parameters):
	logging.info("LawFind")

	if parameters["LawType"] : 

		speech = {"Environment" : "H.R.861 To terminate the Environmental Protection Agency.",
			"Immigration" : "S.2266 H1B and L1 Visa Reform Act of 2015.",
			"Health Care" : "H.R.285 Healthcare Tax Relief and Mandate Repeal Act."}
		response = ""

		for law in parameters["LawType"]:
			response = response + " This is what I found about "+str(law)+" : "+str(speech[law])
			LawId = 123
	
	else:

		speech = ["H.R.861 To terminate the Enviornmental Protection Agency.","S.2266 H1B and L1 Visa Reform Act of 2015.","H.R.285 Healthcare Tax Relief and Mandate Repeal Act."]
		response = speech[randint(0,2)]

	return {"response":response+" Do you want more information about this law?", "contextOut":[{"name":"UserAnswer","lifespan":10, "parameters":{"LawId" : LawId }}]}

def LawMoreInformation(parameters):
	logging.info("inside LawMoreInformation")

	if parameters["MoreInfo"] == "yes":
		#fetch more info
		response = "fetch more info from DB."
	else:
		response = ""

	#check DB for more laws 

	if True:#laws exists:
		response = response + " Do you want to see some more laws." 
		contextOut = [{"name":"MoreLaw", "lifespan" : 10, "parameters" : {"LawId" : parameters["LawId"]} }]
	else:
		response = "Thank you" #stop conversation
		contextOut = []

	return {"response":response, "contextOut":contextOut}


def MoreLaw(parameters):
	logging.info("inside NextLaw")

	CurrentLawId = parameters["LawId"]

	#fetch next law 
	LawId = 123 #next laws Id

	response = "Here is next Law."
	
	return {"response":response+" Do you want more information about this law?", "contextOut":[{"name":"UserAnswer","lifespan":10, "parameters":{"LawId":LawId}}]}

	
handler = {
	"LawFind" : LawFind,
	"LawMoreInformation" : LawMoreInformation,
	"MoreLaw" : MoreLaw
}
