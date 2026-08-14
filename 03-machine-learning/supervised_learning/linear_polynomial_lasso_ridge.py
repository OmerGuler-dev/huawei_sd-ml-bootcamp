import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.metrics import mean_squared_error, r2_score

np.random.seed(42)

x1 = np.random.uniform(0 , 10 , 200)
x2 = np.random.uniform(0 , 10 , 200)
x3 = np.random.uniform(0 , 10 , 200)
x4 = np.random.uniform(0 , 10 , 200)

X = np.column_stack([x1 ,x2 ,x3 ,x4 ])
print(X)

y =  (
    4
    + 2.5 * x1
    + 1.8 * x2
    + 0.15 * (x1 ** 2)
    - 0.1 * (x2 ** 2)
    + 0.2 * x1 * x2
    + np.random.normal(0,2,200)
)
#x1 ve x2 önemli features x3 ve x4 önemsiz gibi görünebilir çünkü denklemde kullanmadık

fig = plt.figure()
ax = fig.add_subplot(111,projection="3d")
ax.scatter(x1,x2,y)
ax.set_xlabel("x1")
ax.set_ylabel("x2")
ax.set_zlabel("y")
plt.title("Sentetik Veri")
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y , test_size=0.2, random_state=42)

linear_model = LinearRegression()

polynomial_model = Pipeline(
    [
        ("poly", PolynomialFeatures(degree=2,include_bias=False)),
        ("lineer",LinearRegression())
    ]
)

lasso_model = Pipeline(
    [
        ("scaler",StandardScaler()),
        ("lasso",Lasso(alpha=0.1))
    ]
)

ridge_model = Pipeline(
    [
        ("scaler",StandardScaler()),
        ("lasso",Ridge(alpha=0.1))
    ]
)

linear_model.fit(X_train,y_train)
polynomial_model.fit(X_train,y_train)
lasso_model.fit(X_train,y_train)
ridge_model.fit(X_train,y_train)

y_pred_linear = linear_model.predict(X_test)
y_pred_polynomial = polynomial_model.predict(X_test)
y_pred_lasso = lasso_model.predict(X_test)
y_pred_ridge = ridge_model.predict(X_test)

print(f"Doğrusal : mse : {mean_squared_error(y_test,y_pred_linear)})  --- R2 = {r2_score(y_test,y_pred_linear)}")
print(f"Polinomial : mse : {mean_squared_error(y_test,y_pred_polynomial)})  --- R2 = {r2_score(y_test,y_pred_polynomial)}")
print(f"Lasoo : mse : {mean_squared_error(y_test,y_pred_lasso)})  --- R2 = {r2_score(y_test,y_pred_lasso)}")
print(f"Ridge : mse : {mean_squared_error(y_test,y_pred_ridge)})  --- R2 = {r2_score(y_test,y_pred_ridge)}")


ozellik_isimleri = np.array(["x1","x2","x3","x4"])
lasso_katsayilari = lasso_model.named_steps["lasso"].coef_

for isim,katsayi in zip(ozellik_isimleri,lasso_katsayilari):
    print(f"{isim}: {katsayi}")