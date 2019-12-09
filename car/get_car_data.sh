# x y z pitch roll yaw
parkings=(
"102.96359 -894.599062442779541 1 0 0 90"
"-2 -525.874 1 0 0 0"
)

for array in "${parkings[@]}"
do
    echo "${array}"
    declare -a TMP=($(echo "${array}"))
    # setting.json作成
    cat base.json|jq ".Vehicles.PhysXCar.X|=${TMP[0]}"|jq ".Vehicles.PhysXCar.Y|=${TMP[1]}"|jq ".Vehicles.PhysXCar.Z|=${TMP[2]}"|jq ".Vehicles.PhysXCar.Pitch|=${TMP[3]}"|jq ".Vehicles.PhysXCar.Roll|=${TMP[4]}"|jq ".Vehicles.PhysXCar.Yaw|=${TMP[5]}">setting.json
    # 起動
    path/CityEnviron.exe
    # 実行
    python get_car_data.py
    # 終了
    taskkill /IM CityEnviron.exe
done
