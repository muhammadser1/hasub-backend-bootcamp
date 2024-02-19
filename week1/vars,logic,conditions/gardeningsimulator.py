class Planet:
  def __init__(self, sun_rain, water, is_it_wind,snow,alive):
    self.sun_rain = sun_rain
    self.water = water
    self.is_it_wind = is_it_wind
    self.snow = snow
    self.alive= alive
def check_condition(planets,type_input,water_number,wind_input):
    if(type_input==1):
        type_input="sun"
    else:
        type_input="rain"

    if(wind_input==1):
        wind_input="yes"
    else:
        wind_input="no"
    #print(type_input,water_number ,wind_input)
    for planet in planets:
        #print(planet.sun_rain," " +  planet.water," "+ planet.is_it_wind)
        if planet.sun_rain == type_input and planet.water == water_number and  planet.is_it_wind== wind_input:
            print(planet.sun_rain," "+ planet.water+ " ", planet.is_it_wind)


if __name__ == "__main__":
    planet1= Planet("sun","100","no",30,"alive")
    planet2 = Planet("sun", "50", "yes",50,"alive")
    planet3 = Planet("rain", "20", "no",70,"alive")
    planets=[planet1,planet2,planet3]
    check_weather=1
    while check_weather:
        print("1. sun?")
        print("2. rain?")
        type_input = input("describe the weather today: ")
        if type_input.isdigit() == 1:
            type_input = (int)(type_input)
            if type_input >= 1 and type_input <= 2:
                water_number = input("precipitation number: ")
                if water_number.isdigit() == 1:
                    water_number = (water_number)
                    print("1. wind?")
                    print("2. not?")
                    wind_input = input("describe the weather today: ")
                    if wind_input.isdigit() == 1:
                        wind_input = (int)(wind_input)
                        if wind_input >= 1 and wind_input <= 2:
                            check_weather=0
                            check_condition(planets,type_input,water_number,wind_input)

    check_snow=1
    i=1
    while check_snow:
        snow_number1 = input("add snow info for planet"+str(i) )
        if snow_number1.isdigit() == 1:
            snow_number1 = (int)(snow_number1)
            if snow_number1>=planets[i-1].snow:
                planets[i-1].alive="died"
            i+=1
            if(i==4):
                check_snow=0
    i=1
    for planet in planets:
        if planet.alive=="died":
            print("planet "+str(i)+ " is died"  )
        i+=1
