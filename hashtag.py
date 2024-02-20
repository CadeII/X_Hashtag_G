import pandas as pd

hashtag1 = '아이유_더위닝_들을준비됐닝'
hashtag2 = 'IU_TheWinning_NowOpen'

data = pd.read_csv('X_Hashtag_G/ment.csv')
a = data.sample(n=1)
a['ment'] = a['ment'].str.split('\n')
b = a.iloc[0,0]

output = 'https://twitter.com/intent/post?text='+b[0]+'%0D%0A%23'+hashtag1+'%0D%0A'+b[1]+'%0D%0A%23'+hashtag2+'%0D%0A'+b[2]
print(output)

