

def fun5():
        import pandas as pd
        import matplotlib.pyplot as plt



        labels = '2017',' '
        # sizes=5,6,7,8
        sizes = 1366056,0
        colors = 'lightskyblue',  'lightcoral'
        explode = 0.1,0.1
        plt.pie(sizes, explode=explode, labels=labels,
                colors=colors, autopct='%1.1f%%', shadow=True, startangle=50)
        plt.axis('equal')
        plt.show()


def fun4():
        #user	time_stamp	adgroup_id	pid	nonclk	clk
        df=pd.read_csv('raw_sample.csv')
        #print(df)
        #df=df[]
        df=df[df['clk']==1]
        df['time_stamp'] = pd.to_datetime(df['time_stamp'], unit='s', origin=pd.Timestamp('1970-01-01 9:00:00'))
        #dfyear=df.groupby(df['time_stamp'].dt.year).count()
        dff=df.head(20)
        print(dff)
        dffhour=dff.groupby(dff['time_stamp'].dt.hour).count()
        print(dffhour)
        #dfmonth=df.groupby(df['time_stamp'].dt.month)
        dfhour=df.groupby(df['time_stamp'].dt.hour).count()
        print(dfhour)
        print(dfhour['clk'])
        labels = [x for x in range(24)]#dfhour['time_stamp']
        plt.xticks(range(len(labels)), labels)
        plt.xlabel('clock (hour)')
        plt.ylabel('click time')
        plt.bar(range(len(labels)), dfhour['clk'], color='lightskyblue')
        plt.show()

        #(dfyear['user'].unstack()).plot(kind='bar', rot='0')
        #plt.show()


def fun3():
        #plt.rcParams['font.sans-serif']=['SimHei']
        #df=pd.read_csv('ad_feature.csv')
        df=pd.read_csv('user_profile.csv')
        #df=df.fillna(4)
        df=df.dropna()
        sex=['1_male','2_female']
        df['final_gender_code']=df['final_gender_code'].map(lambda x:sex[x-1])
        print(df['pvalue_level'])
        pvalue=['1_low','2_medium','3_high']
        df['pvalue_level']=df['pvalue_level'].map(lambda x:pvalue[int(x-1)])
        df['shopping_level']=df['shopping_level'].map(lambda x:pvalue[int(x-1)])
        occupy=['1_university_student','2_not_university_student']
        df['occupation']=df['occupation'].map(lambda x:occupy[int(1-x)])
        classlevel=['tier 1 cities','tier 2 cities','tier 3 cities','tier 4 cities']
        df['new_user_class_level ']=df['new_user_class_level '].map(lambda x:classlevel[int(x-1)])
        #print(df)
        #userid	final_gender_code	age_level	pvalue_level	shopping_level	occupation	new_user_class_level
        group11=df.groupby(by=['new_user_class_level ','pvalue_level']).count()

        (group11['userid'].unstack()).plot(kind='bar',rot='0')
        plt.show()



def fun2():
        p1=[0]*10
        for price in prices:
                if price<100:
                        #print(price)
                        #print(int(price/10))
                        p1[int(price/10)]+=1

        p=[0]*10
        for price in prices:
                if price<1000:
                        #print(price)
                        #print(int(price/100))
                        p[int(price/100)]+=1
        labels=['<1','1-2','2-3','3-4','4-5','5-6','6-7','7-8','8-9','9-10']
        plt.xticks(range(len(labels)), labels)
        plt.xlabel('Price (*10)')
        plt.ylabel('Amounts ')
        plt.bar(range(len(labels)),p1,color='lightskyblue')
        plt.show()



def fun1():
        prices=df['price']
        print(len(prices))


        p1to100=0
        p100to1000=0
        p1000to10000=0
        p1e8=0

        for price in prices:
                if price<100:
                       p1to100+=1
                elif price<500:
                        p100to1000+=1
                elif price<1000:
                        p1000to10000+=1
                else:
                        p1e8 += 1

        labels='<100','100-500','500-1000','>1000'
        #sizes=5,6,7,8
        sizes=p1to100,p100to1000,p1000to10000,p1e8
        colors='lightgreen','gold','lightskyblue','lightcoral'
        explode=0.1,0.1,0.1,0.1
        plt.pie(sizes,explode=explode,labels=labels,
                colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)
        plt.axis('equal')
        plt.show()

if __name__ == '__main__':
        import pandas as pd
        import matplotlib.pyplot as plt
        fun4()