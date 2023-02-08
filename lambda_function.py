import pandas as pd

def lambda_handler(event, context):
    d = {'col1': [1,2], 'col2': [3,4]}
    df = pd.DataFrame(data=d)
    print(df)
<<<<<<< HEAD
    print('DevOPs Dashboard Test 02082023-3')
=======
    print('DevOPs Dashboard Test 01312023-2')
>>>>>>> 2152ffb8260925ac017caea98414e8916c83d512
