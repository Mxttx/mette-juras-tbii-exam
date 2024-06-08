# mette-juras-tbii-exam
# Code explanation
This Python script uses the Tkinter library to create a GUI application for a women’s running application. Here is a detailed, step-by-step explanation of the code:
Main Structure and Initialization
The script imports necessary libraries such as tkinter, tkinter.messagebox, and PIL for image processing. It initializes global variables for various popup windows.
Main Menu
The main_menu() function is the entry point of the application. It sets up the main application window (page_one) with a specific title and geometry. Background color and an image (page_one_bg.jpg) are set. Buttons are created for navigating to different sections of the application (Running Routes, Running Groups, Blog, Send Location, and a Panic Button).
Popup Windows and Functions
The open_popup() function creates a popup window to send location information to predefined contacts (Dad, Mom, Friend). Each contact has a button that triggers the send_location(recipient) function, which asks the user for confirmation and displays a message accordingly. The send_location(recipient) function handles the logic for sending location information. It uses a message box to confirm if the user wants to send their location to the specified recipient.
Running Routes
The open_find_routes() function creates a window displaying running routes. The window (find_routes) has a title, size, and background color set. The function sets up a title label and a descriptive text label. It defines a list of routes, each with details like image, name, level, distance, time, weather, and features. It then creates widgets for each route using the create_route_widgets(route) function.
The create_route_widgets(route) function sets up the GUI elements for each running route. It resizes and displays the route's image and sets up labels to display route details like name, difficulty level, distance, time, weather, and features. It uses dynamic positioning based on other widgets.
Running Groups
The open_running_group() function creates a window displaying different running groups. Similar to open_find_routes(), it sets up the window's title, size, and background color. It defines a list of groups, each with details like name, image, and position and creates widgets for each group using the create_group_widgets(group) function.
The create_group_widgets(group) function sets up the GUI elements for each running group. It resizes and displays the group's image and sets up labels as well as a join button for each group. The join button shows a success message upon being clicked.
Blog
The open_blog() function creates a window for displaying blog entries. It sets up a list of blog entries, each with a title and text and uses buttons to navigate through different blog entries.
Shutdown Function
The shutdown_website() function is used to close the application and destroys the main window (page_one).
Execution
The script calls page_one.mainloop() to start the Tkinter main loop and display the GUI.
