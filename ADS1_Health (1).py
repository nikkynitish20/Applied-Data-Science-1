import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns



def  plot_Scatter(df):
    """
    This function creates a scatter plot to observe the relation 
    between Sleep Duration and Heart Rate
    """
    plt.figure(dpi =80)
    #plotting the Sleep Duration and Heart Rate
    plt.scatter( df['Sleep Duration'],df['Heart Rate'])
    #Set title, x-axis label and  y-axis label
    plt.title('Sleep Duration Over Heart Rate')
    plt.xlabel('Sleep Duration')
    plt.ylabel('Heart Rate')
    plt.xticks(rotation=45)
    # Save and display the plot
    plt.savefig('Scatterplot.png')
    plt.show()
    return

def  plot_Bar(df):
    """
    This function creates a Bar plot to observe the BMI Categories
    with how many steps walked daily
    """
    plt.figure(dpi =80)
    #plotting the Sleep duration and stress data
    plt.bar(df_bar.index,df_bar['Daily Steps'])
    #Set title, x-axis label and  y-axis label
    plt.title('BMI VS Daily Steps')
    plt.xlabel('BMI')
    plt.ylabel('Daily Steps')
    # Save and display the plot
    plt.savefig('Barplot.png') 
    plt.show()
    return

def plot_Heatmap(df):
    """
    This function creates a heatmap to observe the 
    correlation between attributes 
    """
    plt.figure(dpi=80)
    # plotting a heatmap
    sns.heatmap(df.corr(), annot=True,  cmap='Blues', linewidths=.5)
    plt.title('Correlation between various factors')
    # Save and display the plot
    plt.savefig('Heatmap.png')
    plt.show()
    return


df= pd.read_csv('Sleep_health_and_lifestyle_dataset.csv',index_col = 'Person ID')

#cleaning data 
df = df.drop(['Sleep Disorder','Blood Pressure'],axis =1)

#removing all the Qualitative columns for understanding the basic stats
df_stat = df.drop(['Gender','Occupation','BMI Category'],axis = 1)

#basic statistics of the data

print('Describe', end='\n')
print(df.describe() , end='\n\n')

print('Skewness', end='\n')
print(df_stat.skew() , end='\n\n')

print('Kurtosis', end='\n')
print(df_stat.kurtosis() , end='\n\n')

print('Correlation', end='\n')
print(df_stat.corr() , end='\n\n')

#Visualising the scatter plot

plot_Scatter(df)

#Daily steps grouped by BMI category

df_bar = df[['BMI Category','Daily Steps']].groupby('BMI Category').mean()

#Visualising the bar graph

plot_Bar(df_bar)

#Visualising the correlation Heatmap
plot_Heatmap(df_stat)
