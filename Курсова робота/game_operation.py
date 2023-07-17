import ctypes

# Завантаження DLL
game_operation = ctypes.CDLL('./game_2.dll')



# Створення екземпляру класу GameOperation
game_op = game_operation.GameOperation()

# Виклик функцій з класу GameOperation
result = game_op.Fire(10, 5)
print("Fire result:", result)
