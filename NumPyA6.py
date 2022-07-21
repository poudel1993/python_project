{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ca854a98",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np \n",
    "np.random.seed(100)\n",
    "X=np.random.random(20)\n",
    "Q1= np.sum(X)\n",
    "Q1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "99442eb3",
   "metadata": {},
   "outputs": [],
   "source": [
    "Q2=np.max(X)\n",
    "Q2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "92587f63",
   "metadata": {},
   "outputs": [],
   "source": [
    "G= np.random.rand(4,5)\n",
    "Q3=np.min(G,axis=1)\n",
    "Q3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "94a9a0a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "Q4=np.mean(G)\n",
    "Q4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1ca3d15a",
   "metadata": {},
   "outputs": [],
   "source": [
    "Y=[2,3,np.nan,5]\n",
    "Q5=np.nansum(Y)\n",
    "Q5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0be6e211",
   "metadata": {},
   "outputs": [],
   "source": [
    "a=np.random.rand(4)\n",
    "b=np.random.rand(4)\n",
    "Q6=np.concatenate((a,b))\n",
    "Q6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0049e62d",
   "metadata": {},
   "outputs": [],
   "source": [
    "q7=np.random.rand(4,4)\n",
    "Q7=np.concatenate((q7,q7))\n",
    "Q7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a2b7d03d",
   "metadata": {},
   "outputs": [],
   "source": [
    "q8=np.random.rand(2,4)\n",
    "Q8=np.vstack((q7,q8))\n",
    "Q8"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dda3af05",
   "metadata": {},
   "outputs": [],
   "source": [
    "Q9=np.vstack(((((q7,q7,q7,q8,q8)))))\n",
    "Q9"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d1989674",
   "metadata": {},
   "outputs": [],
   "source": [
    "g=np.random.rand(2,1)\n",
    "Q10=np.hstack((q8,g))\n",
    "Q10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "180c5546",
   "metadata": {},
   "outputs": [],
   "source": [
    "q11=np.random.random(20)\n",
    "Q11a,Q11b=np.split(q11,[5])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "888908c4",
   "metadata": {},
   "outputs": [],
   "source": [
    "Q12a,Q12b, Q12c = np.split(q11,[10,15])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b6590b3e",
   "metadata": {},
   "outputs": [],
   "source": [
    "q13=np.random.rand(5,5)\n",
    "Q13a,Q13b=np.vsplit(q13,[3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "79e63f18",
   "metadata": {},
   "outputs": [],
   "source": [
    "Q14a,Q14b=np.hsplit(q13,[3])"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
