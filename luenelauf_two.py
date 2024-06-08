import os
import tkinter as tk
from PIL import Image, ImageTk
import random
import datetime as dt
import webbrowser
from tkinter import messagebox as mb

# Clearing the screen
os.system('clear')

# Creating the gui window
page_one = tk.Tk()
page_one.title('LüneLauf')
page_one.geometry('950x700')

# Adding a background image
def add_image(page_one, file_path='P1.jpg'):
    global pic, t1
    t1 = tk.Frame(page_one)
    img = Image.open('P1.jpg')
    img = img.resize((950, 700), Image.LANCZOS)
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(t1, image=pic)
    Lab.pack()
    t1.pack()
add_image(page_one, file_path='P1.jpg')

# Creating the welcome Label
welcome_label = tk.Label(page_one,
                         text='WELCOME TO LÜNELAUF!',
                         font='Montserrat 50',
                         fg='#E5DCCB', bg='#90A5A3',
                         relief=tk.RAISED)
welcome_label.place(x=150, y=90)
# Text Label
text_label = tk.Label(page_one,
                      text='An interactive app designed by women for women. \n '
                           'Experience the world of running like you never have before.',
                      font=('Montserrat', 20, 'italic'),
                      fg='#E5DCCB',
                      bg='#90A5A3')
text_label.place(x=200, y=200)
# Name Label
name_label = tk.Label(page_one,
                      text='To continue, tell us your name below:',
                      font=('Montserrat', 20),
                      fg='#131C21',
                      bg='#BEAC96')
name_label.place(x=300, y=475)

# Name Entry Box that stores the entered name
name = tk.StringVar()
name_box = tk.Entry(page_one, textvar=name, font=('Montserrat', 15))
name_box.place(x=360, y=530)
entered_name = ''

# Creating a function to open the popup friends list
def open_popup(page_one):
    global popup_window
    popup_window = tk.Toplevel(page_one)
    popup_window.title('Friend List')
    popup_window.geometry('500x400')
    popup_window.configure(bg='#E6C394')

    # Inserting text in the pop-up window
    popup_text = tk.Label(popup_window,
                          text='Select a loved one from your contact list below to let \n'
                               'them know your location while you´re on a run.',
                          font=('Montserrat', 15),
                          fg='#FBFBFB',
                          bg='#E6C394')
    popup_text.place(x=90, y=50)

    # List of image filenames
    image_filenames = ['dad.png', 'mom.png', 'friend.png']

    # Inserting the friend and family images dynamically
    label_positions = [(50, 150), (170, 150), (300, 150)]
    for i, image_filename in enumerate(image_filenames):
        image = Image.open(image_filename)
        image_resized = image.resize((100, 50), Image.LANCZOS)
        image_tk = ImageTk.PhotoImage(image=image_resized)
        label = tk.Label(popup_window, image=image_tk)
        label.image = image_tk
        label.place(x=label_positions[i][0], y=label_positions[i][1])

    # Function to send location
    def send_location(recipient):
        res = mb.askquestion('Panic Button', f'Do you want to send your location to {recipient}?')
        if res == 'yes':
            mb.showinfo('Return', f'Your location was sent to {recipient}.')
            popup_window.destroy()
        else:
            mb.showinfo('Return', 'Returning to main page.')
            popup_window.destroy()

    # Button to send location to dad
    send_location_dad_button = tk.Button(
        popup_window,
        text='Send to dad',
        font=('Montserrat', 12),
        command=lambda: send_location('Dad'),
        relief=tk.RAISED,
        highlightbackground='#E5DCCB',
        cursor='hand2')
    send_location_dad_button.place(x=50, y=250)

    # Button to send location to mom
    send_location_mom_button = tk.Button(
        popup_window,
        text='Send to mom',
        font=('Montserrat', 12),
        command=lambda: send_location('Mom'),
        relief=tk.RAISED,
        highlightbackground='#E5DCCB',
        cursor='hand2')
    send_location_mom_button.place(x=170, y=250)

    # Button to send location to friend
    send_location_friend_button = tk.Button(
        popup_window,
        text='Send to friend',
        font=('Montserrat', 12),
        command=lambda: send_location('Friend'),
        relief=tk.RAISED,
        highlightbackground='#E5DCCB',
        cursor='hand2')
    send_location_friend_button.place(x=300, y=250)

    # Button to close the popup window
    close_button = tk.Button(popup_window, text='Close', font=('Montserrat', 15, 'bold'), bg='#EDB75C',
                             command=popup_window.destroy, cursor='hand2')
    close_button.place(x=200, y=300)

