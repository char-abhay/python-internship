light = input("Enter traffic light (red/yellow/green): ").lower()

match light:
    case "red":
        print("STOP")

    case "yellow":
        print("GET READY")

    case "green":
        print("GO")

    case _:
        print("Invalid Traffic Light")