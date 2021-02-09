########################################
# Name:
# Collaborators:
# Estimate time spent (hrs):
########################################

from pgl import GWindow, GState, GOval, GRect, GLine
import math

def get_heading(x1, y1, x2, y2):
    """
    Returns the angle from horizontal in radians for a
    line draw between the two pairs of points. Correctly
    flips the y-axis so that positive headings proceed
    CCW from the horizontal axis and negative headings
    are measured CW from the horizontal axis.
    """
    return math.atan2(-(y2-y1),(x2-x1))


def draw_face():
    # Add your eventual callback function here






    # Add your code to create the window and draw the original
    # face here. You can choose any reasonable colors or sizes
    # of the face/window that you like.











if __name__ == '__main__':
    draw_face()
