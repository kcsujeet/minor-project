from  numpy import *
from .models import Item

#gets all the data from the database

data_set = Item.objects.all()
data_setnew = []
data_setold=[]
n=0
m=0
# separates the category
def sep_cat():
    num_item = 10
    for i in range(num_item):
        if data_set[i].status== 'Brand New':
            data_setnew[i]=data_set[i]
            n=n+1
        else:
            data_setold[i]=data_set[i]


for i in data_setnew:
    pass









