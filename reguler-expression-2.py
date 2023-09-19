# import re

# text = "The first steam-powered vehicle was designed by Ferdinand Verbiest, a Flemish member of a Jesuit mission in China around 1672. It was a 65-centimetre-long (26 in) scale-model toy for the Kangxi Emperor that was unable to carry a driver or a passenger.[11][24][25] It is not known with certainty if Verbiest's model was successfully built or run.[25] Cugnot's 1771 fardier à vapeur, as preserved at the Musée des Arts et Métiers, Paris, France Nicolas-Joseph Cugnot is widely credited with building the first full-scale, self-propelled mechanical vehicle in about 1769; he created a steam-powered tricycle.[26] He also constructed two steam tractors for the French Army, one of which is preserved in the French National Conservatory of Arts and Crafts.[26] His inventions were limited by problems with water supply and maintaining steam pressure.[26] In 1801, Richard Trevithick built and demonstrated his Puffing Devil road locomotive, believed by many to be the first demonstration of a steam-powered road vehicle. It was unable to maintain sufficient steam pressure for long periods and was of little practical use."


# ptr = "\d{4}"



# xyz = re.finditer(ptr, text)

# # print(xyz)
# for i in xyz:
#     print(i)


import re

txt = "abc hello. 456this is me xyz abc123 1982391kjasd this is car"

ptr = "is"

mth = re.sub(ptr, "oooooooooo", txt)

print(mth)