# Definition to open running group page
def open_running_group():
    global running_group
    running_group = tk.Toplevel(page_one)
    running_group.title('Find Your Running Group')
    running_group.geometry('900x600')
    running_group.configure(bg='#90A5A3')

    # Inserting the text and title
    running_group_title = tk.Label(running_group,
                                   text=f'{entered_name}, find your running buddies below!',
                                   font='Montserrat 40',
                                   fg='#1F3C4E',
                                   bg='#90A5A3')
    running_group_title.place(x=100, y=40)
    running_group_text = tk.Label(running_group,
                                  text="""Find Your Perfect Running Group: Connect with fellow women runners at your level – beginner, advanced, or expert. Run together, support each other, and achieve your goals as a team. Join us and elevate your running experience today!
                                  """,
                                  font='Montserrat 15',
                                  wraplength=750,
                                  fg='#90A5A3',
                                  bg='#E5DCCB')
    running_group_text.place(x=70, y=120)

    # Placing the image for the beginner group
    image_beginner = Image.open('beginner_group.jpg')
    image_beginner_resized = image_beginner.resize((240, 160), Image.LANCZOS)
    picture_one = ImageTk.PhotoImage(image=image_beginner_resized)
    label_beginner = tk.Label(running_group, image=picture_one)
    label_beginner.image = picture_one
    label_beginner.place(x=60, y=260)

    # Button to join the beginner group
    def show_success_message_beginner():
        mb.showinfo("Success", "🌟 You've successfully joined the Beginner Group! 🌟\n"
                               "You´ll shortly receive an e-mail with more information.")

    join_button_beginner = tk.Button(running_group, text='Join the Beginner Group', font=('Montserrat', 13),
                                     highlightbackground='#E5DCCB', command=show_success_message_beginner,
                                     relief=tk.RAISED,
                                     cursor='hand2')
    join_button_beginner.place(x=100, y=450)

    # Placing the image for the advanced group
    image_advanced = Image.open('advanced_group.jpeg')
    image_advanced_resized = image_advanced.resize((240, 160), Image.LANCZOS)
    picture_two = ImageTk.PhotoImage(image=image_advanced_resized)
    label_advanced = tk.Label(running_group, image=picture_two)
    label_advanced.image = picture_two
    label_advanced.place(x=340, y=260)

    # Defining group details
    groups = [
        {"name": "Beginner", "image": "beginner_group.jpg", "position": (60, 260)},
        {"name": "Advanced", "image": "advanced_group.jpeg", "position": (340, 260)},
        {"name": "Pro", "image": "pro_group.jpg", "position": (620, 260)}
    ]

    # Creating widgets for each group
    for group in groups:
        create_group_widgets(group)

    # Button to close the running group window
    close_button = tk.Button(running_group, text='Close', font=('Montserrat', 12), highlightbackground='#E5DCCB',
                             command=running_group.destroy, relief=tk.RAISED, cursor='hand2')
    close_button.place(x=800, y=550)

