from ctf_0_basic_functions import create_update_cf


if __name__ == "__main__":
    template_path = '../cf_2_ec2.yaml'
    stack_name = 'EC2FULL'
    parameters = [
        {'ParameterKey': "NetworkStackName", "ParameterValue": 'EC2VPC'},
    ]
    print(create_update_cf(stack_name, template_path, parameters=parameters))
