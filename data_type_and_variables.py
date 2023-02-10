little_mermaid = 3 
brother_bear = 5 
hercules = 1




(little_mermaid + brother_bear + hercules) * 3 


#print((little_mermaid + brother_bear + hercules) * 3 )



def hours_worked():
	google = int(input('How many hours did you work at Google'))
	amazon = int(input('How many hours did you work at Amazon'))
	facebook = int(input('How many hours did you work at Facebook'))
	total_amount = (google * 400) + (amazon * 380) + (facebook * 350)
	print(f'Look at you go! this week you will make ${total_amount}')

hours_worked()