def create_group_widgets(group):
    image = Image.open(group["image"])
    image_resized = image.resize((240, 160), Image.LANCZOS)
    picture = ImageTk.PhotoImage(image=image_resized)
    label = tk.Label(running_group, image=picture)
    label.image = picture
    label.place(x=group["position"][0], y=group["position"][1])

    # Definition to display the success message
    def show_success_message():
        mb.showinfo("Success", f"🌟 You've successfully joined the {group['name']} Group! 🌟\n"
                               "You´ll shortly receive an e-mail with more information.")

    join_button = tk.Button(running_group, text=f'Join the {group["name"]} Group', font=('Montserrat', 13),
                            highlightbackground='#E5DCCB', command=show_success_message,
                            relief=tk.RAISED, cursor='hand2')
    join_button.place(x=group["position"][0] + 40, y=450)

    # Button to close the running group window
    close_button = tk.Button(running_group, text='Close', font=('Montserrat', 12), highlightbackground='#E5DCCB',
                             command=running_group.destroy, relief=tk.RAISED, cursor='hand2')
    close_button.place(x=800, y=550)

# Definition to open find routes page
def open_find_routes():
    global find_routes
    find_routes = tk.Toplevel(page_one)
    find_routes.title('Find Running Routes')
    find_routes.geometry('900x600')
    find_routes.configure(bg='#C8D499')

    # Inserting the text and title
    running_routes_title = tk.Label(find_routes,
                                    text='Find your ideal route below',
                                    font=('Montserrat', 40),
                                    fg='#C8D499', bg='#FBFBFB')
    running_routes_title.place(x=190, y=40)
    running_routes_text = tk.Label(find_routes,
                                   text='Discover Safe and Personalized Running Routes in Lüneburg: '
                                        'Tailored to women´s preferences, \n'
                                        'our routes ensure safety and enjoyment. Explore Lüneburg confidently, '
                                        'from scenic trails to urban paths.',
                                   font=('Montserrat', 15),
                                   fg='#1F3C4E', bg='#C8D499')
    running_routes_text.place(x=100, y=130)

    # Defining the details for route images and descriptions
    routes = [
        {"image": "easy_route.jpg", "name": "Kloster Lüne", "level": "easy", "distance": "4,89km", "time": "0:30h",
         "weather": "day/noon", "features": "green, historic", "position": (30, 230)},
        {"image": "intermediate_route.jpg", "name": "Rathaus", "level": "intermediate", "distance": "7,71km",
         "time": "0:50h", "weather": "all day", "features": "innercity, historic", "position": (330, 230)},
        {"image": "expert_route.jpg", "name": "Rote Schleuse", "level": "expert", "distance": "15,1km", "time": "1:44h",
         "weather": "day", "features": "scenic, green", "position": (630, 230)}
    ]

    # Creating widgets for each route
    for route in routes:
        create_route_widgets(route)

    # Button to close the find routes window
    close_button = tk.Button(find_routes, text='Close', font=('Montserrat', 13), highlightbackground='#FBFBFB',
                             command=find_routes.destroy, cursor='hand2')
    close_button.place(x=800, y=550)

# Creating the widgets for the running routes
def create_route_widgets(route):
    image = Image.open(route["image"])
    image_resized = image.resize((240, 160), Image.LANCZOS)
    picture = ImageTk.PhotoImage(image=image_resized)
    label = tk.Label(find_routes, image=picture)
    label.image = picture
    label.place(x=route["position"][0], y=route["position"][1])

    route_text = tk.Label(
        find_routes,
        text=f"{route['name']}\n"
             f"💪🏽: {route['level']}\n"
             f"👟: {route['distance']}\n"
             f"🕒: {route['time']}\n"
             f"☀️: {route['weather']}\n"
             f"⭐️: {route['features']}",
        font=('Montserrat', 14),
        justify=tk.LEFT,
        fg='#1F3C4E', bg='#E5DCCB',
        # Specifying the maximum width in one line before going to the next
        wraplength=500)
    route_text.place(x=route["position"][0] + 60, y=420)

