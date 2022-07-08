import pandas 
from sklearn.decomposition import PCA
import numpy as np

def function_to_run(array_of_search_criteria):
    try:
        # Import the data
        df = pandas.read_csv('nytdata.csv')
        
        # Drop columns that I will ignore for now although it will exclude columns explicitly referenced in the prompt. This is simply a priority decision, I would not exclude in a real scenario
        df = df.drop(['latitude', 'longitude','State Code','Region','ID', 'name', 'State Name', 'Image', 'How Expensive','Location'],1)
        
        # Dropping nans and normalizing the data
        cleaned_df = df.dropna()
        normalized_df=(cleaned_df-cleaned_df.mean())/cleaned_df.std()
        
        # Running PCA
        pca = PCA()
        princ_comp = pca.fit_transform(normalized_df)
        
        covariance_matrix = pca.get_covariance()

        data_used = ['latitude', 'longitude','State Code','Region','ID', 'name', 'State Name', 'Image', 'How Expensive','Location']

        #### ACTUAL COMPUATION ##
        # remove variables that we drop originally
        check_array = [item for item in array_of_search_criteria if item not in data_used]

        index = [normalized_df.columns.get_loc(item) for item in check_array]

        # take remaining variable and pull the associated rows of the covarinace matrix
        matrix_to_check = covariance_matrix[:, np.r_[index]].transpose()
        matrix_to_check[matrix_to_check >0.99]=0
        matrix_to_check[matrix_to_check <-0.99]=0

        # take the colums with the max 3 values
        max_val_list=[]
        max_index= []
        for i in range(0,np.shape(matrix_to_check)[0]):
            max_val_list.append(matrix_to_check[i].max())
            max_index.append(np.where(matrix_to_check[i]==max_val_list[i])[0][0])


        # grab the associated column
        relevant_columns = normalized_df.columns[max_index]


        # return the columns wrapped in static text
        print("This area is also known for scoring high on {}".format(" ".join(str(x) for x in relevant_columns + ", ")))
        return "This area is also known for scoring high on {}".format(" ".join(str(x) for x in relevant_columns + ", "))
    except:
        print("Error with computing additional criteria, there might not be any")
        return "Error with computing additional criteria, there might not be any"
    

function_to_run(["Densely Populated Score", "Low Crime Score"])
function_to_run(["Densely Populated Score", "latitude"])
function_to_run(["latitude"])


