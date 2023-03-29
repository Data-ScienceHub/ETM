import boto3

class AWSHelper:
    '''
    Python class for connecting to various AWS API needed for this project

    boto3 documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
    '''

    def __init__(self, region):
        '''
        Purpose: creates a new helper for various AWS actions

        INPUTS:
        region - AWS region
        '''
        self.region = region
    
    def get_ssm_credentials(self, params):
        '''
        Purpose: gets parameters from AWS Systems Manager Parameter Store

        INPUTS:
        params - list of parameter names

        OUTPUTS:
        param_values - dictionary with the parameter names as keys and corresponding values
        '''
        ssm = boto3.client('ssm', self.region)
        response = ssm.get_parameters(
            Names = params,
            WithDecryption = True
        )
        
        # Build dict of credentials
        param_values = {k['Name']: k['Value'] for k in  response['Parameters']}
        return param_values