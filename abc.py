from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from pandas import read_csv
import csv
from sklearn.datasets import load_iris
#filepath = input("Enter the path of the file")
#categorical=['Gender','Married','Dependents','Education','Self_Employed','Credit_History','Property_Area']
#scalable=['Loan_ID','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term']
filepath="C:\\Users\\Shadhrush\\Desktop\\New folder\\loan_prediction\\"
filez =input("Enter your file path")
#filez=load_iris()
X_test=read_csv(filez)
j=0
lines = csv.reader(open(filez, 'r'), delimiter=',')
num_cols = len(next(lines))
#print(num_cols)
categorical=[]
scalable=[]
with open(filez, 'r') as f: #using this to access only the headings of the csv file
    for row in f:
        while(j<num_cols):
            a=0
            b=0
            c=0 #initialising inside the while so that it repeats becoming 0 after moving to a different column each time
            d=0
            if(j==num_cols-1):
                second_data = row.split(',')[j]
                second_data=second_data[:len(second_data)-1]
                #print(second_data)
                for i in X_test[second_data]:
                    if(type(i)==str and i.replace(" ", "").isalpha() or (str(i).isnumeric() and int(i)<5)):
                        c=c+1
                        if(c==50):
                            categorical.append(second_data)
                            
                    elif(str(i).replace(".", "").isnumeric()): #replacing the point since isnumeric returns false for floating point
                        a=a+1
                        if(a==1):
                            scalable.append(second_data)
                    else:
                        continue        
                #print(X_test[second_data])
            else:
                second_data = row.split(',')[j]        
                #print(second_data)
                for i in X_test[second_data]:
                    if(type(i)==str and i.replace(" ", "").isalpha() or (str(i).isnumeric() and int(i)<5)):                       
                        d=d+1
                        if(d==50):
                            categorical.append(second_data)
                    elif(str(i).replace(".", "").isnumeric()):
                        b=b+1
                        if(b==1):
                            scalable.append(second_data)
                    else:
                        continue
                        
                #print(X_test[second_data])
            j=j+1
print("The scalable attributes are")
print("\n")
print(scalable)
print("\n")
print("The categorical attributes are")
print("\n")
print(categorical)
            
            
'''
print(X_test)
print(X_test['Gender'])
c=0
 for i in X_test[j]:
    if(type(i)==str):
        #print(i)
        c=c+1
        if(c==3):
            new_categorical.append(j)
            break()
    else:
        new_scalable.append(j)
#print(c)
'''
