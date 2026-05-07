from sklearn.datasets import load_diabetes

diabetes = load_diabetes()
X,Y = diabetes.data, diabetes.target

print(diabetes.DESCR)
