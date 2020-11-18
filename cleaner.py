import pickle,os
dbfile = open('this file', 'rb')      
db = pickle.load(dbfile)
#print(db)
 
dbfile.close() 
import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','cookbook.settings')
import django
# Import settings
django.setup()
from recipes import models
def add_cuisines(string):
    t = models.cuisines.objects.get_or_create(cuisine_name=string)[0]
    t.save()
    return t
def add_recipes(a,b,c,d,e,f='default.jpg'):
    t = models.recipe.objects.get_or_create(cuisine_name=a,
                                             name=b,
                                             ingredients=c,
                                             method=d,
                                             time=e,
                                             image=f)[0]
    t.save()
    return t
print(db['Cuisines']['African'][9])
db=db['Cuisines']
p=[]
s=os.listdir('.')
for i in s:
    if '.jpg'in i:
        p.append(i[:len(i)-4])
#print(p)        
#'''
for keys in db:
    print (keys)
    a=add_cuisines(keys)

    for i in db[keys]:
        print(i)
        if str(i['count'])in p:
            print(('a',i['name'],i['Ingredients'][12:],i['Method'][7:],i['Time'],str(i['count'])+'.jpg'))
            add_recipes(a,i['name'],i['Ingredients'][12:],i['Method'][7:],i['Time'],str(i['count'])+'.jpg')
        else:
            print(('a',i['name'],i['Ingredients'][12:],i['Method'][7:],i['Time']))
            add_recipes(a,i['name'],i['Ingredients'][12:],i['Method'][7:],i['Time'])




        
#'''