# Definition to open blog entry one
def open_blog_entry_one(blog_title, blog_text, blog_entry_one, blog_entry_two, label_blog_one, label_blog_two):
    blog_title.destroy()
    blog_text.destroy()
    blog_entry_one.destroy()
    blog_entry_two.destroy()
    label_blog_one.destroy()
    label_blog_two.destroy()

    entry_one_title = tk.Label(blog,
                               text='Mastering the Art of Breath: \n'
                                    'Essential Breathing Techniques for Runners',
                               font=('Montserrat', 30),
                               fg='#90A5A3', bg='#1F3C4E')
    entry_one_title.place(x=150, y=30)

    blog_entry_one_text = tk.Label(
        blog,
        # This text is very long, unfortunately I was not able to figure out a better way to display the blog text,
        # as ist is very big and this is the only formatting where I did not have too much spacing between lines
        # so they would fit the page.
        text="""Running isn't just about moving your legs; it's about syncing your entire body, including your breath. Proper breathing techniques are often underestimated but can make a world of difference in your running performance. Whether you're a novice runner or a seasoned athlete, mastering the art of breath is key to unlocking your true potential and enhancing your overall running experience.

    1. Nose Breathing vs. Mouth Breathing:
    There's an ongoing debate about whether to breathe through your nose or mouth while running. The truth is, it's a combination of both. At lower intensities, nasal breathing helps filter and humidify the air, while mouth breathing becomes essential during high-intensity efforts when you need more oxygen quickly. Pay attention to your body's cues and switch between nose and mouth breathing as needed.

    2. Rhythmic Breathing:
    Rhythmic breathing involves coordinating your breath with your steps. This technique helps establish a steady breathing pattern that prevents fatigue and minimizes side stitches. A common rhythmic pattern is the 3:2 ratio – inhale for three steps, exhale for two steps. Adjust the ratio to find what works best for you, but maintaining a consistent rhythm is key.

    3. Diaphragmatic Breathing:
    Also known as belly breathing, diaphragmatic breathing engages the diaphragm to draw air deep into your lungs. This technique maximizes oxygen intake and helps relax your body. Place your hand on your abdomen – as you inhale, your belly should expand, and as you exhale, it should contract. Practice diaphragmatic breathing during your runs to enhance oxygen exchange.

    4. Relaxation and Posture:
    Your posture plays a crucial role in breathing efficiency. Maintain an upright posture with your shoulders relaxed and your chest open. Tension in your upper body restricts your lung capacity, hindering proper oxygen intake. Stay relaxed and let your breath flow naturally.

    Just as a runner's stride is unique, so is their breathing style. It's essential to explore different techniques and find what suits you best. By incorporating proper breathing practices into your running routine, you'll not only enhance your performance but also increase your enjoyment and reduce the risk of injury. So, lace up your shoes, focus on your breath, and discover the incredible synergy between your steps and the rhythm of your breath.""",
        font=('Montserrat', 12),
        # Binding the text to the left
        justify=tk.LEFT,
        fg='#1F3C4E', bg='#E5DCCB',
        # Specifying the maximum width in one line before going to the next
        wraplength=800)
    blog_entry_one_text.place(x=40, y=120)

# Definition to open blog entry two
def open_blog_entry_two(blog_title, blog_text, blog_entry_one, blog_entry_two, label_blog_one, label_blog_two):
    blog_title.destroy()
    blog_text.destroy()
    blog_entry_one.destroy()
    blog_entry_two.destroy()
    label_blog_one.destroy()
    label_blog_two.destroy()

    entry_two_title = tk.Label(blog,
                               text='Running and the Menstrual Cycle: \n'
                                    'Navigating Your Stride',
                               font=('Montserrat', 30),
                               fg='#90A5A3', bg='#1F3C4E')
    entry_two_title.place(x=220, y=30)

    blog_entry_two_text = tk.Label(
        blog,
        # As with the other blog entry, I have run into the same formatting problem. This is the only way to
        # fully display the text in the window
        text="""Running is an invigorating activity that brings countless physical and mental benefits. It's a fantastic way to stay fit, boost your mood, and challenge yourself. However, if you're a female runner, you might have noticed that your running experience can vary throughout your menstrual cycle. Understanding how your menstrual cycle affects your running performance and tailoring your approach can help you make the most out of your runs.
    The menstrual cycle consists of four main phases: the menstrual phase, the follicular phase, ovulation, and the luteal phase. Each phase is characterized by hormonal fluctuations that can impact your body's energy levels, endurance, and overall performance.

    Tips for Running with Your Cycle:

    Track Your Cycle: Keep a menstrual calendar to better understand the patterns in your energy levels and performance.
    Hydration: Stay hydrated throughout your cycle to maintain your body's equilibrium and support your runs.
    Nutrition: Adjust your nutritional intake to match your energy needs, especially during phases when your metabolism is higher.
    Listen to Your Body: If you're feeling fatigued or low on energy, opt for lighter workouts or rest days. Pushing too hard can lead to burnout.
    Mindfulness: Use running as a way to connect with your body. Practice mindfulness to stay attuned to your physical and emotional state.

    Running and the menstrual cycle are intertwined, and understanding this connection can help you tailor your running routine to your body's changing needs. Embrace the variations in your performance throughout your cycle and recognize that each phase has its own benefits. By working with your body rather than against it, you can optimize your running experience and achieve your fitness goals while respecting your body's natural rhythms.
    """,
        font=('Montserrat', 12),
        # Binding the text to the left
        justify=tk.LEFT,
        fg='#1F3C4E', bg='#E5DCCB',
        # Specifying the maximum width in one line before going to the next
        wraplength=800)
    blog_entry_two_text.place(x=40, y=140)

