import pyautogui
import bezier
import numpy as np

def curve(start, end, control1, control2, curve_steps, duration):
    # Format points to use with bezier
    control_points = np.array([start, control1, control2, end])
    points = np.array([control_points[:,0], control_points[:,1]]) # Split x and y coordinates

    # You can set the degree of the curve here, should be less than # of control points
    # Create the bezier curve
    degree = 3
    curve = bezier.Curve(points, degree=degree)

    # You can also create it with using Curve.from_nodes(), which sets degree to len(control_points)-1
    # curve = bezier.Curve.from_nodes(points)
    delay = duration/curve_steps  # Time between movements. 1/curve_steps = 1 second for entire curve

    # Move the mouse
    for i in range(1, curve_steps+1):
        # The evaluate method takes a float from [0.0, 1.0] and returns the coordinates at that point in the curve
        # Another way of thinking about it is that i/steps gets the coordinates at (100*i/steps) percent into the curve
        x, y = curve.evaluate(i/curve_steps)
        pyautogui.moveTo(x, y)  # Move to point in curve
        pyautogui.sleep(delay)  # Wait delay

# Disable pyautogui pauses (from DJV's answer)
pyautogui.MINIMUM_DURATION = 0
pyautogui.MINIMUM_SLEEP = 0
pyautogui.PAUSE = 0

if __name__ == '__main__':
    pass
