import libxml2
import sys

'''
purpose
	return the course mark for student s
preconditions
	student is a list of the form:
		[last_name, first_name, student_id, marks]
		where
		marks is a list of the form: [ [assignment_id,score], ... ]
	assignments is a dictionary of the form:
		{mark_id:[points, percentage], ... }
'''
def compute_mark(student, assignments):
	l,f,sid,marks=student
	total=0.0
	for aid,sc in marks:
		sc=int(sc)
		points,perc=assignments[aid]
		total+= sc/float(points)*perc
	return total	

	# pass # REPLACE THIS LINE WITH YOUR IMPLEMENTATION

'''
purpose
	extract the information from a and return it as a list:
		[mark_id, points, percentage]
preconditions
	s is an assignment element from a legal students XML file
'''
def extract_assignment(a):
	info=[0,0,0]
	while a:
		if a.name=='mark_id':
			#print repr(str(a))
			a0=a.children
			info[0]=str(a0)
		elif a.name=='points':
			a0=a.children
			info[1]=int(str(a0))
		elif a.name=='percentage':
			a0=a.children
			info[2]=float(str(a0))
		a=a.next
	return info
#	pass # REPLACE THIS LINE WITH YOUR IMPLEMENTATION

'''
purpose
	extract the information from s and return it as a list:
		[last_name, first_name, student_id, marks]
		where
		marks is a list of the form: [ [assignment_id,score], ... ]
preconditions
	s is a student element from a legal students XML file
'''
def extract_student(s):
	info=[0]*4
	while s:
		s0=s.children
		if s.name=='first_name':
			info[1]=str(s0)
		elif s.name=='last_name':
			info[0]=str(s0)
		elif s.name=='student_id':
			info[2]=str(s0)
		elif s.name=='marks':
			info[3]=[]
			while s0:
				s1=s0.children
				if s0.name=='mark':
					m=[0,0]
					while s1:
						s2=s1.children
						if s1.name=='mark_id':
							m[0]=str(s2)
						elif s1.name=='score':
							m[1]=int(str(s2))
						s1=s1.next
					info[3].append(m)
				s0=s0.next
				
		s=s.next
	return info
	#pass # REPLACE THIS LINE WITH YOUR IMPLEMENTATION
