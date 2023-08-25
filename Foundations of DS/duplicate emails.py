"""
Write a solution to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.
Return the result table in any order.
"""

import pandas as pd

data = [[1, 'a@b.com'], [2, 'c@d.com'], [3, 'a@b.com']]
Person = pd.DataFrame(data, columns=['id', 'email']).astype({'id':'Int64', 'email':'object'})

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    print(person['email'].value_counts().values)

duplicate_emails(Person)