# Definition to open the blog page
def open_blog():
    global blog, blog_entry_one, blog_entry_two
    blog = tk.Toplevel(page_one)
    blog.title('LüneLauf Blog')
    blog.geometry('900x600')
    blog.configure(bg='#1F3C4E')

    # Inserting the text and title
    blog_title = tk.Label(blog,
                          text='LüneLauf Blog',
                          font=('Montserrat', 40),
                          fg='#90A5A3', bg='#1F3C4E')
    blog_title.place(x=350, y=40)
    blog_text = tk.Label(blog,
                         text='Welcome to our LüneLauf Blog, your ultimate source of'
                              ' empowerment and inspiration for women runners! \n'
                              'Explore our blog to discover expert insights on '
                              'breathing techniques, menstrual cycle impact, \n'
                              'training strategies, nutrition tips, and more. '
                              'Let´s run together and unleash our full potential! 🏃‍♀️🌟',
                         font=('Montserrat', 15),
                         fg='#E5DCCB', bg='#90A5A3')
    blog_text.place(x=100, y=110)

    # Placing the image for the first blog entry
    image_blog_one = Image.open('breathing_blog.jpg')
    image_blog_one_resized = image_blog_one.resize((250, 170), Image.LANCZOS)
    blog_one = ImageTk.PhotoImage(image=image_blog_one_resized)
    label_blog_one = tk.Label(blog, image=blog_one)
    label_blog_one.image = blog_one
    label_blog_one.place(x=130, y=210)

    # Placing the image for the second blog entry
    image_blog_two = Image.open('cycle_blog.jpg')
    image_blog_two_resized = image_blog_two.resize((250, 170), Image.LANCZOS)
    blog_two = ImageTk.PhotoImage(image=image_blog_two_resized)
    label_blog_two = tk.Label(blog, image=blog_two)
    label_blog_two.image = blog_two
    label_blog_two.place(x=530, y=210)

    # Button that redirects to blog entry one
    blog_entry_one = tk.Button(
        blog,
        text='Read:\n'
             'Mastering the Art of Breath:\n'
             'Essential Breathing Techniques for Runners',
        font=('Montserrat', 15),
        highlightbackground='#1F3C4E',
        fg='#1F3C4E',
        cursor='hand2',
        relief=tk.RAISED,
        command=lambda: open_blog_entry_one(blog_title, blog_text, blog_entry_one, blog_entry_two, label_blog_one,
                                            label_blog_two),
        width=30,
        height=4)
    blog_entry_one.place(x=100, y=400)

    # Button that redirects to blog entry two
    blog_entry_two = tk.Button(
        blog,
        text='Read:\n'
             'Running and the Menstrual Cycle:\n'
             'Navigating Your Stride',
        font=('Montserrat', 15),
        highlightbackground='#1F3C4E',
        fg='#1F3C4E',
        cursor='hand2',
        relief=tk.RAISED,
        command=lambda: open_blog_entry_two(blog_title, blog_text, blog_entry_one, blog_entry_two, label_blog_one,
                                            label_blog_two),
        width=30,
        height=4)
    blog_entry_two.place(x=500, y=400)

    # Button to close the blog window
    close_button = tk.Button(blog, text='Close', font=('Montserrat', 13), highlightbackground='#90A5A3',
                             command=blog.destroy, cursor='hand2')
    close_button.place(x=800, y=550)

# Destroying all items from page_one and opening the main menu
def main_menu():
    t1.destroy()
    welcome_label.destroy()
    text_label.destroy()
    name_label.destroy()
    name_box.destroy()
    enter_button.destroy()
    # Getting the stored name from page_one
    global entered_name
    entered_name = name.get()

    # Creating a new background
    def add_image(page_one, file_path='Running_background.jpg'):
        global pic, t1
        t1 = tk.Frame(page_one)
        img = Image.open('Running_background.jpg')
        img = img.resize((950, 700), Image.LANCZOS)
        pic = ImageTk.PhotoImage(img)
        Lab = tk.Label(t1, image=pic)
        Lab.pack()
        t1.pack()

    add_image(page_one, file_path='Running_background.jpg')

    # Creating welcome label for main menu
    welcome_label_two = tk.Label(
        page_one,
        text=f'Welcome, {entered_name}!',
        font=('Montserrat 35'),
        fg='#EDB75C',
        bg='#FBFBFB')
    welcome_label_two.place(x=350, y=60)

    # Adding a main text
    main_text = tk.Label(page_one,
                         text='This is LüneLauf, the ultimate running adventure for women. Unleash your inner athlete'
                              'and join us on a journey of sweat, smiles, and success! \n' \
                              'Select from the menu below to find new routes, join a running group or find smart'
                              'running tipps in our blog. 👟\n'
                              'Lace up your sneakers, hit the pavement, and let´s make every step count! 🏃‍',
                         font=('Montserrat', 12),
                         fg='#FBFBFB',
                         bg='#EDB75C')
    main_text.place(x=50, y=150)

    # Creating a label that displays today´s date
    date = dt.datetime.now()
    date_label = tk.Label(page_one,
                          text=f'🗓️ Today is {date:%A, %B %d, %Y} ',
                          font=('Montserrat', 12),
                          fg='#E6C394',
                          bg='#FBFBFB')
    date_label.place(x=700, y=50)

    # Creating a random song recommendation widget
    song_selection = [
        "🎵 Rev Up Your Run with the Perfect Soundtrack! Today´s selection for you is: Angry Woman - Ashe 🎵",
        "🎵 Step Up Your Running Game with Epic Tunes! Presenting Your Running Anthem: The Man - Taylor Swift 🎵",
        "🎵 Get in the Groove and Move! Dive into Today's Running Playlist: Victoria´s Secret - Jax 🎵",
        "🎵 Rev Up Your Run with the Perfect Soundtrack! Today´s selection for you is: Run the World (Girls) - Beyoncé 🎵",
        "🎵 Step Up Your Running Game with Epic Tunes! Presenting Your Running Anthem: God is a woman - Ariana Grande 🎵",
        "🎵 Hit the Ground Running with the Ultimate Playlist! Tune in to Today's Selection: W.I.T.C.H. - Devon Cole 🎵",
        "🎵 Run to the Rhythm with Our Tailored Playlist! This Session's Musical Boost: Feeling Myself - Nicky Minaj, Beyoncé 🎵",
        "🎵 Get in the Groove and Move! Dive into Today's Running Playlist: Savage - Meghan Thee Stallion 🎵",
        "🎵 Stride to the Beat of Your Playlist! Presenting Your Running Soundtrack: Boss Bitch - Doja Cat 🎵",
    ]
    song_recommendations = tk.Label(
        page_one,
        text=f'🌟 Today´s song selection from us to you 🌟 \n'
             f'{random.choice(song_selection)}\n'
             ' \n'
             '\n',
        font=('Montserrat', 13),
        fg='#2A1E06',
        bg='#E5DCCB')
    song_recommendations.place(x=120, y=230)

    # Function to open external playlist
    def open_weblink():
        webbrowser.open('https://open.spotify.com/playlist/5OcQgoauD1iRJzJrOksHfl?si=3ce606a87fb244d3')

    # Creating clickable label that leads to the playlist
    weblink_label = tk.Label(
        page_one,
        text='✨ Click here to listen to our full playlist! ✨',
        font=('Montserrat', 14, 'italic'),
        fg='#2A1E06',
        bg='#BEAC96',
        cursor='hand2',
        relief=tk.RAISED)
    weblink_label.place(x=300, y=285)
    weblink_label.bind('<Button-1>', lambda e: open_weblink())

    # Creating a function to execute the call (in the web version this can be linked to the phone, here, it shuts down the program)
    def call():
        res = mb.askquestion('Panic Button', 'You pressed the Panic Button. Do you really want to call the police?')
        if res == 'yes':
            page_one.destroy()
        else:
            mb.showinfo('Return', 'Returning to main page.')

    # Placing the button that redirects to the panic button window
    panic_button = tk.Button(
        page_one,
        text='🚨 PANIC BUTTON 🚨',
        font=('Montserrat', 15),
        command=call,
        relief=tk.RAISED,
        highlightbackground='#EDB75C',
        cursor='hand2')
    panic_button.place(x=700, y=650)

    # Button that redirects to the popup window with friends list
    location_button = tk.Button(
        page_one,
        text='📍Send your location to a friend',
        font=('Montserrat', 15),
        relief=tk.RAISED,
        command=lambda: open_popup(page_one),  # Pass page_one to open_popup
        highlightbackground='#EDB75C',
        cursor='hand2')
    location_button.place(x=50, y=650)

    # Button to open the running routes page
    running_routes_button = tk.Button(
        page_one,
        text='Find \n'
             'Running \n'
             'Routes',
        font=('Montserrat', 20, 'bold'),
        highlightbackground='#92760B',
        fg='#BEAC96',
        cursor='hand2',
        relief=tk.RAISED,
        command=open_find_routes,
        width=15,
        height=5)
    running_routes_button.place(x=350, y=450)

    # Button to open the running group page
    running_group_button = tk.Button(
        page_one,
        text='Find \n'
             'Running \n'
             'Groups',
        font=('Montserrat', 20, 'bold'),
        highlightbackground='#92760B',
        fg='#BEAC96',
        cursor='hand2',
        relief=tk.RAISED,
        command=open_running_group,  # Pass page_one to open_popup
        width=15,
        height=5)
    running_group_button.place(x=70, y=450)

    # Button to open the blog page
    blog_button = tk.Button(
        page_one,
        text='Our\n'
             'Blog',
        font=('Montserrat', 20, 'bold'),
        highlightbackground='#92760B',
        fg='#BEAC96',
        cursor='hand2',
        relief=tk.RAISED,
        command=open_blog,
        width=15,
        height=5)
    blog_button.place(x=630, y=450)

    # Button and definition to shut down the website
    def shutdown_website():
        page_one.destroy()

    shutdown_button = tk.Button(page_one, text='Close', font=('Montserrat', 12), highlightbackground='#E5DCCB',
                                command=shutdown_website, relief=tk.RAISED, cursor='hand2')
    shutdown_button.place(x=30, y=30)

# Button to get to the main page
enter_button = tk.Button(page_one, text='Enter', font=('Montserrat', 15, 'bold'), highlightbackground='#E5DCCB',
                         command=main_menu, relief=tk.RAISED, cursor='heart')
enter_button.place(x=435, y=585)

def shutdown_website():
    page_one.destroy()

# Button to shut down the website
shutdown_button = tk.Button(page_one, text='Close', font=('Montserrat', 12), highlightbackground='#E5DCCB',
                            command=shutdown_website, relief=tk.RAISED, cursor='hand2')
shutdown_button.place(x=30, y=30)

# Code to execute the code
page_one.mainloop()