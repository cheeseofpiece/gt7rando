import csv
import random
import tkinter as tk
from tkinter import ttk
import colorsys

# Created by GTP_CON360

eligible_cars = []

def read_csv(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the first row
        for row in reader:
            data.append(row)
    return data

def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return None

def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        return None
    
def randomize_race():

    # Access the global eligible_cars variable
    global eligible_cars, tyre_limit_enabled, pp_opt_enabled
       
    # Choose a random event from EventList.csv
    event = random.choice(event_list)
    
    # Clear the eligible_cars list
    eligible_cars.clear()

    # Apply restrictions and filter eligible cars from CarsList.csv
    if custom_cars_race.get():
        all_cars = cars_list + custom_cars_list
    else:
        all_cars = cars_list
        
    for car in all_cars:
        if (
            (event[4] == "" or car[0] == event[4]) and
            (event[5] == "" or car[1] == event[5]) and
            (event[6] == "" or (car[2] != "" and int(car[2]) >= int(event[6]))) and
            (event[7] == "" or (car[2] != "" and int(car[2]) <= int(event[7]))) and
            (event[8] == "" or (car[3] != "" and float(car[3]) >= int(event[8]))) and
            (event[9] == "" or (car[3] != "" and float(car[3]) <= int(event[9]))) and
            (not pp_opt_enabled.get() or event[10] == "" or (car[2] != "" and float(car[3]) <= int(event[10]))) and
            (tyre_limit_enabled.get() or event[11] == "" or car[4][0] == event[11] or car[4] == event[11]) and
            (event[12] == "" or car[5] == event[12]) and
            (event[13] == "" or car[6] in event[13:20]) and
            (event[20] == "" or car[7] == event[20]) and
            (event[21] == "" or car[8] == event[21]) and
            (event[22] == "" or (car[9] != "" and int(car[9]) >= int(event[22]))) and
            (event[23] == "" or (car[9] != "" and int(car[9]) <= int(event[23]))) and
            (event[24] == "" or (car[10] != "" and int(car[10]) >= int(event[24]))) and
            (event[25] == "" or (car[10] != "" and int(car[10]) <= int(event[25]))) and
            (event[26] == "" or (car[11] != "" and int(car[11]) >= int(event[26]))) and
            (event[27] == "" or (car[11] != "" and int(car[11]) <= int(event[27]))) and
            (event[28] == "" or (car[12] != "" and int(car[12]) >= int(event[28]))) and
            (event[29] == "" or (car[12] != "" and int(car[12]) <= int(event[29]))) and
            (event[30] == "" or (car[13] != "" and int(car[13]) >= int(event[30]))) and
            (event[31] == "" or (car[13] != "" and int(car[13]) <= int(event[31]))) and
            (event[32] == "" or (car[14] != "" and int(car[14]) >= int(event[32]))) and
            (event[33] == "" or (car[14] != "" and int(car[14]) <= int(event[33]))) and
            (event[34] == "" or car[15] == event[34]) and
            (event[35] == "" or (car[16] != "" and int(car[16]) >= int(event[35]))) and
            (event[36] == "" or (car[16] != "" and int(car[16]) <= int(event[36]))) and
            (event[37] == "" or car[17] == event[37]) and
            (event[38] == "" or car[18] == event[38]) and
            (event[39] == "" or car[19] in event[39:41]) and
            (event[42] == "" or car[20] == event[42]) and
            (event[43] == "" or car[21] == event[43]) and
            (event[44] == "" or car[22] == event[44]) and
            (event[45] == "" or car[23] == event[45]) and
            (event[46] == "" or car[24] == event[46]) and
            (event[47] == "" or car[25] == event[47]) and
            (event[48] == "" or car[26] == event[48]) and
            (event[49] == "" or car[27] == event[49]) and
            (event[50] == "" or car[28] == event[50]) and
            (event[51] == "" or car[29] == event[51]) and
            (event[52] == "" or car[30] == event[52]) and
            (event[53] == "" or car[31] == event[53]) and
            (event[54] == "" or car[32] == event[54]) and
            (event[55] == "" or car[33] == event[55]) and
            (event[56] == "" or car[34] == event[56]) and
            (event[57] == "" or car[35] == event[57]) and
            (event[58] == "" or car[36] == event[58]) and
            (event[59] == "" or car[37] == event[59]) and
            (event[60] == "" or car[38] == event[60])
        ):
            eligible_cars.append(car)

    # Choose a random car from the eligible cars
    if eligible_cars:
        chosen_car = random.choice(eligible_cars)
    else:
        chosen_car = ["No eligible cars found"]

    # Display the chosen event and car in the UI
    event_label.configure(text=f"Event: {event[0]} - {event[1]}")
    if len(chosen_car) >= 2:  # Check if chosen_car has at least two elements
        car_label.configure(text=f"Car: {chosen_car[0]} {chosen_car[1]}")
    else:
        car_label.configure(text="No eligible cars found")
	
def randomize_custom():

    # Choose a random car and event
    if custom_cars_custom.get():
        gen_cars = cars_list + custom_cars_list
    else:
        gen_cars = cars_list
    
    if car_override_var.get():
        picked_car = car_combobox.get()
        picked_car = car_combobox_map.get(picked_car)
    else:
        picked_car = random.choice(gen_cars)
	
    if track_override_var.get():
        chosen_track = track_combobox.get()
        chosen_track = track_combobox_map.get(chosen_track)
    else:
        chosen_track = random.choice(tracks_list)

    # Get the value from the miles_entry box
    miles_chosen = convert_to_int(miles_entry.get())
    if miles_chosen is None:
        return

    # Randomly choose a car from CarsList.csv
    if len(cars_list) > 0:
        car_label_custom.configure(text=f"Car: {picked_car[0]} {picked_car[1]}")
        if generate_opponents_enabled.get():
            
            # Filter the cars_list based on group_limit_enabled checkbox state
            if group_limit_enabled.get():
                filtered_cars_list = [car for car in gen_cars if car[18] == picked_car[18]] 
            else:
                filtered_cars_list = gen_cars
                
             # Filter the cars_list based on group_limit_enabled checkbox state
            if make_limit_enabled.get():
                filtered_cars_list = [car for car in filtered_cars_list if car[0] == picked_car[0]]
                
            # Filter the opponents based on pp_difference_limit_enabled checkbox state
            if pp_difference_limit_enabled.get():
                pp_difference_limit = convert_to_int(pp_difference_entry.get())
                if pp_difference_limit is not None:
                    filtered_cars_list = [car for car in filtered_cars_list if abs(float(car[3]) - float(picked_car[3])) <= pp_difference_limit] 
            
            # Filter the cars_list based on engine_type_limit_enabled checkbox state
            if engine_type_limit_enabled.get():
                filtered_cars_list = [car for car in filtered_cars_list if car[17] == picked_car[17]]
            
            # Filter the cars_list based on type_limit_enabled checkbox state
            if type_limit_enabled.get():
                filtered_cars_list = [car for car in filtered_cars_list if car[19] == picked_car[19]]
            
            # Filter the cars_list based on year_difference_limit_enabled checkbox state
            if year_difference_limit_enabled.get():
                year_difference_limit = convert_to_int(year_difference_entry.get())
                if year_difference_limit is not None:
                    filtered_cars_list = [car for car in filtered_cars_list if car[2] != '' and abs(int(car[2]) - int(picked_car[2])) <= year_difference_limit]
                    
            # Filter the cars_list based on aspiration_limit_enabled checkbox state
            if aspiration_limit_enabled.get():
                filtered_cars_list = [car for car in filtered_cars_list if car[8] == picked_car[8]]
                
            # Filter the cars_list based on drivetrain_limit_enabled checkbox state
            if drivetrain_limit_enabled.get():
                filtered_cars_list = [car for car in filtered_cars_list if car[7] == picked_car[7]]
                
            # Filter the cars_list based on country_limit_enabled checkbox state
            if country_limit_enabled.get():
                filtered_cars_list = [car for car in filtered_cars_list if car[6] == picked_car[6]]
                
            # Filter the cars_list based on tag_limit_enabled checkbox state
            if tag_limit_enabled.get():
                for i in range(20, 38):
                    filtered_cars_list = [car for car in filtered_cars_list if car[i] == picked_car[i]]
                                
            # Randomly select 19 cars from filtered_cars_list
            if len(filtered_cars_list) >= 19:
                random.shuffle(filtered_cars_list)
                opponents_cars = filtered_cars_list[:19]
            else:
                opponents_cars = random.choices(filtered_cars_list, k=19)
            # Generate a random index to place "Player Car Here!" within the 19 cars
            player_car_index = random.randint(0, 19)
            # Insert the "Player Car Here!" text at the randomly chosen index
            opponents_cars.insert(player_car_index, "Player Car Here!")
            # Display the opponents cars
            opponents_text = "\n".join([car[0] + " " + car[1] if isinstance(car, list) else car for car in opponents_cars])
            opponents_label_custom.configure(text=f"Opponent Cars:\n{opponents_text}", justify="left")
        else:
            car_label_custom.configure(text=f"Car: {picked_car[0]} {picked_car[1]}")
    else:
        car_label_custom.configure(text="No cars available")

    # Randomly choose a track from TracksList.csv
    if len(tracks_list) > 0:
        track_label_custom.configure(text=f"Track: {chosen_track[0]} - {chosen_track[1]}")
        laps = random.randint(1, int(miles_chosen) // float(chosen_track[2]))
        
        # Randomly choose a time name from the given options
        available_times = []
        if chosen_track[4] != "":
            available_times.append("Early Dawn")
        if chosen_track[5] != "":
            available_times.append("Dawn")
        if chosen_track[6] != "":
            available_times.append("Sunrise")
        if chosen_track[7] != "":
            available_times.append("Early Morning")
        if chosen_track[8] != "":
            available_times.append("Late Morning")
        if chosen_track[9] != "":
            available_times.append("Afternoon")
        if chosen_track[10] != "":
            available_times.append("Evening")
        if chosen_track[11] != "":
            available_times.append("Sunset")
        if chosen_track[12] != "":
            available_times.append("Twilight")
        if chosen_track[13] != "":
            available_times.append("Night")
        if chosen_track[14] != "":
            available_times.append("Midnight")

        if available_times:
            time = random.choice(available_times)
        else:
            time = "No available time"
        if chosen_track[3] == "":
            weather = random.choice(["S01", "S02", "S03", "S04", "S05", "S06", "S07", "S08", "S09", "S10",
                                     "S11", "S12", "S13", "S14", "S15", "S16", "S17", "S18", "C01", "C02",
                                     "C03", "C04", "C05", "C06"])
        else:
            weather = random.choice(["S01", "S02", "S03", "S04", "S05", "S06", "S07", "S08", "S09", "S10",
                                     "S11", "S12", "S13", "S14", "S15", "S16", "S17", "S18", "C01", "C02",
                                     "C03", "C04", "C05", "C06", "R01", "R02", "R03", "R04", "R05", "R06",
                                     "R07", "R08"])
        laps_label.configure(text=f"Laps: {laps}")
        time_label.configure(text=f"Time: {time}")
        weather_label.configure(text=f"Weather: {weather}")
    else:
        track_label_custom.configure(text="No tracks available")

# Define lists for paint materials and decal finishes
paint_materials = ['Solid', 'Metallic', 'Pearl']
decal_finishes = ['Glossy', 'Semi-Glossy', 'Matte', 'Powder']

def randomize_gtauto():
    # Choose random values from the respective lists
    wheel = random.choice(wheels)
    chosen_paint = random.choice(paint)
    paint_material = random.choice(paint_materials)
    decal_finish = random.choice(decal_finishes)

    # Generate random HSL values
    hue = random.randint(0, 360)
    saturation = random.randint(0, 100)
    luminosity = random.randint(0, 100)

    # Display the chosen values in the UI
    wheels_label.configure(text=f"Wheels: {wheel}")
    paint_label.configure(text=f"Paint: {chosen_paint}")
    livery_label.configure(text=f"Paint Material: {paint_material}")
    hue_label.configure(text=f"Hue: {hue}")
    saturation_label.configure(text=f"Saturation: {saturation}")
    luminosity_label.configure(text=f"Luminosity: {luminosity}")
    decal_finish_label.configure(text=f"Decal Finish: {decal_finish}")

    # Convert HSL to RGB
    rgb = colorsys.hls_to_rgb(hue / 360.0, luminosity / 100.0, saturation / 100.0)
    # Convert RGB to hexadecimal color code
    hex_color = '#%02x%02x%02x' % (int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))

    # Update the color preview box
    color_preview.configure(bg=hex_color)


event_list = read_csv('EventList.csv')
cars_list = read_csv('CarsList.csv')
wheels = read_csv('WheelsList.csv')
paint = read_csv('PaintsList.csv')
tracks_list = read_csv('TracksList.csv')
custom_cars_list = read_csv('CustomCars.csv')

window = tk.Tk()
window.title("Randomizer")
window.geometry("1024x768")

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

tab_control = ttk.Notebook(window)

tab_control.pack(expand=1, fill="both")

#Race Tab

race_tab = ttk.Frame(tab_control)
tab_control.add(race_tab, text="Race")

pp_opt_enabled = tk.BooleanVar(value=False)
pp_opt_checkbox = tk.Checkbutton(race_tab, text="Enable optional PP restrictions", variable=pp_opt_enabled)
pp_opt_checkbox.pack(anchor="nw", padx=10, pady=10)

tyre_limit_enabled = tk.BooleanVar(value=False)
tyre_limit_checkbox = tk.Checkbutton(race_tab, text="Disable tyre limit checking", variable=tyre_limit_enabled)
tyre_limit_checkbox.pack(anchor="nw", padx=10, pady=10)

custom_cars_race = tk.BooleanVar(value=False)
custom_cars_checkbox = tk.Checkbutton(race_tab, text="Include Custom Cars", variable=custom_cars_race)
custom_cars_checkbox.pack(anchor="nw", padx=10, pady=10)

event_label = tk.Label(race_tab, text="Track - Event")
event_label.pack(expand=True, pady=(50, 10))
event_label.config(font=("Arial", 16))

car_label = tk.Label(race_tab, text="Make Model")
car_label.pack(expand=True)
car_label.config(font=("Arial", 16))

randomize_button = tk.Button(race_tab, text="Randomize", command=randomize_race)
randomize_button.pack(expand=True, pady=50)
randomize_button.config(font=("Arial", 12), width=20)

randomize_button.configure(command=randomize_race)

# Custom Tab
custom_tab = ttk.Frame(tab_control)
tab_control.add(custom_tab, text="Custom")

car_combobox_map = {car[0] + " " + car[1]: car for car in cars_list + custom_cars_list}
track_combobox_map = {track[1]: track for track in tracks_list}

car_label_custom = tk.Label(custom_tab, text="Car")
car_label_custom.grid(row=0, column=1, sticky="e")
car_label_custom.config(font=("Arial", 16))

track_label_custom = tk.Label(custom_tab, text="Track")
track_label_custom.grid(row=1, column=1, sticky="e")
track_label_custom.config(font=("Arial", 16))

laps_label = tk.Label(custom_tab, text="Laps")
laps_label.grid(row=3, column=1, sticky="e")
laps_label.config(font=("Arial", 16))

time_label = tk.Label(custom_tab, text="Time")
time_label.grid(row=4, column=1, sticky="e")
time_label.config(font=("Arial", 16))

weather_label = tk.Label(custom_tab, text="Weather")
weather_label.grid(row=5, column=1, sticky="e")
weather_label.config(font=("Arial", 16))

custom_cars_custom = tk.BooleanVar(value=False)
custom_cars_checkbox = tk.Checkbutton(custom_tab, text="Include Custom Cars (Opponents & Player)", variable=custom_cars_custom)
custom_cars_checkbox.grid(row=7, column=1, sticky="e")

car_override_var = tk.BooleanVar(value=False)
car_override_checkbox = tk.Checkbutton(custom_tab, text="Override Car Selection", variable=car_override_var)
car_override_checkbox.grid(row=8, column=1, sticky="e")

car_combobox = ttk.Combobox(custom_tab, values=[car[0] + " " + car[1] for car in cars_list + custom_cars_list], width=70)
car_combobox.set(cars_list[0][0] + " " + cars_list[0][1])
car_combobox.grid(row=9, column=1, sticky="e")

track_override_var = tk.BooleanVar(value=False)
track_override_checkbox = tk.Checkbutton(custom_tab, text="Override Track Selection", variable=track_override_var)
track_override_checkbox.grid(row=10, column=1, sticky="e")

track_combobox = ttk.Combobox(custom_tab, values=[track[1] for track in tracks_list], width=70)
track_combobox.set(tracks_list[0][1])
track_combobox.grid(row=11, column=1, sticky="e")

miles_label = ttk.Label(custom_tab, text="Max race mileage")
miles_label.grid(row=12, column=1, sticky="e")

miles_entry = ttk.Entry(custom_tab)
miles_entry.insert(0, "50")
miles_entry.grid(row=13, column=1, sticky="e")

randomize_button_custom = tk.Button(custom_tab, text="Randomize", command=randomize_custom)
randomize_button_custom.grid(row=14, column=1, sticky="e", padx=250)
randomize_button_custom.config(font=("Arial", 12), width=20)

opponent_limits_heading = ttk.Label(custom_tab, text="Opponent limits")
opponent_limits_heading.grid(row=0, column=0, sticky="w")

generate_opponents_enabled = tk.BooleanVar(value=False)
generate_opponents_checkbox = tk.Checkbutton(custom_tab, text="Generate opponents", variable=generate_opponents_enabled)
generate_opponents_checkbox.grid(row=1, column=0, sticky="w")

group_limit_enabled = tk.BooleanVar(value=False)
group_limit_checkbox = tk.Checkbutton(custom_tab, text="Group Limit", variable=group_limit_enabled)
group_limit_checkbox.grid(row=2, column=0, sticky="w")

make_limit_enabled = tk.BooleanVar(value=False)
make_limit_checkbox = tk.Checkbutton(custom_tab, text="Make Limit", variable=make_limit_enabled)
make_limit_checkbox.grid(row=3, column=0, sticky="w")

engine_type_limit_enabled = tk.BooleanVar(value=False)
engine_type_limit_checkbox = tk.Checkbutton(custom_tab, text="Engine Type Limit", variable=engine_type_limit_enabled)
engine_type_limit_checkbox.grid(row=4, column=0, sticky="w")

type_limit_enabled = tk.BooleanVar(value=False)
type_limit_checkbox = tk.Checkbutton(custom_tab, text="Type Limit", variable=type_limit_enabled)
type_limit_checkbox.grid(row=5, column=0, sticky="w")

aspiration_limit_enabled = tk.BooleanVar(value=False)
aspiration_limit_checkbox = tk.Checkbutton(custom_tab, text="Aspiration Limit", variable=aspiration_limit_enabled)
aspiration_limit_checkbox.grid(row=6, column=0, sticky="w")

drivetrain_limit_enabled = tk.BooleanVar(value=False)
drivetrain_limit_checkbox = tk.Checkbutton(custom_tab, text="Drivetrain Limit", variable=drivetrain_limit_enabled)
drivetrain_limit_checkbox.grid(row=7, column=0, sticky="w")

country_limit_enabled = tk.BooleanVar(value=False)
country_limit_checkbox = tk.Checkbutton(custom_tab, text="Country Limit", variable=country_limit_enabled)
country_limit_checkbox.grid(row=8, column=0, sticky="w")

tag_limit_enabled = tk.BooleanVar(value=False)
tag_limit_checkbox = tk.Checkbutton(custom_tab, text="Tag Limit", variable=tag_limit_enabled)
tag_limit_checkbox.grid(row=9, column=0, sticky="w")

pp_difference_limit_enabled = tk.BooleanVar(value=False)
pp_difference_limit_checkbox = tk.Checkbutton(custom_tab, text="PP Difference Limit", variable=pp_difference_limit_enabled)
pp_difference_limit_checkbox.grid(row=10, column=0, sticky="w")

pp_difference_label = ttk.Label(custom_tab, text="PP difference (Above and below)")
pp_difference_label.grid(row=11, column=0, sticky="w")

pp_difference_entry = ttk.Entry(custom_tab)
pp_difference_entry.insert(0, "50")
pp_difference_entry.grid(row=12, column=0, sticky="w")

year_difference_limit_enabled = tk.BooleanVar(value=False)
year_difference_limit_checkbox = tk.Checkbutton(custom_tab, text="Year Difference Limit", variable=year_difference_limit_enabled)
year_difference_limit_checkbox.grid(row=13, column=0, sticky="w")

year_difference_label = ttk.Label(custom_tab, text="Year difference (Above and below)")
year_difference_label.grid(row=14, column=0, sticky="w")

year_difference_entry = ttk.Entry(custom_tab)
year_difference_entry.insert(0, "10")
year_difference_entry.grid(row=15, column=0, sticky="w")

opponents_label_custom = tk.Label(custom_tab, text="Opponent Cars:")
opponents_label_custom.grid(row=16, column=0, sticky="w")

custom_tab.grid_columnconfigure(0, weight=1)
custom_tab.grid_columnconfigure(1, weight=1)

#GTAuto Tab

gtauto_tab = ttk.Frame(tab_control)
tab_control.add(gtauto_tab, text="GTAuto")

wheels_label = tk.Label(gtauto_tab, text="Wheels: ")
wheels_label.pack(anchor="nw", padx=10, pady=10)

paint_label = tk.Label(gtauto_tab, text="Paint: ")
paint_label.pack(anchor="nw", padx=10, pady=10)

decal_finish_label = tk.Label(gtauto_tab, text="Decal Finish: ")
decal_finish_label.pack(anchor="ne", padx=10, pady=10)

livery_label = tk.Label(gtauto_tab, text="Paint Material: ")
livery_label.pack(anchor="ne", padx=10, pady=10)

hue_label = tk.Label(gtauto_tab, text="Hue: ")
hue_label.pack(anchor="ne", padx=10, pady=3)

saturation_label = tk.Label(gtauto_tab, text="Saturation: ")
saturation_label.pack(anchor="ne", padx=10, pady=3)

luminosity_label = tk.Label(gtauto_tab, text="Luminosity: ")
luminosity_label.pack(anchor="ne", padx=10, pady=3)

color_preview = tk.Label(gtauto_tab, width=30, height=10)
color_preview.pack(anchor="ne", padx=10, pady=10)

randomize_button_gtauto = tk.Button(gtauto_tab, text="Randomize", command=randomize_gtauto)
randomize_button_gtauto.pack(expand=True, pady=20)
randomize_button_gtauto.config(font=("Arial", 12), width=20)

window.mainloop()

# Created by GTP_CON360