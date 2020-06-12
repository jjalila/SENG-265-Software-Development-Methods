import libxml2
import sys

'''
purpose
	store the information from an answer element
'''
class Answer:
	def __init__(self, index, path, result, answer, time):
		self.index = index
		self.path = path
		self.result = result
		self.answer = answer
		self.time = time

'''
purpose
	Store the information from a display element.
'''
class Display:
	def __init__(self, index, path, time):
		self.index = index
		self.path = path
		self.time = time

'''
purpose
	Extract the information from log_file and return it as a list
	of answer and display objects.
preconditions
	log_file is the name of a legal, readable quiz log XML file
'''
def load_quiz_log(log_file):
	tree=libxml2.parseFile(log_file)
	quiz=tree.getRootElement().children
	ls=[]
	obj=None
	while quiz:
		if quiz.name=='answer':
			attrs=quiz.children
			index, path, result, answer, time = [None]*5
			while attrs:
				if attrs.name=='index':
					index=int(str(attrs.children))
				elif attrs.name=='path':
					path=str(attrs.children)
				elif attrs.name=='result':
					result=str(attrs.children)
					#print >> sys.stderr, result
					if result!='None': # result is not all white spaces
						result=int(result)
				elif attrs.name=='answer':
					answer=str(attrs.children)
				elif attrs.name=='time':
					time=str(attrs.children)
					if time!='None':
						time=int(time)
				attrs=attrs.next
			ls.append(Answer(index, path, result, answer, time))
		elif quiz.name=='display':
			attrs=quiz.children
			index, path, time=[None]*3
			while attrs:
				if attrs.name=='index':
					index=int(str(attrs.children))
				elif attrs.name=='path':
					path=str(attrs.children)
				elif attrs.name=='time':
					time=str(attrs.children)
					if time!='None':
						time=int(time)
				attrs=attrs.next
			ls.append(Display(index,path,time))
		quiz=quiz.next
	return ls


'''
purpose
	Return the number of distinct questions in log_list.
preconditions
	log_list was returned by load_quiz_log
'''
def compute_question_count(log_list):
	count=0
	for el in log_list:
		if isinstance(el,Answer) and type(el.result)!=int:
			count+=1
	return count

'''
purpose
	Extract the list of marks.
	For each index value, use the result from the last non-empty answer,
	or 0 if there are no non-empty results.
preconditions
	log_list was returned by load_quiz_log
'''
def compute_mark_list(log_list):
	ans=[0]*compute_question_count(log_list)
	for el in log_list:
		if isinstance(el,Answer) and el.result!='None':
			ans[el.index]=el.result
	return ans
