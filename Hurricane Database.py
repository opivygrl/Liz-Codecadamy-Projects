#!/usr/bin/env python
# coding: utf-8

# In[1]:


# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


# In[7]:


# write your update damages function here:

def update_damages(damage_list):
    new_list = []
    amount = 0
    for record in damage_list:
        if record == 'Damages not recorded':
            new_list.append('Damages not recorded')
        elif "M" in record:
            amount = float(record[0:-1]) * 1000000
            new_list.append(amount)
        elif "B" in record:
            amount = float(record[0:-1]) * 1000000000
            new_list.append(amount)
    return new_list
cleaned_damages = update_damages(damages)
print(cleaned_damages)


# In[30]:


#"Cuba I" would have the value: {'Name': 'Cuba I', 'Month': 'October', 'Year': 1924, 'Max Sustained Wind': 165, 
#'Areas Affected': ['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], 'Damage': 'Damages not recorded', 
#'Deaths': 90}
# write your construct hurricane dictionary function here:
def construct_hurricane_dictionary(Names, Months, Years, Wind, Areas, Damages, Deaths):
    hurricane_dictionary = {}
    for i in range(len(Names)):
        hurricane_dictionary[Names[i]] = {'Name': Names[i], 'Month': Months[i], 'Year': Years[i], 'Max Sustained Wind': Wind[i], 'Areas Affected': Areas[i], 'Damage': Damages[i], 'Deaths': Deaths[i]}
    return hurricane_dictionary

compiled_dictionary = construct_hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, cleaned_damages, deaths)
print(compiled_dictionary)


# In[39]:


# write your construct hurricane by year dictionary function here:
def dict_by_year(hurricanes):
    by_year = {}
    names = list(hurricanes)
    current_hurricane = {}
    #print(names)
    for i in range(len(names)):
        current_hurricane = hurricanes.get(names[i])
        current_year = current_hurricane.get("Year")
        if current_year in by_year:
            by_year.get(current_year).append(current_hurricane)
        else:
            by_year[current_year] = [current_hurricane]
    return by_year
compiled_dictionary_year = dict_by_year(compiled_dictionary)
#print(compiled_dictionary_year)


# In[55]:


# write your count affected areas function here:
#return the results in a dictionary where the keys are the affected areas and 
#the values are counts of how many times the areas were affected
def count_affected_areas(hurricanes):
    names = list(hurricanes)
    area_count = {}
    for i in range(len(names)):
        current_hurricane = hurricanes.get(names[i])
        #print(current_hurricane)
        areas = current_hurricane.get("Areas Affected") #areas is list of one hurricane's areas
#         print(areas)
#         print(str(len(areas)))
        for j in range(len(areas)):
            current_area = areas[j] #a single area from the hurricane
            if current_area in area_count: #if area has already been added to new dict
                current_count = area_count[current_area]
                area_count[current_area] = current_count +1
            else:
                area_count[current_area] = 1
    return area_count
            
count_by_area = count_affected_areas(compiled_dictionary)
print(count_by_area)


# In[60]:


# write your find most affected area function here:
def most_affected(CBA):
    most_affected_area = ""
    most_affected_count = 0
    
    areas = list(CBA)
    
    for i in range(len(areas)):
        cur_key = areas[i]
        cur_affected = CBA[cur_key]
        if cur_affected>most_affected_count:
            most_affected_count = cur_affected
            most_affected_area = cur_key
            #print("Entered if!")
        #print (cur_key)   <---verifies that all locations were checked
    return most_affected_area, most_affected_count
    
print(most_affected(count_by_area))


# In[64]:


# write your greatest number of deaths function here:
#Write a function that finds the hurricane that caused the greatest number of deaths, and how many deaths it caused.
def most_deaths(hurricanes):
    most_death_area = ""
    most_death_count = 0
    names = list(hurricanes)
    for i in range(len(names)):
        cur_key = names[i]
        cur_cane = hurricanes[cur_key]
        cur_deaths = cur_cane["Deaths"]
        if cur_deaths > most_death_count:
            most_death_count = cur_deaths
            most_death_area = cur_key
    return most_death_area, most_death_count
    
print(most_deaths(compiled_dictionary))


# In[75]:


# write your catgeorize by mortality function here:
# mortality_scale = {0: 0,
#                    1: 100,
#                    2: 500,
#                    3: 1000,
#                    4: 10000}
#Store the hurricanes in a new dictionary where the keys are mortality ratings and the values are 
#lists containing a dictionary for each hurricane that falls into that mortality rating.
def mortality_rating(hurricanes):
    by_rating = {0:[], 1:[], 2:[], 3:[], 4:[]}
    names = list(hurricanes)
    for i in range(len(names)):
        current_hurricane = hurricanes.get(names[i])
        cur_death = current_hurricane.get("Deaths")
        if cur_death < 100:
            by_rating[0].append(current_hurricane)
        elif cur_death >= 100 and cur_death < 500:
            by_rating[1].append(current_hurricane)
        elif cur_death >= 500 and cur_death < 1000:
            by_rating[2].append(current_hurricane)
        elif cur_death >= 1000 and cur_death < 10000:
            by_rating[3].append(current_hurricane)
        elif cur_death >= 10000:
            by_rating[4].append(current_hurricane)
    return by_rating
            


# In[80]:


#Write a function that finds the hurricane that caused the greatest damage, and how costly it was.
# write your greatest damage function here:
def most_damage(hurricanes):
    most_damage_area = ""
    most_damage = 0.0
    names = list(hurricanes)
    for i in range(len(names)):
        cur_key = names[i]
        cur_cane = hurricanes[cur_key]
        cur_damage = cur_cane["Damage"]
        if cur_damage == "Damages not recorded":
            continue
        if cur_damage > most_damage:
            most_damage = cur_damage
            most_damage_area = cur_key
    return most_damage_area, most_damage
    
print(most_damage(compiled_dictionary))


# In[82]:


# damage_scale = {0: 0,
#                 1: 100000000,
#                 2: 1000000000,
#                 3: 10000000000,
#                 4: 50000000000}
# Store the hurricanes in a new dictionary where the keys are damage ratings and the values are lists containing a 
# dictionary for each hurricane that falls into that damage rating.
# write your catgeorize by damage function here:
def damage_rating(hurricanes):
    by_rating = {0:[], 1:[], 2:[], 3:[], 4:[]}
    names = list(hurricanes)
    for i in range(len(names)):
        current_hurricane = hurricanes.get(names[i])
        cur_damage = current_hurricane.get("Damage")
        if cur_damage == "Damages not recorded":
            continue
        if cur_damage < 100000000:
            by_rating[0].append(current_hurricane)
        elif cur_damage >= 100000000 and cur_damage < 1000000000:
            by_rating[1].append(current_hurricane)
        elif cur_damage >= 1000000000 and cur_damage < 10000000000:
            by_rating[2].append(current_hurricane)
        elif cur_damage >= 10000000000 and cur_damage < 50000000000:
            by_rating[3].append(current_hurricane)
        elif cur_damage >= 50000000000:
            by_rating[4].append(current_hurricane)
    return by_rating

print(damage_rating(compiled_dictionary))


# In[ ]:




