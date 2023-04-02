import pandas as pd

class FileHelper:
    '''
    Python class for various file operations
    '''

    def __init__(self):
        '''
        Purpose: creates a new helper for various file actions
        '''
        pass
    
    def divide_chunks(self, my_list, chunk_size):
        '''
        Purpose: divides a list into sublists (chunks) of equal lengths

        INPUTS:
        my_list - list
        chunk_size - int length of desired chunks

        OUTPUTS:
        my_list - list of lists
        '''
        # looping till length l
        for i in range(0, len(my_list), chunk_size):
            yield my_list[i: i + chunk_size]
    
    def batch_upload_snowpark_as_csv(self, snowpark_results, file_name, batch_size=10000):
        '''
        Purpose: creates a CSV file in batches from a list of Snowpark objects

        INPUTS:
        snowpark_results - list of Snowpark objects
        file_name - str desired CSV file name
        batch_size - int size of batches, default 10000
        '''
        batches = self.divide_chunks(snowpark_results, batch_size)
        
        for idx, batch in enumerate(batches):
            batch_json = list(map(lambda x: x.as_dict(), batch))
            batch_df = pd.DataFrame(batch_json)
            if idx == 0:
                batch_df.to_csv(file_name, index = 0)
            else:
                batch_df.to_csv(file_name, index = 0, mode = 'a', header = False) # append succeeding batches
            
            print('Uploaded batch {0}'.format(idx + 1))
    
    def batch_upload_json_as_csv(self, json_results, file_name, batch_size=10000):
        '''
        Purpose: creates a CSV file in batches from a list of json objects

        INPUTS:
        json_results - list of json objects
        file_name - str desired CSV file name
        batch_size - int size of batches, default 10000
        '''
        batches = self.divide_chunks(json_results, batch_size)
        
        for idx, batch in enumerate(batches):
            batch_df = pd.DataFrame(batch)
            if idx == 0:
                batch_df.to_csv(file_name, index = 0)
            else:
                batch_df.to_csv(file_name, index = 0, mode = 'a', header = False) # append succeeding batches
            
            print('Uploaded batch {0}'.format(idx + 1))