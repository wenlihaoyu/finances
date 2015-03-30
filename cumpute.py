import pandas,random
class order:
    def __init__(self,n=100):
       self.n=n
    def get_date(self):
        self.date=list(range(self.n))
    def get_strategy(self):
        self.strategy=[random.choice(['sell','buy','sell']) for i in range(self.n)]
    def get_num(self):
        self.num=[int(random.uniform(1,10))*100 for i in range(self.n)]
    def get_price(self):
        self.price=[int(random.uniform(7,10)) for i in range(self.n)]
    def get_data(self):
        self.get_date()
        self.get_num()
        self.get_strategy()
        self.get_price()
        self.data=[ [self.date[i],self.price[i],self.num[i],self.strategy[i]] for i in range(self.n)]
    def DataFrame(self,data):
        return(pandas.DataFrame(data))
def cumpute(data):
        i=0
        j=0
        m_average=0
        m_total=0
        m_data=data
        while (i<=len(m_data)-1 and j<=len(m_data)-1):
            ## find the next lable is buy
            while m_data[i][3]=="sell" and i<=len(m_data)-1:
                i+=1
                if i==len(m_data):
                    break
            ## find the next lable is sell
            while m_data[j][3]=="buy" and j<=len(m_data)-1:
                j+=1
                if j==len(m_data):
                    break
            if i <len(m_data) and j< len(m_data):    
                if m_data[i][2]>m_data[j][2]:
                    m_average+=m_data[j][2]*(m_data[j][1]-m_data[i][1])
                    m_total+=m_data[j][2]
                    m_data[i][2]-=m_data[j][2]
                    j+=1
                
                elif m_data[i][2]<m_data[j][2]:
                    m_average+=m_data[i][2]*(m_data[j][1]-m_data[i][1])
                    m_total+=m_data[i][2]
                    m_data[j][2]-=m_data[i][2]
                    i+=1
                else:
                    m_average+=m_data[i][2]*(m_data[j][1]-m_data[i][1])
                    m_total+=m_data[i][2]
                    i+=1
                    j+=1
        #print m_average
        #print m_total
        return  m_average/1.0/m_total 
        
        
        