import Constants
print(Constants.height)
step_length = Constants.height/4 + 0.37
distance = Constants.step * step_length / 1000
velocity = distance / Constants.time
calories = 0.035 * Constants.weight + velocity ** 2/ Constants.height * 0.029 * Constants.weight
print(f'Distant: {distance} Calories: {calories} ccal')
if (distance < 2):
    print("Норма не выполнена!")
elif (distance > 2 and distance < 4):
    print("Норма почти выполнена")
else :
    print("Норма выполнена!")