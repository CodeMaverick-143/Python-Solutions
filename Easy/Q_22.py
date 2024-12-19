temperature , humidity = map(int,input().split())
if temperature > 35:
    if humidity > 70:
        print("Tropical")
    else:
        print("Desert")
elif 20 <= temperature <= 35 :
    if humidity > 70:
        print("Rainy")
    elif 40 <= humidity <= 70:
        print("Average")
    else:
        print("Dry")
elif temperature < 20:
    if humidity > 70:
        print("Cold")
    else:
        print("Winter")