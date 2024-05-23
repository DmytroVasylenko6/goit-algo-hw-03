import turtle


def draw_koch_segment(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        draw_koch_segment(t, length, level - 1)
        t.left(60)
        draw_koch_segment(t, length, level - 1)
        t.right(120)
        draw_koch_segment(t, length, level - 1)
        t.left(60)
        draw_koch_segment(t, length, level - 1)


def draw_koch_snowflake(t, length, level):
    for _ in range(3):
        draw_koch_segment(t, length, level)
        t.right(120)


def main():
    level = int(input("Enter the recursion level: "))

    wn = turtle.Screen()
    wn.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, 100)
    t.pendown()

    length = 300
    draw_koch_snowflake(t, length, level)

    wn.mainloop()


if __name__ == "__main__":
    main()
