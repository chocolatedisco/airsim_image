# 自動でデータ集める手法の候補
## 1
1. Carを用いる
2. 確認済みの駐車場の座標からスタート
3. 数種類のコントロールを実行する(ex.前に発進, 右に発進, ...)
```
for parking in parking_list:
    for control in control_list:
        get_data(parking, control)
```
#### メリット
車を用いているので車の動きを再現できる

#### デメリット
駐車場の白線が3Dモデルとしてあるため、踏むと大きく車が傾く

## 2
1. multiRotorを用いる
2. 確認済みの駐車場の座標からスタート
3. 数種類のコントロールを実行する
```
for parking in parking_list:
    for control in control_list:
        get_data(parking, control)
```
#### メリット
邪魔な3Dモデルに影響されない

#### デメリット
動きが車っぽくなくなってしまう？

## 3
1. Carを用いる
2. 確認済みの駐車場の座標からスタート
3. 数種類のコントロールを実行する(ex.前に発進, 右に発進, ...)
4. その時のxy座標を取得しておく
5. "SimMode": "ComputerVision"を用いる
6. 取得したxy座標に従って画像を取得する(z座標無視)
```
for parking in parking_list:
    for control in control_list:
        trajectory_lists.append(get_xy(parking, control))
for trajectory_list in trajectory_lists:
    get_data(trajectory)
```
#### メリット

#### デメリット