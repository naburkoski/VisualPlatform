
import pygame
import random
import time
import sys


# set colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# set a window to a default size
display_width = 800
display_height = 800


# Initialize pygame
pygame.init()

# set my_window
my_window = pygame.display.set_mode((display_width, display_height))
my_window.fill(white)
pygame.display.flip()

# setting title to the window
pygame.display.set_caption("Press the space bar for the sort to begin")

# initial position
x = 40
y = 40

# width of each bar
width = 10

run = True

# methods to display instructions to User


def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def message_display(text, message_height):
    large_text = pygame.font.Font('freesansbold.ttf', 20)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((display_width/2), message_height)
    my_window.blit(text_surf, text_rect)
    pygame.display.update()

# method to show the list of height


# Dis play the bars
def show(height):
    # loop to iterate each item of list
    for i in range(len(height)):
        # draw the bar based on the value generated
        pygame.draw.rect(my_window, red, (x + 30 * i, y, width, height[i]))


# Do a bubble sort
def bubble_sort(height):
    # start sorting using bubble sort technique
    count = 0
    for i in range(len(height) - 1):

        # after this iteration max element will come at last
        for j in range(len(height) - i - 1):

            # starting is greater then next element
            if height[j] > height[j + 1]:
                # save it in temporary variable
                # and swap them using temporary variable
                t = height[j]
                height[j] = height[j + 1]
                height[j + 1] = t
            draw(height)
            count += 1
            message_display("operations: " + str(count), 380)
    pygame.display.set_caption("Bubble Sort is Complete, took %s operations" % count)


# Do a selection sort
def selection_sort(height):

    count = 0
    # This value of i corresponds to how many values were sorted
    for i in range(len(height)):
        # We assume that the first item of the unsorted segment is the smallest
        lowest_value_index = i
        # This loop iterates over the unsorted items
        for j in range(i + 1, len(height)):
            if height[j] < height[lowest_value_index]:
                lowest_value_index = j
        # Swap values of the lowest unsorted element with the first unsorted
        # element
        height[i], height[lowest_value_index] = height[lowest_value_index], height[i]
        draw(height)
        count += 1
        message_display("operations: " + str(count), 380)
    pygame.display.set_caption("Selection sort is complete, took %s operations" % count)


# do a merge sort
def merge_sort(height):

    count = 0
    if len(height) > 1:
        mid = len(height) // 2
        left_half = height[:mid]
        right_half = height[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                height[k] = left_half[i]
                i = i + 1
            else:
                height[k] = right_half[j]
                j = j + 1
            k = k + 1
            draw(height)
            count += 1
            message_display("operations: " + str(count), 380)

        while i < len(left_half):
            height[k] = left_half[i]
            i = i + 1
            k = k + 1
            draw(height)
            count += 1
            message_display("operations: " + str(count), 380)

        while j < len(right_half):
            height[k] = right_half[j]
            j = j + 1
            k = k + 1
            draw(height)
            count += 1
            message_display("operations: " + str(count), 380)

    pygame.display.set_caption("Merge sort is complete, took %s operations" % count)


# Draw the bars
def draw(height):
    # fill the window
    my_window.fill(white)

    # call show method to display the list items
    show(height)

    # create a time delay
    pygame.time.delay(5)

    # update the display
    pygame.display.update()


# Generate the random bars
def generate_bars():
    # Generate a random list of values 15-20
    number_of_bars = random.randint(15, 20)
    rand_set = set()
    while len(rand_set) <= number_of_bars:
        rand_int = random.randint(0, 300)
        rand_set.add(rand_int)

    new_heights = list(rand_set)
    draw(new_heights)
    return new_heights


def load_instructions():
    message_display("Press 0 for Bubble sort", 450)
    message_display("Press 1 for Merge Sort", 480)
    message_display("Press 2 for Selection Sort", 510)
    message_display("Press 9 to quit", 630)


# combine the setup prior sorting, then call the correct sort
def setup_sort(algorithm, pressed):

    bar_height = generate_bars()
    print("Detected %s Pressed" % pressed)
    time.sleep(1)
    draw(bar_height)
    time.sleep(1)
    algorithm(bar_height)
    load_instructions()


# Set the initial display and the instructions before Starting
# bar_height = generate_bars()
load_instructions()

# infinite loop


while run:

    execute = True
    # time delay
    pygame.time.delay(1)

    # getting keys pressed
    keys = pygame.key.get_pressed()

    # iterating events
    for event in pygame.event.get():

        # if event is to quit
        if event.type == pygame.QUIT:
            # making run = false so break the while loop
            pygame.quit()
            sys.exit()

        if execute:

            if keys[pygame.K_0]:
                setup_sort(bubble_sort, "0")
                execute = False

            elif keys[pygame.K_1]:
                setup_sort(merge_sort, "1")
                execute = False

            elif keys[pygame.K_2]:
                setup_sort(selection_sort, "2")
                execute = False

            elif keys[pygame.K_9]:
                # make execute flag to true
                print("Detected 9 Pressed")
                execute = False
                pygame.quit()
                sys.exit()

# exiting the main window
pygame.quit()
sys.exit()
