from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.createsnake()
        self.head = self.segments[0]
        self.last_heading = 0

    def createsnake(self):
        # Init snake
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        if abs(self.head.heading() - self.last_heading) == 180:
            self.head.setheading(self.last_heading)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        self.last_heading = self.head.heading()

    def up(self):
        if self.head.heading() != 90 and self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90 and self.head.heading() != 270:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != 180 and self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180 and self.head.heading() != 0:
            self.head.setheading(0)
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.setposition(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())