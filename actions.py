from random import randint
import logging

def LawFind(parameters):

	speech = ["H.R.861 To terminate the Enviornmental Protection Agency.","S.2266 H1B and L1 Visa Reform Act of 2015.","H.R.285 Healthcare Tax Relief and Mandate Repeal Act."]

	return {"response":speech[randint(0,2)], "contextOut":[{}]}


def LawFindByKeyWord(parameters):
	speech = {"Environment" : "H.R.861 To terminate the Environmental Protection Agency.",
			"Immigration" : "S.2266 H1B and L1 Visa Reform Act of 2015.",
			"Health Care" : "H.R.285 Healthcare Tax Relief and Mandate Repeal Act."}

	response = ""

	for law in parameters["LawType"]:
		response = response + "This is what I found about "+str(law)+" : "+str(speech[law])

	return {"response":response + "Do you want to hear more details?", "contextOut":[{"name":"userAnswer","lifespan":10, "parameters":{"lawid":123}}]}
	
def LawMoreInformation(parameters):
	logging.info(parameters)
	return {"response":"here is more information", "contextOut":[{}]}
	
handler = {
	"LawFind" : LawFind,
	"LawFindByKeyWord" : LawFindByKeyWord,
	"LawMoreInformation" : LawMoreInformation
}
