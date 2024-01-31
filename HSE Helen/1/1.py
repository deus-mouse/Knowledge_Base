
import pandas
from sklearn.linear_model import LinearRegression
import numpy as np
from matplotlib import pyplot as plt




data = pandas.read_csv('../abalone.data',
                       names=['sex', 'len', 'diam', 'height',
                              'whole weight', 'shucked weight',
                              'viscera weight', 'shell weight',
                              'rings'])


# print(f'{type(data)=}')
# print(f'{data=}')

X = data[data.columns[1:-1]].values
y = data[data.columns[-1]].values

# print(f'{type(X.shape)=}')
# print(f'{X.shape=}')
# print(f'{X.shape[0]=}')

print('number of objects:', X.shape[0])
n_objects = X.shape[0]

coeffs = []

i = 2
for _ in range(i):
  indices = np.random.choice(n_objects, int(n_objects * 0.1))
  # print(f'{indices=}')
  # print(f'{len(indices)=}')

  reg = LinearRegression().fit(X[indices], y[indices])
  # print(f'{type(reg)=}')
  # print(f'{reg=}')
  # print(f'{type(reg.coef_)=}')
  # print(f'{reg.coef_=}')

  coeffs.append(reg.coef_)

  all_coeffs = np.vstack(tuple(coeffs))
  # print(f'{type(all_coeffs)=}')
  # print(f'{all_coeffs=}')

  # all_coeffs.shape

  for feature in range(all_coeffs.shape[1]):
      ax = plt.figure()
      # print(f'{ax=}')
      plt.hist(all_coeffs[:, feature], bins=100)
      plt.vlines(
          x=[np.percentile(all_coeffs[:, feature], 5),
             np.percentile(all_coeffs[:, feature], 95)],
          ymin=0,
          ymax=100,
          color='red'
      )
      ax.suptitle(f'feature {data.columns[feature + 1]}')


ranges = []
for feat in range(all_coeffs.shape[1]):
  feature = X[:, feat]
  print('-------------')
  print(f'{feature=}')
  print(f'{np.max(feature) - np.min(feature)=}')
  ranges.append(np.max(feature) - np.min(feature))

print(f'{ranges=}')

print(f'{plt.bar(height=ranges, x=range(len(ranges)))=}')