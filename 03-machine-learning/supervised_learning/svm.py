import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report

digits = load_digits()
print(digits.DESCR)

fig, axes = plt.subplots(nrows=2, ncols=5, figsize = (8,5), subplot_kw={"xticks": [], "yticks": []})
for i, ax in enumerate(axes.flat):
    ax.imshow(digits.images[i], cmap = "binary", interpolation = "nearest")
    ax.set_title(f"Label: {digits.target[i]}")

plt.tight_layout()
plt.show()

X = digits.data
y = digits.target

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)

svm = SVC(kernel="linear", random_state=42)

svm.fit(X_train, y_train)

y_pred = svm.predict(X_test)

cls_report = classification_report(y_test, y_pred)
print(cls_report)
