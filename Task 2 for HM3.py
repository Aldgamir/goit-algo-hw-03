import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def main():
    # Використовуємо бібліотеку turtle для візуалізації
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Сніжинка Коха")

    t = turtle.Turtle()
    t.penup()
    t.goto(-150, 90)
    t.pendown()
    t.speed(0)
    
    for _ in range(3):
        level = int(input("Введіть рівень рекурсії (ціле число): "))
        koch_snowflake(t, level, 300)
        t.right(120) # Для кожного повороту на 120 градусів слід вводити рівень рекурсії в терміналі.

    # Закрити вікно при кліку миші
    window.mainloop()

if __name__ == "__main__":
    main()
