import boto3
#Script to check your AWS account for any roles giving cross account access, it is very useful for securing your account. 
# Create an AWS IAM client
iam = boto3.client('iam')

# List all roles
response = iam.list_roles()

roles_with_cross_account_access = []

# Iterate through roles
for role in response['Roles']:
    # Get the role details including its trust policy
    role_details = iam.get_role(RoleName=role['RoleName'])
    
    # Check if the trust policy allows cross-account access
    for policy in role_details['Role']['AssumeRolePolicyDocument']['Statement']:
        if policy['Principal'].get('AWS'):
            roles_with_cross_account_access.append(role['RoleName'])
            break

# Print or use the roles with cross-account access
print("Roles with cross-account access: ")
for role_name in roles_with_cross_account_access:
    print(role_name)
