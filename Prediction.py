{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np \n",
    "import pandas as pd \n",
    "import pandas_datareader as data \n",
    "import matplotlib.pyplot as plt\n",
    "import pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Open</th>\n",
       "      <th>Close</th>\n",
       "      <th>Volume</th>\n",
       "      <th>Adj Close</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2009-12-31</th>\n",
       "      <td>7.619643</td>\n",
       "      <td>7.520000</td>\n",
       "      <td>7.611786</td>\n",
       "      <td>7.526071</td>\n",
       "      <td>352410800.0</td>\n",
       "      <td>6.471691</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2010-01-04</th>\n",
       "      <td>7.660714</td>\n",
       "      <td>7.585000</td>\n",
       "      <td>7.622500</td>\n",
       "      <td>7.643214</td>\n",
       "      <td>493729600.0</td>\n",
       "      <td>6.572422</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2010-01-05</th>\n",
       "      <td>7.699643</td>\n",
       "      <td>7.616071</td>\n",
       "      <td>7.664286</td>\n",
       "      <td>7.656429</td>\n",
       "      <td>601904800.0</td>\n",
       "      <td>6.583784</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2010-01-06</th>\n",
       "      <td>7.686786</td>\n",
       "      <td>7.526786</td>\n",
       "      <td>7.656429</td>\n",
       "      <td>7.534643</td>\n",
       "      <td>552160000.0</td>\n",
       "      <td>6.479061</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2010-01-07</th>\n",
       "      <td>7.571429</td>\n",
       "      <td>7.466071</td>\n",
       "      <td>7.562500</td>\n",
       "      <td>7.520714</td>\n",
       "      <td>477131200.0</td>\n",
       "      <td>6.467082</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                High       Low      Open     Close       Volume  Adj Close\n",
       "Date                                                                      \n",
       "2009-12-31  7.619643  7.520000  7.611786  7.526071  352410800.0   6.471691\n",
       "2010-01-04  7.660714  7.585000  7.622500  7.643214  493729600.0   6.572422\n",
       "2010-01-05  7.699643  7.616071  7.664286  7.656429  601904800.0   6.583784\n",
       "2010-01-06  7.686786  7.526786  7.656429  7.534643  552160000.0   6.479061\n",
       "2010-01-07  7.571429  7.466071  7.562500  7.520714  477131200.0   6.467082"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "start = '2010-01-01'\n",
    "end = '2019-12-31'\n",
    "df = data.DataReader('AAPL', 'yahoo', start,end)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df.reset_index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Open</th>\n",
       "      <th>Close</th>\n",
       "      <th>Volume</th>\n",
       "      <th>Adj Close</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2009-12-31</td>\n",
       "      <td>7.619643</td>\n",
       "      <td>7.520000</td>\n",
       "      <td>7.611786</td>\n",
       "      <td>7.526071</td>\n",
       "      <td>352410800.0</td>\n",
       "      <td>6.471691</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2010-01-04</td>\n",
       "      <td>7.660714</td>\n",
       "      <td>7.585000</td>\n",
       "      <td>7.622500</td>\n",
       "      <td>7.643214</td>\n",
       "      <td>493729600.0</td>\n",
       "      <td>6.572422</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2010-01-05</td>\n",
       "      <td>7.699643</td>\n",
       "      <td>7.616071</td>\n",
       "      <td>7.664286</td>\n",
       "      <td>7.656429</td>\n",
       "      <td>601904800.0</td>\n",
       "      <td>6.583784</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2010-01-06</td>\n",
       "      <td>7.686786</td>\n",
       "      <td>7.526786</td>\n",
       "      <td>7.656429</td>\n",
       "      <td>7.534643</td>\n",
       "      <td>552160000.0</td>\n",
       "      <td>6.479061</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2010-01-07</td>\n",
       "      <td>7.571429</td>\n",
       "      <td>7.466071</td>\n",
       "      <td>7.562500</td>\n",
       "      <td>7.520714</td>\n",
       "      <td>477131200.0</td>\n",
       "      <td>6.467082</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Date      High       Low      Open     Close       Volume  Adj Close\n",
       "0 2009-12-31  7.619643  7.520000  7.611786  7.526071  352410800.0   6.471691\n",
       "1 2010-01-04  7.660714  7.585000  7.622500  7.643214  493729600.0   6.572422\n",
       "2 2010-01-05  7.699643  7.616071  7.664286  7.656429  601904800.0   6.583784\n",
       "3 2010-01-06  7.686786  7.526786  7.656429  7.534643  552160000.0   6.479061\n",
       "4 2010-01-07  7.571429  7.466071  7.562500  7.520714  477131200.0   6.467082"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df.drop(['Adj Close', 'Date'], axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x24a701a3fa0>]"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXAAAAD4CAYAAAD1jb0+AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8vihELAAAACXBIWXMAAAsTAAALEwEAmpwYAAAvpElEQVR4nO3dd3xUVfr48c9JJwVCQhI6oXdpkWIFkSIW7F3Rr7vorvvV/e1acIu6ugru6lq/Fiwra2N11QUXYUUEEVEwVOmdEAkkQHpP5vz+uHcm05JMwsxkbvK8Xy9ec++5d+aey8CTk+eeorTWCCGEsJ6wlq6AEEKI5pEALoQQFiUBXAghLEoCuBBCWJQEcCGEsKiIYF6sU6dOOj09PZiXFEIIy9uwYcMJrXWKe3lQA3h6ejqZmZnBvKQQQlieUuqwt3JJoQghhEVJABdCCIuSAC6EEBYlAVwIISxKArgQQliUBHAhhLAoCeBCCGFREsCFECKAjhdV8PR/d7M/r8Tvny0BXAghAujgiVJeWrmPY4UVfv9sCeBCCBFAp0qrAEiKi/L7Z0sAF0KIAFqxMxeA5HgJ4EIIYSn2ZSuT46L9/tkSwIUQIpAUdEtsR3iY8vtHSwAXQogAqqqxER0RmFArAVwIIQKootpGVEsFcKXUQKXUZqc/RUqpXyulkpRSy5VSe83XjgGpoRBCWFh2fllAHmCCDwFca71baz1Saz0SGAOUAZ8Cc4AVWuv+wApzXwghhJPSqhpSE2IC8tlNbddPBvZrrQ8DM4EFZvkC4HI/1ksIISyvoKyKI6fKKa2sCcjnNzWAXw98YG6naa1zAMzXVG9vUErNVkplKqUy8/Lyml9TIYSwmPfWZQHwxY7jAfl8nwO4UioKuAz4qCkX0FrP11pnaK0zUlI81uQUQohWq5OZ+373jnEB+fymtMAvAjZqre0/So4rpboAmK+5/q6cEEJYWXGFkTo5o0eHgHx+UwL4DdSlTwAWA7PM7VnAIn9VSgghWoMSM/cdFxURkM/3KYArpWKBKcAnTsXzgClKqb3msXn+r54QQlhXSUUNcVHhARmFCeDTjwWtdRmQ7FZ2EqNXihBCCC9KKmuIjwlM6xtkJKYQQgTMwh+OEBEWuDArAVwIIQJg3YGTAPxUUB6wa0gAF0KIANiaXRjwa0gAF0IIP/tgfRZPfL4z4NeRAC6EEH720Cc/Orbvmdw/YNeRAC6EEH5UVWNz2Z88yOssI34hAVwIIfzo4IlSl33pRiiEEBaxMSvfZT8hWgK4EEJYQmF5tcu+tMCFEMIiCsuriQhTDO9mTGDVLjI8YNcK3I8GIYRog95cc5Aam+bdO8Zx+FQpSgVmHhSQAC6EEH5l74XSITaSM2ITA3otSaEIIYSfaK0BuHtS36BcTwK4EEL4SXWtEcADmfd2JgFcCCH8pKKmFoAYCeBCCGEtldVG/jtaArgQQljLscIKAKIjghNaJYALIYSfXPrSGkBSKEIIYVkx0gIXQghrigyXAC6EENYUuMGXLnwK4EqpRKXUv5RSu5RSO5VSE5RSSUqp5UqpveZrx0BXVgghrKB9TGRQruNrC/x5YJnWehAwAtgJzAFWaK37AyvMfSGEaLMSYiJIiI5gdM/EoFyv0QCulGoPnAe8CaC1rtJaFwAzgQXmaQuAywNTRSGECH0nSyoprqghpX10QCewcuZLC7wPkAf8XSm1SSn1hlIqDkjTWucAmK9e1w1SSs1WSmUqpTLz8vL8VnEhhAglOWYf8LP7dgraNX0J4BHAaOAVrfUooJQmpEu01vO11hla64yUlJRmVlMIIUJbpTkL4QWDA7cGpjtfAng2kK21Xmfu/wsjoB9XSnUBMF9zA1NFIYQIfb8zV6KPDdIgHvAhgGutjwFHlFIDzaLJwA5gMTDLLJsFLApIDYUQwgJ2Hy8GoFvHdkG7pq8LOvwv8J5SKgo4ANyOEfw/VErdAWQB1wSmikIIYR1dO4RYANdabwYyvBya7NfaCCHEaXhiyQ4mDUrlrCA+SLSLj47g2owehIUFaRQPMhJTCNFK2Gya1785yI2vr2v85ACoqrERFaQ5UOwkgAshWoWSqpoWu7bNpqmqlQAuhBBN8trX+0mfs4T80qoWq4P9h0dCdHDXiZcALoSwtLlLdwHw6tf7HWW1Nh3UOsz/+gAA1TZbUK8rAVwI0Sp8sP6IY7uiujao135p5T4ACsurg3rd4Lb3hRAiCGpqg9MCP1pQzu5jxY79Hh1jg3JdO2mBCyFanRGPfcE/f8gK+HV+vXAzt7/9g2P/xrE9A35NZxLAhRCt0oMf/8jRgvKAXmNLdoHLfjD7gIMEcCGEhdkaeVgZ6IeZ9gmsWooEcCGEZRVXNNz3O9gt4mCTAC6EsKzxc1c0eLyxFvrpmj60s2P75ZtGB/Ra3kgvFCGEZZWb3QXn3zKGyhobmYdOseC7w47jNQEO4GFhEKZg7pXDmTG8S0Cv5Y0EcCGE5Y3skUhq+xiyTpW5lNcGeGBNUXkNI3skct2Zwe19YicpFCGEpY0wgzfATeN6MnFg3cpfgWiBv/r1fg6dKGXt/hOs2XeCpLhov1/DVxLAhRCWZO9hMnFAXcBOjI3i7dvHOvabM6Dn8MlSnlq2C60933uqtIp5S3cx8elVjlkPY6OCtwKPOwngQghLsue/vQXQ+6cZC4idbMYEV+f/dRWvrNrPgROlHsdqaj1TMhnpHZt8DX+RAC6EsKQb5n8PQOcOMR7HhnXrAMCst9Y3+/O99WD502c7PMpigrgGpjsJ4EIIyymvquXHnwoB6J+a4HE8opn9v52npC2p9OxjvuTHnAbfE2wSwIUQlnMkv663SZ+UOI/jYap5AfzNNQcd240NErILdFfFhkg3QiGE5VSZQ9j/ctUZXlMYmuYF1eNFFY5t5xa4zaZ5Zvlur+/plxrfrGv5g7TAhRCWY2/1JsdHeT3e3O7fEeF1IbHEqQW+bPsx/m/lfm9vYZrTaMxg86kFrpQ6BBQDtUCN1jpDKZUE/BNIBw4B12qt8wNTTSGEqGPvDeIccJ01d0EH53x2sVML/Msdx5v1eYHWlBb4JK31SK11hrk/B1ihte4PrDD3hRAi4KrN/t2R9TysTIyNbPJnVtbUsmz7Mcd+cUXd6joVNd5/IKy+f1KTr+NPp5NCmQksMLcXAJefdm2EEMIH9kE89bXAM9KT6JsSR1p730dJDvzDMpd9ewrleFEFn/9oBPYxver6fF89pjs9k4O7Ao87XwO4Br5QSm1QSs02y9K01jkA5muqtzcqpWYrpTKVUpl5eXmnX2MhRJtnXzw4Irz+3ibj+iQ3ayTmVaO7k5oQ7XiIOe7JuhkP37rtTMf2ny8f1uTP9jdfA/jZWuvRwEXA3Uqp83y9gNZ6vtY6Q2udkZKS0vgbhBCiETWOFEr9ISwqPIwqLyMn63PhYKMN+vjlQ0mIifDajbBDu7rUTEsO4LHzKYBrrY+ar7nAp8BY4LhSqguA+ZobqEoKIYQz+zD6hlrg0RFhju6GjdlzvJisU2Wc278TsVERREeEO1bbSUkw0jC9Wjhd4k2jAVwpFaeUSrBvA1OBbcBiYJZ52ixgUaAqKYRo25Zty+FYYV0f7Xs+2ARAZAMBPCoijMoam9dJqZwVVVQz9dnV7DlewsA0Y1RneJii1mZjw+FT5BVXAvD89aNO9zb8zpcWeBqwRim1BVgPLNFaLwPmAVOUUnuBKea+EEL4VUllDXe9u5FJT68CXOcoiWgghWJPgbz41b4GP7/aqZXeJbEdYAZwDftySxzHRvZIbGrVA67RfuBa6wPACC/lJ4HJgaiUEELYHcwzZgUsr67FZtNc9epax7GGUih5JUbL+d+bfuKeyf3rPc95KHxSnJHj1kBOQTnKHJJ/xzm9Hed8+ZvzKKlsXj9zf5Oh9EKIkFRr0/z924Musw1+tOEIm7IKHPuR9XQjhLr5UGyNpFCc8+TJ5uIMW44Y1/gpvxyAX03q5zinn5fJs1qKBHAhREhavSePPy/Z6VL2t+V7HNvREWF0jPU+lB6MtSoBahsJ4NVOPVV6JLk+qNyaXQBAXHRohsrQrJUQQnjJjhwvMtIi4/sksXD2hAbfbs+MNDYvyj+cFkHuZubA7bJOlREVEUZURGhOGxWatRJCtHkFZfXPs/3qzWMaff/gLkaqI7WR0ZjvfF8XwN0D9f68UhJCtPUNEsCFECHq4Aljzu8hXdqz8r6JLscSG0id2N11Xl8ANh8pYO3+E/Wed/2ZPQD4+v66a4Q7zbESqukTkAAuhAhRhWVVdGgXyef3nkvvTnFENzGNERam6Nw+Bq1xLEDsTVlVLd07tqNXct3CEJ/96hzHdrwEcCGEqJ/WmtV78lwG3ZRX19LOabi6PT/93HUjff5cX3LXp0qrSIpzbdF3Tazr+SIBXAghGvBRZja3vrWeTzf95Cgrr7bRzmnF+ZdvHs0NY3ty6YiuPn9uWVXj/bWPFVaQEu+aJ0+MjWK4uTByOy+r3ocKCeBCiKDbcDifRZuNYF1SWcMXO4zpWvfn1Y18LK+qdZkwalDn9sy9crhLfroxJ8zBPA3JLa6gq1vvE4BYM3DHRIZumAzdmgkhWq2rXlnLvQs3o7XmqaW7+HKnMRfewvVHOFVaxR1v/8CBvBLaBSF4llfXOoK1M3v6xdfFjVuCBHAhRMDYbJpNWXUrLa7cleuybNn+vFL25hY79mMiw1m5K5cVu3I5cKI04OkLm01TUW1rcGrYtftPBrQOp0MCuBAiYP7zYw5XvLyWOR9v5cipMm5/+wdGPb7ccfxIfpnL+ZU1NpfV4Lt28Ext+NPsdzYA3vPcj1w6FID2MaH7EDN0ayaEsDx763vhD0fYmOW55nlJRQ2xUXVhKL+simynoB4foOD57PI9nCip5MudxmLFZZWeaRJ7z5SmLAoRbNICF0IEjPNEUXuOl3gcP5Jfxle7jPz3fVMHUGvTvP7NQcfxhiaragr3tTGfX7GX99ZlOfaLvQRwe8vbeR3MUCMBXAgRMOX1dOOzrxr/l2W7686t9jy3oQUbfDFtaBpgzKHivMq8u2szeniURYSH8fk95/o0bL+lSAAXQgRMiZeWLXj2zx6YlkB8dKTHeQ0t2OCLV28ew8VndAHg3oWbvZ6z94mLGNylvddjQ7q2JyHGs16hQgK4ECIgamptfLHjuNdjM4Z1dlnh5q/XnOF11OTptsCVUizZmgPgSNU4u3tSX7+laVqCPMQUQgREQXldyuKfs8ez7WgR5w9IobC8msFdEhjy8H8dx2Miw4nyEqydH3A214PTB/HUsl2OlrjWGqXgylHduX/aoNP+/JZk3R89QoiQVuQUwMf1SeaOc3rTLzWeMb06EhsVQZxT1712keEuLfBO8UYPkLjo0+8H/ouJxqyE9pZ4TmEFWsOAtPjT/uyWJgFcCOEXWSfLXB5a2h9KvnLTaK/n//mKYY7tmMhwOrQzgvagzgmOz/FHC9zdKXMgkbfh81bjcwBXSoUrpTYppf5j7icppZYrpfaar6Hb10YIEVC5xRWc99eV/HnJDkdZRbXRhbC+0ZTREXXlMZFhTB2SxsOXDOHjX5xFqRnA8xtY1KG57P26A9XHPJia0gK/F3BeoG4OsEJr3R9YYe4LIdqYnMJyXl11AMClb3Wl2QKvb5i6c2u9XWQ4YWGK/zmnt8sCCv5qgV84OM2xbe+bHm3hh5d2Pv3tKKW6AxcDTwC/MYtnAhPN7QXAKuBB/1ZPCBHKyqpqmDD3K5eyjVn5DOnSnnnLdgH1B/AIp4eWEW7BdO8TF/HxhmyuGNXNL/XslRzryLnbA3iornPZFL7ewXPAA4DzmNI0rXUOgPma6u2NSqnZSqlMpVRmXl7e6dRVCBFiDuSVepRd+fJaFm8+ytbsQqD+6ViVqr+LYGR4GNeP7dmkqWMbEh0RRqUZuNtUAFdKXQLkaq03NOcCWuv5WusMrXVGSkpKcz5CCBGi6ptvu6C8LncdE+G9Be6f0OybmMhwamyal77ay/pDp4A2EsCBs4HLlFKHgIXABUqpd4HjSqkuAOarZy95IYTllVXVkGkGPXe3/f0Hx/ZvpgxwbDvnwutbFLiBBrjf1dqMpdqe/mIP81cb+fqoVpADb/QOtNYPaa27a63TgeuBr7TWNwOLgVnmabOARQGrpRCixbz29QGufvU7xjy+nPQ5Sygs9z6nyOzz+vC/F/QD4PDJuhkF7X263Z0/IHi/kWsvZac7TD8UnM4j3nnAh0qpO4As4Br/VEkIEUqeX7EXgJNm/+kNh09xwaA0bLa6sPjhnRPMvtx184ZcM6Y7c68cXm+uOyEmkvumDghIX293kV5y6a2hG2GT7kBrvQqjtwla65PAZP9XSQgRyuwLx7+99pCjbGzvJADaOwXweyb39+hd4u5XF/T3e/288VYP95Xorcj6v0MIIYLKPkBn3tJdngfN4D5taBo9kmKDWKuGRbi1wF+/NaOFauJfEsCFED6xL4pQUV1Lda3N60o1AzsnAHD+AK+9iltMhNtEWVOGpNVzprVIABdC1MveZ3pE9w68c8c4ACpqatl9rNjr+SN6JLL6/kncMNZzgYSW5JxCOTO99cz6Yf0svhAiYJZtPwYYPUZSE4wW+JFT5STHGds/P7c3l47o6vKensmhkzqxc06h3DSuVwvWxL8kgAsh6vXZlqMAJMdHO4bEv/r1fsfxn5/bh9T2MS1St6Y4u28nx3Yor3HZVBLAhRAubDbN2U99Rc+kWNYdNAbw3DK+l8fAm6iIMJLjo718QujpmRxL5/YxHCuq8MiHW5kEcCGEix05ReQUVpBTWOEoC/PSj7qqxua3uUqCocbst26lOjdGHmIKIVzc99EWl/07zunt2O6fWreKza0TrJVL7pMSB7jOQ2510gIXQgDGCvIfZR5hl1sPk3ucBtt8dNcEDp4oZVRP6+WR598yhi3ZhS6jRa1OArgQAoBhj/zXZX/h7PFsOJxPh9i6gJcYG8WontYcwZgYGxXU+VeCQQK4EMLDrsenExMZzvg+yS1dFdEACeBCCNYdOOnYPjh3RoOLLYjQIQ8xhRD85b+7Afj77WdK8LYQCeBCeHGssAKtvc0i3TodPmksjTZpYGjNYSIaJgFcCDf7cksYP3cFf//2kEv5da99x2Of7eD9dVmkz1nimCcEYO2+E2w/WhjkmvpHYVk1J0qqmDG8c0tXRTSRBHAh3OQWGwNY3l+f5VK+7uAp3vr2IL/79EcAnv1yj+PYjW+s4+IX1gSvkn60ao+xGuIEp+HmwhokgAvhxmY2rPflljjKnFvbdq+s2t8q0ix7j5cQpowVdIS1SAAXws176w47tic9vYptPxU6csTuej/0ORsOe1/w1ypeWrkPm8YxWZWwDulGKISbA3l1wfrgiVIuedEzNXLz+J68+72RYrnqle+CVrdA6ZbYrqWrIJpBWuBCuNFoBqYlNHjO3ZP6Bak2gdc+JqLVrFDT1kgAF8LNiZIqxjSyakuXDu04NO9iund0bbnaH4BaSXWtJrIVTbHaljQawJVSMUqp9UqpLUqp7UqpP5nlSUqp5Uqpvear9Wa3EcJNTa2N/LIqOrnNc53RqyOL7j6b7x66gP1PznCUv2suM2b3/Jd76/3sbT8Vsu2n0OtqWGOzEdnI6vEiNPmSA68ELtBalyilIoE1SqmlwJXACq31PKXUHGAO8GAA6ypEwJ0qq0JrSImvm7Dp8pFdeebakV7nkU7vFOeyvyW7oN7PtufSQ2mo+uItR6mu1WSdKmvpqohmaDSAa6OflL0/VaT5RwMzgYlm+QJgFRLAhcXZW8jJ8dFsfngKtTbt86oz5/TrRObhU5RU1hAf7fpfq7ii2rG9L7eE/o3k2IMhO7+Mez7YBMDMkd1auDaiOXz6vUkpFa6U2gzkAsu11uuANK11DoD56nUMrlJqtlIqUymVmZeX56dqC3F6Dp0oJX3OEjYfKXCU1do0//N2JgDtYyJJjI3yKXjfP20g12X0IDoijIpqG3e9s8HjnCc/3+XYnvLsatLnLCHzUHC6H2bnl1FRXetRfs5TKwHomRQrDzEtyqcArrWu1VqPBLoDY5VSw3y9gNZ6vtY6Q2udkZLSuubiFdZ18QvfAPDgv7Y6yvbm1i1kMLZ3ks+fdfekfjx19RmOZcfW7Dvhcc4HbqM6Aa5+NbDdD7XW9H5oCec8tZI5H291KZ+7dKdj/8vfnB/QeojAadKTC611AUaqZDpwXCnVBcB8zfV35YQIlDO6JwJQ7tQyjQgz/jv0SYkjKqLpD/WcU+S7jhXx64WbePf7w/W/IUBqam0cyCvh4IlS7ANFV+yq++/5wfojvPb1AQAemD6wWfcqQkOjOXClVApQrbUuUEq1Ay4EngIWA7OAeebrokBWVAh/+s6c/zrrVBnVtTbClKKyxgjmD0wb1KzPXLu/bk7t3ceK+ffmo/x781GGd+tw+hVugre+PciTn+/iPKfVZ8am1/1G8fKqfY7tCwdL6sTKfPnR2wVYqZTaCvyAkQP/D0bgnqKU2gtMMfeFCHlH3Hpc9P/9Ui59cQ25RZUAxEQ2r0X6+My6zOK9Czc7tv+4aJvHuakJRm7d/kPDn3bmGKmg1XuMZ05ndO9AXolxbydLKsnOLwfg0LyLGRACD1NF8zX6L1VrvVVrPUprfYbWepjW+jGz/KTWerLWur/5au0JIUSbccic18S5W+COnCJuf/sHwOhi1RyXj+rG7PP6eJRvzTZ6tswc2dVR9v+mDADgZElVg5+ZV1zJI4u2NSnQ90yKddkf3bMjW7ML2XWsiJveWAfADWN7+vx5InRJ8ku0OTkFxmjJxb862+txm635MwzeP21gvceiwsN449YM3r1jHKWVNQDMX32g3vM3ZeVz5hNfsuC7w3yzx/PBaH1qbHUzJy6cPZ4uHWIAmP7cN44V528aJwG8NZDJrESbUlJZwwNmj4z60genEb8bHNF437SBpLU3gmm7KOO8/XklaK29Duy54uW1ju2aRipVXlXLpS+toX1MBMO6daBDu0i2PDIVgE7x0cxdusvl/H6p8b7dkAhpEsBFm/JR5hHHdn3BdkR3/z90fOWm0Y7gDXW9YL7Ze4IFaw9x29m9G3z/CTOHXZ87FvzgmL98Y1aByzH3+VpApo5tLSSAizblxa+MHhjuc5jYpSfHkuoUaE/HE1cM46Zxvbwec/7h8c73hz0CeG6R66RYL361l5vHe/8scO0B4845WD900SDuPL9vg/UW1iE5cNGmnCo1Hhqe099YPuyNWzNc8sFnpvs+gKcx9QVvd+P7JHuUXfOa6yCf40X1t8BXmn28O8VHMaRLe6/n3Du5PwApCb5NCyCsQVrgotWqqbVRWWMjzpyXxD6cfEyvuokzLxySxoVD0rh/2kCy88uDmhv+5oFJXPLiGkrMB5rODp80ujrOvXI4heXVzFu6i5MllV6H9r/4lTEDYrfEdrx+awZjn1zhcc4vJvYlKS5K5jxpZSSAi1Zr9jsb+GpXLi/fNBqb1o6HlrdO8GwZJ8ZGkRgb5VEeSD2SYhmQFs9xt3SJfdHkeyf354axPflsy1HA+O3BWwAf2aMjG7MK+GD2eGKjvP+XjokMZ9ZZ6f69AdHiJICLVulkSSVfmamFX763EYBLRxj9sL091POnRXefTbso3x4SpraP4YeDp7jng008cukQkuOjeX+dMW+KvT+3PYddUe25sDJArc1G+5gIR/D+5Jdn0SlOUiVtgeTA25hb3lxH+pwlrWI19YY8v8JzYQV7SzY1wT8PKeszokeizyMcU+KjyS2uZPGWo/zPgkzKqurSKeP6GPl4+8jQippa/vyfHYx5fDnrDxrj5o4WlLPgu8NU1tQF99E9O9Iz2XUwj2idJIC3IVprvtlrDAjJL6tu5Gxr+vu3B5n8zCoOnax/gYJQepDnnD7ZcqTA8f08ddVwunc0gnB0hNECr6y28caag5wsreJa8yHnr943frtwDuCi7ZAA3kbU1Nr40KkP9Jc7jrdgbQLnT5/tYH9eKav35HldQQdCqw90uds83Xeac4k719HRAnc79x/fHfLo8y3aFsmBtxEX/u1rl1bpAx9v5doze7Rgjfzr4IlSJj29yqVs3pXDGdylPakJRprCvqRZKElPjgM8FzpJiqt7oGoP5tn5xvcXFR5GVa2NhxdtD0odReiSAN4GbMrK95pSOF5U4TI60Ip+Kign62SZ1wUTxvVOduSCU9vH8Mkvz6KkwrPLXkv67dQBjOyRyK//udml/Jx+nRzbMWYK5dHPdgDw3PUjHQ9mAb78zXkky0PLNklSKG3A0m3HHNtRTiMAP930U0tUx69ufmMdN7z+PXtzSxxlKQnRXHJGF48HeaN7dnSZIzsUJMREcvko177Zv5kywGVulM4dXH/IDuqcwO9nDHbs90tNoGNccLtAitAgLfA2oJcZyFbdN5H0TnHsOFrEjBe+Yd7SXUwZkkbfFGtObKS15uAJY2rYnTlFgLEqzjcPTAqpPLcvnrpqOCdLq+ibEs+0oZ1djkVFhDF1SBpfmM8t+qTEc8Sc03u627mibZEWuEW9/e1BLnhmlU9Tn35rrtFob8l1S6zrB/351pzAVDAI3vr2kMv+72YM4sDciy0XvAGuO7Mnv5zYzyN42712yxiX/Ql9krntrHQemzk0GNUTIUoCuEU9+tkODuSVssdpIV5vjhdV8PmPRgrFHtg6xEY6jj+zfE/gKhlgj//HyAlfPrIrqQnRrXp5MKUUEwemOOY0iYoI49HLhvpt4i1hTZJCsaCv99T1Wli9J4+BaQke80l/sD6LHUeLHKMR3RcaePXmMdz17obAVzaABqTFk1NQwXPXj2rpqgTF27ePbekqiBAjAdxiam2aWW+td+w/+fkuDp4oY+6Vwx1lxworeOiTH13ed5fbFKJje/tv1r1gq6iuNX77OF7idQkzIdoKSaFYTNYpz+6A7l3oDuSVuOyP6dXRY1CLMTOdMTfI7mMNp2FCic2mGfTHZcx44RsAZgzv0sI1EqLlSAC3mKfclsays89tsikrnxvNhWvt6lv/0J4zfnPNAdLnLGHUY1/4saaBselIgcv+yB6JLVIPIUJBowFcKdVDKbVSKbVTKbVdKXWvWZ6klFqulNprvnZs7LPE6cs8bExitPGPU1zKt2YXkj5nics6ihPMhQI6tIvEm6Fdjcn/P8zMBqwxP4rz3Nk/P7fhZciEaO18aYHXAL/VWg8GxgN3K6WGAHOAFVrr/sAKc18EWEavJAakxZMUF8Vgp9VXZv7ftx7nXj+2B5Hhqt6Z8eyTJbWkWpsmfc4Szv3LV0x99muqGpmUyb6a+9J7z+X3Fw8JRhWFCFmNBnCtdY7WeqO5XQzsBLoBM4EF5mkLgMsDVEfhpLiymoQYo0U9+zzvLdBz+3firvP7MnNkN3Y+Np0eSd4DdVREGOP7uD7MDPY0s98fMNZyPHKqnD3HSxjwh6Xc/9EWCsu9/zZgD+Dx0fL8XYgm/S9QSqUDo4B1QJrWOgeMIK+USq3nPbOB2QA9e3rPxQrflFbWsPFwgSPoXjaiG0cLKqissfGCOf/1/FvGMNVpMEhEPSuv25VXuc5wl19WzbPL93D/9IG0j/GeevGnRxd7Tsj00YZsPtqQzas3j2ZC3050aBdJ1skyUttHU2bWN9bHBROEaM18DuBKqXjgY+DXWusi937H9dFazwfmA2RkZLTuVQQC7NIX11BeXUtXcyRleJji7kn9WLbNGE05vk+SS/D2xZbsQpf90Y8vByA2OpyHLhrs7S1+NbpnR5d5TJzd9e5GLhvRlavGdHd0nbw2ozuAY51LIdoyn3qhKKUiMYL3e1rrT8zi40qpLubxLkBuYKoo7A6Y8364P5S057Ibyx97c27/Tl7LsxpYEOF0rdh5nPQ5S/jHd4f4Yscx+nSKY8MfLuTqMd09zl285ahLv3f7A9foCOlAJYQvvVAU8CawU2v9N6dDi4FZ5vYsYJH/qyfsiirqcsLui9P2S43nwsFp3D9tUJM/981ZZwJwVt9kl/Kl245RUxuYVV7uWJAJwMOLtpNfVk21zUZyfDRPXzOC568fyRCnh7P18fU3QCFaM1+aMWcDtwAXKKU2m39mAPOAKUqpvcAUc18EyMXmwJUPfj7eYw7vmMhw3piVwQS3IOyLqIgwvvrt+fz99jM9jvX7/dLmVdbJj9mFVNfaHA8fvenotBr8zJHdSO/k+tD1mWtGsObBSVxyhjFo52fnSPdBIcCHHLjWeg1QX3Nnsn+rI7wpr6rlyClj+tAz0/3f3b6POZ3sA9MH8pdlu/32ud/tP8kNr3/v2N/2p2lU19iICFNMHZpGakIMY3p19JiBz776+m1npfObqQMcD1NfunE0z11na/TBrBBthTwJsoBNWfmO7UAGr19O7McvJ/bjsy1H+d8PNgFGt8LmpitW7HRdd/OppbvY+lMhNTbN3ZP6MbRrB6/vmzw4la3ZBdxxTm+PnjASvIWoIwHcAo6YayF+dNeEoFzPOaWxMauAfqnx9Y7mbEiZ2yK873x/2LHdUJ77pnG9uHFsT8lzC9EIac5YwKlS4wHmYB8e7vnD2f2SGdbNuNZVr6xl9j8ym/wZNptmU1YBvTvFceuEXi7HJg5MaTQ4S/AWonESwC1gZ04RXTvEBG30oVKK686sG3S17qAx/8q+3GJe+mqvY7Tm81/u9bqYMMAnm35iZ04RB0+UcsGgujFej88cKvNaC+EnkkIJcSdKKlm85WjQV5updetCuPtYMdOeWw3A9GGd6dMpnme/NFbz6ZrYjuS4KIZ1q8tpv/b1fsf2+U4LCd8yIT2AtRaibZEAHuLmfGwszDBpUHBXU88pqnDZtwdvgJzCCmKj6v7p2Afa7HviIiLCw9BaO0ZXPnvdCEc6ROYvEcK/JIUS4uyTPd04NrjzyKQm1L/W4i1vrmfZtmMe5fZ+4x+ZoyXvPL8PV4wyRld+/9Bk1jw4KQA1FaLtkiZRC9t+tJAuHdqRFBflceyFFXsd818H+6HebWelM7hzAmN7J/HI4u28t8411/2YuaCwu/fXZfG7T43fGi4b0dVR3rmDLL4rhL9JC7wFaK3ZcDif8qpaLn5hjWMCKWcH8kr4WwuuGB8epjirXyciwsNISYh2lNsXgQDoGBvJo5cOYcvDU3nuupEAjuANuLxPCOF/0gIPguNFFSTERDjyxhuzCrjqlbVMHVL3YPLu9zdy/9SBpHeKA+Cyl4wFGqLCw1h45/jgV9rJ3ZP60Ss5lpkjuqEx8uH7ckvomRzHbWcbw9qnDnV9yPrIpUMaTMMIIU6fBPAAs9k0455cAcCheRcDsOOoMYXrFzvqRiou2ZrDsm3H2PboNDZm5TtSJ3ueuCjINfYUGR7myGUDZPTqyL7cElLi69I+zg81F919NiNkrUohAk4CeIAdOlnq2H73+8Os3pPnErid1do0gx9e5tgP1sjLprKvcH+D24PVyYNSWbErl17JLb9UmxBtgQTwANvqtGDCH/69zes5H945gWtf+86j/Mz0JC9nt7z/N2UASXFRnOM2l/j/3TSa3KJKEmM9H8gKIfxPHmIG2PajhV7LfzGxr2N7bO8k5t8yxrHfLbEdD0wfGPC6NVen+Gh+O3Ug0RGuy5rFRIbTU1rfQgSNtMCb4J3vDvHHRdu5ekx3pg/tzIVDGh4dmVtcwevfHGR4tw78+FNdILfniPccK6a9OUmU81JoK++bSJSsOCOEaIQEcB9sOHyKTvHR/HGRsQDvvzZk868N2Qzu0p67zu9Ddn45f/3vbqYP7czDlw4hO7+csb2T+O2HWwBo57YAr/0B35u3uS6isP53k9mRUyTBWwjhEwngjdh9rJirXvHMT4MxydS9Czc79pdtP8ay7cYIxdX3T3KsQjP/ljFsOlIAwODO9c8omNo+htT20vVOCOEbCeCNmLt0p8t+bFQ4gzonsDGrwKU8JSGavOJKx/55f10JGKuoJ8ZGMWlgKkII4U8SwDFGRp4srQLgaEE5fVPiOf+vqzhRUuly3vs/H8dYs2eI+3qRT14xnP15Jcxbusul/JqMHgGsuRCiLZMADsxffYC5boHX2Yd3TkBrzbg+dYsG2wflaK3ZfrSIYd06MIU07jq/L5uy8rni5bVA6HYFFEJYX6MBXCn1FnAJkKu1HmaWJQH/BNKBQ8C1Wuv8+j4j1C2vZ2DNnj9f1OgDRaWUyzzYAKN6duTpa0ZwRnfvaz4KIYQ/+NLd4W1gulvZHGCF1ro/sMLct5yK6loWbf6J7Pxyj2MH5844rd4gV4/pzoC0hNOpnhBCNKjRFrjWerVSKt2teCYw0dxeAKwCHvRnxYLhpa/28dLKfYCx8MBFw7o4jsmajEKIUNfcJmaa1joHwHwNiS4WuW6ryGw/WsiNr39PtdvyYGDMO2IP3gCXjehGTGS4448QQoS6gI8YUUrNVkplKqUy8/LyAnadtftPMPbJFaTPWUJecSVf78nj4hfWsHb/SX62IJPCsmpe/Xo/28wRkV/uNPLeY9OTeO9n4xwTNAkhhFU0txfKcaVUF611jlKqC5Bb34la6/nAfICMjAzdzOs1asOhumeoZz7xpcuxr/fkMeKxLxz7T1wxjN9/akws9eZtGSTERAaqWkIIETDNbYEvBmaZ27OARf6pTvPU2jTPNGH1Gnvwvnl8TwneQgjLajSAK6U+AL4DBiqlspVSdwDzgClKqb3AFHO/RVRU1zLWrcXtbP4tYxzzU7//s3EkxtYF7DvP61vf24QQIuT50gvlhnoOTfZzXZpszd4T3PzmOgCuHNWNRy4dyojHviAqPIynrx3B6J6JdO8Y6zLT3+aHp/Kr9zcyvFsHeiTJ1KdCCOtSWgcsLe0hIyNDZ2ZmNuu9+aVVnCytpF+q0bd697Fipj232nHcPjJSCCFaG6XUBq11hnu5JYbSv776AE98bkwqNXlQKm/MyuCd7w8BcF1GDx65bEgL1k4IIVqGJQK483zaK3bl0vuhzwEY1TORp64+o6WqJYQQLcoSKwfcPL4XB+fO8Ch/6ioJ3kKItssSARyMoe1bHp4KwKDOCWz70zSZa0QI0aZZIoVi1yE2Uh5WCiGEyTItcCGEEK4kgAshhEVJABdCCIuSAC6EEBYlAVwIISxKArgQQliUBHAhhLAoCeBCCGFRQZ2NUCmVBxxu5ts7ASf8WB0raGv33NbuF9rePbe1+wX/3HMvrXWKe2FQA/jpUEpleptOsTVra/fc1u4X2t49t7X7hcDes6RQhBDCoiSACyGERVkpgM9v6Qq0gLZ2z23tfqHt3XNbu18I4D1bJgcuhBDClZVa4EIIIZxIABdCCIuyRABXSk1XSu1WSu1TSs1p6fr4i1LqkFLqR6XUZqVUplmWpJRarpTaa752dDr/IfPvYLdSalrL1dx3Sqm3lFK5SqltTmVNvkel1Bjz72qfUuoFpZQK9r34op77fVQp9ZP5PW9WSs1wOmb1++2hlFqplNqplNqulLrXLG/N33F99xz871lrHdJ/gHBgP9AHiAK2AENaul5+urdDQCe3sr8Ac8ztOcBT5vYQ896jgd7m30l4S9+DD/d4HjAa2HY69wisByYAClgKXNTS99aE+30UuM/Lua3hfrsAo83tBGCPeV+t+Tuu756D/j1boQU+FtintT6gta4CFgIzW7hOgTQTWGBuLwAudypfqLWu1FofBPZh/N2ENK31auCUW3GT7lEp1QVor7X+Thv/6v/h9J6QUs/91qc13G+O1nqjuV0M7AS60bq/4/ruuT4Bu2crBPBuwBGn/Wwa/suyEg18oZTaoJSabZalaa1zwPiHAqSa5a3p76Gp99jN3HYvt5JfKaW2mikWezqhVd2vUiodGAWso418x273DEH+nq0QwL3lhFpL38eztdajgYuAu5VS5zVwbmv+e7Cr7x6tfu+vAH2BkUAO8IxZ3mruVykVD3wM/FprXdTQqV7KWss9B/17tkIAzwZ6OO13B462UF38Smt91HzNBT7FSIkcN3+1wnzNNU9vTX8PTb3HbHPbvdwStNbHtda1Wmsb8Dp1qa9Wcb9KqUiMQPae1voTs7hVf8fe7rklvmcrBPAfgP5Kqd5KqSjgemBxC9fptCml4pRSCfZtYCqwDePeZpmnzQIWmduLgeuVUtFKqd5Af4wHIFbUpHs0fwUvVkqNN5/S3+r0npBnD2SmKzC+Z2gF92vW701gp9b6b06HWu13XN89t8j33NJPdH186jsD40nvfuD3LV0fP91TH4wn01uA7fb7ApKBFcBe8zXJ6T2/N/8OdhOiT+i93OcHGL9OVmO0OO5ozj0CGeZ/iP3AS5ijiEPtTz33+w7wI7DV/M/cpRXd7zkYv/ZvBTabf2a08u+4vnsO+vcsQ+mFEMKirJBCEUII4YUEcCGEsCgJ4EIIYVESwIUQwqIkgAshhEVJABdCCIuSAC6EEBb1/wFsWz0QpPl2ZQAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(df.Close)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "weekma = df.Close.rolling(100).mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x24a10e98850>]"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(weekma)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2517, 5)"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1761, 1)\n",
      "(756, 1)\n"
     ]
    }
   ],
   "source": [
    "#Splitting into Training and Testing\n",
    "\n",
    "data_training = pd.DataFrame(df['Close'][0:int(len(df)*0.70)])\n",
    "data_testing =  pd.DataFrame(df['Close'][int(len(df)*0.70):int(len(df))])\n",
    "\n",
    "print(data_training.shape)\n",
    "print(data_testing.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Close</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>7.526071</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>7.643214</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>7.656429</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>7.534643</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>7.520714</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Close\n",
       "0  7.526071\n",
       "1  7.643214\n",
       "2  7.656429\n",
       "3  7.534643\n",
       "4  7.520714"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_training.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Close</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2512</th>\n",
       "      <td>71.067497</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2513</th>\n",
       "      <td>72.477501</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2514</th>\n",
       "      <td>72.449997</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2515</th>\n",
       "      <td>72.879997</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2516</th>\n",
       "      <td>73.412498</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          Close\n",
       "2512  71.067497\n",
       "2513  72.477501\n",
       "2514  72.449997\n",
       "2515  72.879997\n",
       "2516  73.412498"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_testing.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.02527908],\n",
       "       [0.02971782],\n",
       "       [0.03021854],\n",
       "       ...,\n",
       "       [0.84388656],\n",
       "       [0.85089656],\n",
       "       [0.84616011]])"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.preprocessing import MinMaxScaler\n",
    "\n",
    "scaler = MinMaxScaler()\n",
    "data_training_array = scaler.fit_transform(data_training)\n",
    "data_training_array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "x_train = []\n",
    "y_train = []\n",
    "\n",
    "for i in range(100, data_training_array.shape[0]):\n",
    "    x_train.append(data_training_array[i-100: i])\n",
    "    y_train.append(data_training_array[i,0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "x_train, y_train = np.array(x_train), np.array(y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1661, 100, 1)"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_train.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1661,)"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_train.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "from keras.layers import Dense, Dropout, LSTM\n",
    "from keras.models import Sequential"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "model = Sequential()\n",
    "model.add(LSTM(units = 50, activation = 'relu', return_sequences = True, input_shape = (x_train.shape[1], 1))) \n",
    "model.add(Dropout(0.2))\n",
    "\n",
    "model.add(LSTM(units = 60, activation = 'relu', return_sequences = True)) \n",
    "model.add(Dropout(0.3))\n",
    "\n",
    "model.add(LSTM(units = 80, activation = 'relu', return_sequences = True)) \n",
    "model.add(Dropout(0.4))\n",
    "\n",
    "model.add(LSTM(units = 120, activation = 'relu')) \n",
    "model.add(Dropout(0.5))\n",
    "\n",
    "model.add(Dense(units = 1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model: \"sequential\"\n",
      "_________________________________________________________________\n",
      "Layer (type)                 Output Shape              Param #   \n",
      "=================================================================\n",
      "lstm (LSTM)                  (None, 100, 50)           10400     \n",
      "_________________________________________________________________\n",
      "dropout (Dropout)            (None, 100, 50)           0         \n",
      "_________________________________________________________________\n",
      "lstm_1 (LSTM)                (None, 100, 60)           26640     \n",
      "_________________________________________________________________\n",
      "dropout_1 (Dropout)          (None, 100, 60)           0         \n",
      "_________________________________________________________________\n",
      "lstm_2 (LSTM)                (None, 100, 80)           45120     \n",
      "_________________________________________________________________\n",
      "dropout_2 (Dropout)          (None, 100, 80)           0         \n",
      "_________________________________________________________________\n",
      "lstm_3 (LSTM)                (None, 120)               96480     \n",
      "_________________________________________________________________\n",
      "dropout_3 (Dropout)          (None, 120)               0         \n",
      "_________________________________________________________________\n",
      "dense (Dense)                (None, 1)                 121       \n",
      "=================================================================\n",
      "Total params: 178,761\n",
      "Trainable params: 178,761\n",
      "Non-trainable params: 0\n",
      "_________________________________________________________________\n"
     ]
