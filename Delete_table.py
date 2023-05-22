import boto3

def delete_food_table(dynamodb = None):
    if dynamodb is None:
        dynamodb = boto3.resource('dynamodb')
        
    table = dynamodb.Table('food_table')
    table.delete()
    
def main():
    delete_food_table()
    

if __name__ == "__main__":
    main()
    
