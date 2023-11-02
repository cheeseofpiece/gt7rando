# gt7rando
A basic customisable randomiser for Gran Turismo 7 with three whole tabs!

Runs on Python, but there is a packed exe in 'Releases' so you shouldn't need to install Python to run it! Hopefully!

And apologies in advance for how basic it is, this is literally my first coding project...

Will update the csv files when a game update is available and I have access to the data!

You can edit the csv files yourselves if you want to add custom events as ones that can appear or custom cars that can appear as well! The only thing you'll have to do is keep the data layed out the same way as the rest, which you can determine what is what by looking at the headings.

If you want to edit the csv files, they must be saved as comma delimited csvs with UTF-8 encoding!

You can now add your custom cars to a seperate csv file (named CustomCars.csv)! The file needs to exist otherwise the program will crash, so it is included in the download with three cars in there for reference: The 25th Anniversary GR Yaris, the Michelin Event 918 and the Honda eMS Event Civic FL5. You can add as many cars as you'd like to this list and not worry about updating it ever (just make sure not to overwrite it if you download the whole package again!

I would also recommend setting your cars to have custom 'Groups' where the group category is. Such as the included 'Custom1' group. This can have anything input into it and is very useful if you want to limit the pool of cars to ones you have tuned to be balanced to eachother!

I have also updated the Race and Custom tabs to have more functionality!


Here are the three tabs:


![image](https://github.com/cheeseofpiece/gt7rando/assets/88277510/b191cbaa-2fc8-4fac-be91-910a9398ea19)


![image](https://github.com/cheeseofpiece/gt7rando/assets/88277510/bc581537-08ef-467a-96f0-fe1d70183665)


![image](https://github.com/cheeseofpiece/gt7rando/assets/88277510/42f31239-10ee-47b9-9722-9a8c388b07ab)


Like I said, basic.

First, please be aware that all the data is based on the data in game, not the real world. Some data in game is wrong such as certain dimensions of cars of even some engine layouts. The types are a particular annoyance as cars like the Vulkan & FXX K should be listed as Racing Cars and not Road Cars...

The first tab is what I'd consider the main tab for most, it chooses a random event and then gives you a random car that in it's stock form is eligible for the event. Obviously you will end up with say a Hypercar Parade event with a Suzuki Swift as the car. It will be up to you if you want to take on the challenge of tuning up the car or re-rolling for a different set! There are options for disabling any tyre restriction checking (so cars that fall within the PP limit but with Sports Hards instead of Comfort Softs will show up on events that have such requirements for example), and there is an optional PP restriction which uses the PP recommended values for events which technically have no PP restriction. There is now a new option of enabling any cars within the CustomCars list to be included in the pool of cars that can be chosen for the events!



The second tab is technically the most complex. It is the Custom Race tab! This will select a random car, then a random track, then it will generate a random number of laps between 1 and whatever amount of laps will bring you just above your defined mileage (in the 'Max race mileage' section, default 50 miles), then a time of day, then a weather (rain enabled tracks will also have rain as an option).
On the right hand side there is now a new option of enabling any cars within the CustomCars list to be included in the pool of cars that can be chosen for your custom events, and you can also force override the car (custom cars included in the list)/track so it will always generate everything else around your selections!
On the left hand side is the opponent selection retriction generator. If you enable opponent generation then it will also take into account all of the ticked (and defined) restrictions underneath it and give you a field of 20 cars that fit the restrictions based on the random car it has given you. The restrictions are as follows:

Group Limit: If your car is Gr.3, your opponents will be Gr.3, if you are in a Gr.1 your opponents will be Gr.1
Make Limit: Keep all generated cars to the same brand as the players rolled/chosen car.
Engine Type: This will limit the cars by engine layout, you have an I4, you'll only get I4 opponents. Flat 6? Flat 6 opponents etc.
Type: This is: Road Car, Racing Car or Professionally Tuned.
Aspiration: Limits by Turbo, Supercharged, EV or Naturally Asipirated.
Drivetrain: If FR, then opponents FR. If 4WD, then opponenents 4WD etc.
Country: Always chooses cars of the same country of origin.
Tag: will only choose cars that have exactly the same tags as the car you are given, excluding the ones used for 'Type'. So a car with #Hybrid + #Vision Gran Turismo will only have other #Hybrid & #Vision Gran Turismo cars.
PP difference: Should be self explanatory, only picks cars within the PP difference provided, this is both above and be (Default 50, so +50 & -50)
Year difference: Same concept as PP diff, just with year of manufacture. so a 2010 car with a year difference of 10 would see 2000 - 2020.

And yes, the restrictions do stack! Also in the opponent list will be 'Player car here!' to also give you a random starting position in the custom race if you so wish.



The third tab is the GTAuto tab. This will generate a random wheel choice & a random paint choice. Then on the right hand side it will also generate custom colours & options for the livery editor. It will give you a random decal finish, paint material for custom colours & and also generate and show you a custom colour.

I hope this makes the game a little more enjoyable for those that end up using this!
