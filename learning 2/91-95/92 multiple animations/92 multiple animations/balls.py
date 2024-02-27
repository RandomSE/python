class Ball:

    def __init__(self, canvas, x, y, diameter, x_velocity, y_velocity, colour):
        self.canvas = canvas
        self.image = canvas.create_oval(x, y, x + diameter, y + diameter, fill=colour)
        self.xVelocity = x_velocity
        self.yVelocity = y_velocity

    def move(self):
        coordinates = self.canvas.coords(self.image)
        if coordinates[2] >= self.canvas.winfo_width() or coordinates[0] < 0:
            self.xVelocity = -self.xVelocity

        if coordinates[3] >= self.canvas.winfo_height() or coordinates[1] < 0:
            self.yVelocity = -self.yVelocity

        self.canvas.move(self.image, self.xVelocity, self.yVelocity)
