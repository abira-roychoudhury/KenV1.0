
def LawFind(parameters):

	speech = ["H.R.861 To terminate the Enviornmental Protection Agency.","S.2266 H1B and L1 Visa Reform Act of 2015.","H.R.285 Healthcare Tax Relief and Mandate Repeal Act."]

	return speech[randint(0,2)] 


def LawFindByKeyWord(parameters):
	speech = {"Environment" : "H.R.861 To terminate the Environmental Protection Agency.",
			"Immigration" : "S.2266 H1B and L1 Visa Reform Act of 2015.",
			"Health Care" : "H.R.285 Healthcare Tax Relief and Mandate Repeal Act."}

	return "This is what I found about "+str(parameters["LawType"])+" : "+str(speech[str(parameters["LawType"])])

handler = {
	"LawFind" : LawFind,
	"LawFindByKeyWord" : LawFindByKeyWord 
}